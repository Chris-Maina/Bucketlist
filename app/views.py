""" views.py """

from flask import render_template
from app import app

@app.route('/')
def index():
    """Handles rendering of index page
    """
    return render_template("index.html")


@app.route('/register', methods=['GET', 'POST'])
def register():
    """Handles registeration of users
    """
    return render_template("bucketlist-reg-login.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    """Handles logging in
    """
    return render_template("bucketlist-login.html")


@app.route('/bucketlist-bucket', methods=['GET', 'POST'])
def bucket():
    """Handles bucket creation
    """
    return render_template("bucketlist-login.html")

@app.route('/bucketlist-activity', methods=['GET', 'POST'])
def activity():
    """Handles creation of activities
    """
    return render_template("bucketlist-activity.html")
   