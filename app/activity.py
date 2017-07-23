"""activity.py"""
import re

class ActivityClass(object):
    """Handles creation,editing and deletion of buckets
    """

    def __init__(self):
        # list to hold activities within a bucket
        self.activity_list = []

    def add_activity(self, bucketname, activity_name, user):
        """Handles adding an activity to a bucket
            Args
                bucket name
            result
                list of buckets
        """
        # Check for special characters
        if re.match("^[a-zA-Z0-9_]*$", activity_name):
            # Get users activities
            my_activities = self.owner_activities(user)
            for item in my_activities:
                if item['name'] == activity_name:
                    return "Activity name already exists"
            activity_dict = {
                'name': activity_name,
                'bucket': bucketname,
                'owner': user
            }
            self.activity_list.append(activity_dict)
            return self.owner_activities(user)
        else:
            return "No special characters (. , ! space [] )"

    def edit_activity(self, activity_name, org_activity_name, bucket_name, user):
        """Handles editing of activities
            Args
                editted name and original name
            returns
                error message or a list of activities
        """
        # Get users activities
        my_activities = self.owner_activities(user)
        for activity in my_activities:
            if activity['bucket'] == bucket_name:
                if activity['name'] != activity_name:
                    if activity['name'] == org_activity_name:
                        del activity['name']
                        edit_dict = {
                            'name': activity_name,
                        }
                        activity.update(edit_dict)
                else:
                    return "Activity name already exists"
        return my_activities

    def delete_activity(self, activity_name, user):
        """Handles deletion of bucket activities
        Args
            activity name
        returns
            list with activity name removed
        """
        # Get users activities
        my_activities = self.owner_activities(user)
        my_activities = [activity for activity in my_activities if activity.get(
            'name') != activity_name]
        deleted_activity_list = []
        for activity in my_activities:
            deleted_activity_list.append(activity['name'])
        return deleted_activity_list

    def owner_activities(self, user):
        """Returns activities belonging to a user
        Args
                 user
            returns
                 list of user's activities
        """
        user_activities = [item for item in self.activity_list if item['owner'] == user]
        return user_activities

