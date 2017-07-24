""" buckets.py """
import re
from app.activity import ActivityClass

class BucketClass(object):
    """
    Handles creation of buckets
    """

    def __init__(self):
        # list to hold buckets a user creates
        self.buckets = []

    def create_bucket(self, bucket_name, user):
        """Handles creation of buckets
            Args
                bucket name
            result
                list of buckets
        """
        # Check for special characters
        if re.match("^[a-zA-Z0-9_]*$", bucket_name):
            # Get users buckets
            my_buckets = self.owner_buckets(user)
            # check if bucket name exists
            for item in my_buckets:
                if bucket_name == item['name']:
                    print (self.buckets)
                    return "Bucket name already exists."
            bucket_dict = {
                'name': bucket_name,
                'owner':user,
            }
            self.buckets.append(bucket_dict)
        else:
            return "No special characters (. , ! space [] )"
        return self.owner_buckets(user)

    def edit_bucket(self, edit_name, org_name, user):
        """Handles edits made to bucket name
            Args
                editted name and original name
            returns
                error message or a list of buckets
        """
        if re.match("^[a-zA-Z0-9_]*$", edit_name):
            # Get users buckets
            my_buckets = self.owner_buckets(user)
            for bucket in my_buckets:
                if edit_name == bucket['name']:
                    return "Bucket name already exists"
                elif org_name == bucket['name']:
                    del bucket['name']
                    edit_dict = {
                        'name': edit_name
                    }
                    bucket.update(edit_dict)
        else:
            return "No special characters (. , ! space [] )"
        return self.owner_buckets(user)

    def delete_bucket(self, bucket_name, user):
        """Handles removal of buckets using list comprehension
            Args
                 bucket name
            returns
                 list with bucket name removed
        """
        # Get users buckets
        my_buckets = self.owner_buckets(user)
        my_buckets = [bucket for bucket in my_buckets if bucket.get(
            'name') != bucket_name]
        # Delete activities with same bucket name
        activity_object = ActivityClass()
        activity_object.activity_list = [
            activity for activity in activity_object.activity_list if activity.get('bucketname') != bucket_name]
        return my_buckets

    def owner_buckets(self, user):
        """Returns buckets belonging to a user
        Args
                 user
            returns
                 list of user's bucket(s)
        """
        user_buckets = [item for item in self.buckets if item['owner'] == user]
        return user_buckets
