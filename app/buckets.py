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
    