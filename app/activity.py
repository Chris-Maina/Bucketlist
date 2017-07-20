"""activity.py"""
import re

class ActivityClass(object):
    """Handles creation,editing and deletion of buckets
    """

    def __init__(self):
        # list to hold activities within a bucket
        self.activity_list = []
        