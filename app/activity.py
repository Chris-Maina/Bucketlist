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

    def edit_activity(self, activity_name, org_activity_name, bucket_name):
        """Handles editing of activities
            Args
                editted name and original name
            returns
                error message or a list of activities
        """
        edit_activity_list = []
        for activity in self.activity_list:
            if activity['bucket'] == bucket_name:
                if activity['name'] != activity_name:
                    if activity['name'] == org_activity_name:
                        del activity['name']
                        edit_dict = {
                            'name': activity_name,
                        }
                        activity.update(edit_dict)
                        return self.activity_list
                else:
                    return "Activity name already exists"
        return edit_activity_list

    def delete_activity(self, activity_name):
        """Handles deletion of bucket activities
        Args
            activity name
        returns
            list with activity name removed
        """
        self.activity_list = [activity for activity in self.activity_list if activity.get(
            'name') != activity_name]
        deleted_activity_list = []
        for activity in self.activity_list:
            deleted_activity_list.append(activity['name'])
        return deleted_activity_list
