"""activity.py"""
import re

class ActivityClass(object):
    """Handles creation,editing and deletion of buckets
    """

    def __init__(self):
        # list to hold activities within a bucket
        self.activity_list = []

    def add_activity(self, bucketname, activity_name):
        """Handles adding an activity to a bucket
            Args
                bucket name
            result
                list of buckets
        """
        # Check for special characters
        if re.match("^[a-zA-Z0-9_]*$", activity_name):
            for item in self.activity_list:
                if item['name'] == activity_name:
                    return "Activity name already exists"
            activity_dict = {
                'name': activity_name,
                'bucket': bucketname
            }
            self.activity_list.append(activity_dict)
            return self.activity_list
        else:
            return "No special characters (. , ! space [] )"
        