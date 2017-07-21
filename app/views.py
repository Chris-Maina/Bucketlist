""" views.py """

from flask import render_template, request, session
from app import app, user_object, bucket_object, activity_object

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
            return render_template('bucketlist-bucket.html', resp=msg)
        else:
            return render_template('bucketlist-login.html', resp=msg)
    return render_template("bucketlist-login.html")


@app.route('/bucketlist-bucket', methods=['GET', 'POST'])
def bucket():
    """Handles bucket creation
    """
    if 'email' in session.keys():
        if request.method == 'POST':
            bucket_name = request.form['bucket-name']
            msg = bucket_object.create_bucket(bucket_name)
            if msg == bucket_object.buckets:
                return render_template('bucketlist-bucket.html', bucketlist=msg)
            else:
                return render_template('bucketlist-bucket.html', resp=msg, bucketlist=bucket_object.buckets)
        return render_template('bucketlist-bucket.html', bucketlist=bucket_object.buckets)
    return render_template("bucketlist-login.html")

@app.route('/edits', methods=['GET', 'POST'])
def save_edits():
    """ Handles editing of buckets """
    if 'email' in session.keys():
        if request.method == 'POST':
            edit_name = request.form['temp_bucket_name']
            org_name = request.form['org_bucket_name']
            msg = bucket_object.edit_bucket(edit_name, org_name)
            if msg == bucket_object.buckets:
                response = "Successfully edited bucket"
                return render_template('bucketlist-bucket.html', resp=response, bucketlist=msg)
            else:
                existing = bucket_object.buckets
                return render_template('bucketlist-bucket.html', resp=msg, bucketlist=existing)
        return render_template('bucketlist-bucket.html')
    return render_template("bucketlist-login.html")

@app.route('/delete', methods=['GET', 'POST'])
def delete():
    """Handles deletion of buckets
    """
    if 'email' in session.keys():
        if request.method == 'POST':
            del_name = request.form['temp_bucket_name']
            msg = bucket_object.delete_bucket(del_name)
            response = "Successfuly deleted bucket"
            return render_template('bucketlist-bucket.html', resp=response, bucketlist=msg)
    return render_template("bucketlist-login.html")

@app.route('/bucketlist-activity/<bucketname>', methods=['GET', 'POST'])
def activity(bucketname):
    """Handles creation of activities
    """
    if 'email' in session.keys():
        if request.method == 'POST':
            activity_name = request.form['activity-name']
            msg = activity_object.add_activity(bucketname, activity_name)
            print(msg)
            new_list = [item['name'] for item in activity_object.activity_list if item['bucket'] == bucketname]
            if not isinstance(msg, basestring):
                return render_template("bucketlist-activity.html", activitylist=new_list, name=bucketname)
            else:
                # Display list of the bucket name already created
                return render_template("bucketlist-activity.html", resp=msg, activitylist=new_list)
        else:
            response = "You can now add your activities"
            new_list = [item['name'] for item in activity_object.activity_list if item['bucket'] == bucketname]
            return render_template("bucketlist-activity.html", resp=response, name=bucketname, activitylist=new_list)
    return render_template("bucketlist-login.html")

@app.route('/edit-activity', methods=['GET', 'POST'])
def edit_activity():
    """ Handles editing of activities
    """
    if 'email' in session.keys():
        if request.method == 'POST':
            activity_name = request.form['activity_name']
            activity_name_org = request.form['activity_name_org']
            bucket_name = request.form['bucket_name']
            msg = activity_object.edit_activity(
                activity_name, activity_name_org, bucket_name)
            new_list = [item['name'] for item in activity_object.activity_list if item['bucket'] == bucket_name]
            if not isinstance(msg, basestring):
                response = "Successfully edited activity"
                return render_template("bucketlist-activity.html", activitylist=new_list, name=bucket_name, resp=response)
            else:
                return render_template("bucketlist-activity.html", activitylist=new_list, name=bucket_name, resp=msg)
    return render_template("bucketlist-login.html")

@app.route('/delete-activity', methods=['GET', 'POST'])
def delete_activity():
    """ Handles deletion of activities
    """
    if 'email' in session.keys():
        if request.method == 'POST':
            activity_name = request.form['activity_name']
            bucket_name = request.form['bucket_name']
            msg = activity_object.delete_activity(activity_name)
            response = "Successfuly deleted activity"
            return render_template("bucketlist-activity.html", activitylist=msg, name=bucket_name, resp=response)
    return render_template("bucketlist-login.html")
