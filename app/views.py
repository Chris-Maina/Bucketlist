""" views.py """
from functools import wraps
from flask import render_template, request, session
from app import app, user_object, bucket_object, activity_object


def authorize(f):
    @wraps(f)
    def check(*args, **kwargs):
        if "logged_in" in session:
            return f(*args, **kwargs)
        else:
            msg = "Please login"
            return render_template("bucketlist-login.html", resp=msg)
    return check


@app.route('/')
def index():
    """Handles rendering of index page
    """
    return render_template("index.html")


@app.route('/register', methods=['GET', 'POST'])
def register():
    """Handles registeration of users
    """
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        cpassword = request.form['confirm-password']

        msg = user_object.registeruser(username, email, password, cpassword)
        if msg == "Successfully registered. You can now login!":
            return render_template("bucketlist-login.html", resp=msg)
        else:
            return render_template("bucketlist-reg-login.html", resp=msg)
    return render_template("bucketlist-reg-login.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    """Handles logging in
    """
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        msg = user_object.login(email, password)
        if msg == "Successfully logged in, create buckets!":
            session['email'] = email
            session['logged_in'] = True
            return render_template('bucketlist-bucket.html', resp=msg)
        else:
            return render_template('bucketlist-login.html', resp=msg)
    return render_template("bucketlist-login.html")


@app.route('/bucketlist-bucket', methods=['GET', 'POST'])
@authorize
def bucket():
    """Handles bucket creation
    """
    user = session['email']
    user_buckets = bucket_object.owner_buckets(user)
    if request.method == 'POST':
        bucket_name = request.form['bucket-name']
        msg = bucket_object.create_bucket(bucket_name, user)
        if isinstance(msg, list):
            return render_template('bucketlist-bucket.html', bucketlist=msg)
        else:
            return render_template('bucketlist-bucket.html', resp=msg, bucketlist=user_buckets)
    return render_template('bucketlist-bucket.html', bucketlist=user_buckets)


@app.route('/edits', methods=['GET', 'POST'])
@authorize
def save_edits():
    """ Handles editing of buckets """

    user = session['email']
    user_buckets = bucket_object.owner_buckets(user)
    if request.method == 'POST':
        edit_name = request.form['temp_bucket_name']
        org_name = request.form['org_bucket_name']
        msg = bucket_object.edit_bucket(edit_name, org_name, user)
        if msg == bucket_object.buckets:
            response = "Successfully edited bucket " + org_name
            return render_template('bucketlist-bucket.html', resp=response, bucketlist=msg)
        else:
            #existing = bucket_object.buckets
            return render_template('bucketlist-bucket.html', resp=msg, bucketlist=user_buckets)
    return render_template('bucketlist-bucket.html')


@app.route('/delete', methods=['GET', 'POST'])
@authorize
def delete():
    """Handles deletion of buckets and its activies
    """
    user = session['email']
    if request.method == 'POST':
        del_name = request.form['temp_bucket_name']
        msg = bucket_object.delete_bucket(del_name, user)
        # Delete the its activies
        activity_object.deleted_bucket_activities(del_name)
        response = "Successfuly deleted bucket " + del_name
        return render_template('bucketlist-bucket.html', resp=response, bucketlist=msg)


@app.route('/bucketlist-activity/<bucketname>', methods=['GET', 'POST'])
@authorize
def activity(bucketname):
    """Handles creation of activities
    """

    user = session['email']
    # Get a list of users activities for a specific bucketname
    user_activities = activity_object.owner_activities(user)
    new_list = [item['name']
                for item in user_activities if item['bucket'] == bucketname]
    if request.method == 'POST':
        activity_name = request.form['activity-name']
        msg = activity_object.add_activity(bucketname, activity_name, user)
        if isinstance(msg, list):
            new_list = [item['name']
                        for item in msg if item['bucket'] == bucketname]
            return render_template("bucketlist-activity.html", activitylist=new_list, name=bucketname)
        else:
            # Display list of the bucket name already created by user
            return render_template("bucketlist-activity.html", resp=msg, activitylist=new_list, name=bucketname)
    else:
        response = "You can now add your activities"
        return render_template("bucketlist-activity.html", resp=response, name=bucketname, activitylist=new_list)


@app.route('/edit-activity', methods=['GET', 'POST'])
@authorize
def edit_activity():
    """ Handles editing of activities
    """

    user = session['email']
    if request.method == 'POST':
        activity_name = request.form['activity_name']
        activity_name_org = request.form['activity_name_org']
        bucket_name = request.form['bucket_name']
        msg = activity_object.edit_activity(
            activity_name, activity_name_org, bucket_name, user)
        if isinstance(msg, list):
            response = "Successfully edited activity " + activity_name_org
            # Get edited list of the current bucket
            new_list = [item['name']
                        for item in msg if item['bucket'] == bucket_name]
            return render_template("bucketlist-activity.html", activitylist=new_list, name=bucket_name, resp=response)
        else:
            # Get user's activities in the current bucket
            user_activities = activity_object.owner_activities(user)
            new_list = [item['name']
                        for item in user_activities if item['bucket'] == bucket_name]
    return render_template("bucketlist-activity.html", activitylist=new_list, name=bucket_name, resp=msg)


@app.route('/delete-activity', methods=['GET', 'POST'])
@authorize
def delete_activity():
    """ Handles deletion of activities
    """
    user = session['email']
    if request.method == 'POST':
        activity_name = request.form['activity_name']
        bucket_name = request.form['bucket_name']
        msg = activity_object.delete_activity(activity_name, user)
        response = "Successfuly deleted activity " + activity_name
        return render_template("bucketlist-activity.html", activitylist=msg, name=bucket_name, resp=response)


@app.route('/logout')
@authorize
def logout():
    """Handles logging out of users"""
    session.pop('email', None)
    return render_template("index.html")
