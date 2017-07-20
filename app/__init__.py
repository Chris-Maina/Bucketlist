# app/__init__.py
from flask import Flask
from app import useraccounts
from app import buckets

# Initialize the app
app = Flask(__name__, instance_relative_config=True)

user_object = useraccounts.UserClass()
bucket_object = buckets.BucketClass()
from app import views

# Load the config file
app.config.from_object('config')