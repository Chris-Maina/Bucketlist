""" buckets.py """
import re

class BucketClass(object):
    """
    Handles creation of buckets
    """

    def __init__(self):
        # list to hold buckets a user creates
        self.buckets = []

    def create_bucket(self, bucket_name):
        """Handles creation of buckets
            Args
                bucket name
            result
                list of buckets
        """
        # Check for special characters
        if re.match("^[a-zA-Z0-9_]*$", bucket_name):
            # check if bucket name exists
            for item in self.buckets:
                if bucket_name == item['name']:
                    return "Bucket name already exists."
            bucket_dict = {
                'name': bucket_name,
            }
            self.buckets.append(bucket_dict)
        else:
            return "No special characters (. , ! space [] )"
        return self.buckets

    def edit_bucket(self, edit_name, org_name):
        """Handles edits made to bucket name
            Args
                editted name and original name
            returns
                error message or a list of buckets
        """
        if re.match("^[a-zA-Z0-9_]*$", edit_name):
            for bucket in self.buckets:
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
        return self.buckets