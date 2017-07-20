"""test_buckets.py"""
import unittest
from app.buckets import BucketClass

class TestCasesBuckets(unittest.TestCase):
    """
    Test for empty bucket name
    Test for existence of bucket in bucket creation
    Test for special character bucketnames
    Test for correct output(bucket creation)
    Test for deletion of existing bucket
    Test for editing bucketnames
    Test for editing bucketnames with existing bucketnames
    """
    
    def setUp(self):
        """Setting up BucketClass
        """
        self.bucket_class_obj = BucketClass()

    def tearDown(self):
        """Removing BucketClass
        """
        del self.bucket_class_obj
        