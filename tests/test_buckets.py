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

    def test_empty_field(self):
        """Check to see empty bucket name field
        """
        msg = self.bucket_class_obj.create_bucket("")
        self.assertEqual(msg, "[]")

    def test_existing_bucket(self):
        """Check to see bucket name exists or not
         """
        self.bucket_class_obj.buckets.append("Rave")
        msg = self.bucket_class_obj.create_bucket("Rave")
        self.assertEqual(msg, "Bucket name already exists.")
        
    def test_special_characters(self):
        """Check for special characters in bucket name
        """
        msg = self.bucket_class_obj.create_bucket("Huwai.Gems-2018")
        self.assertEqual(msg, "No special characters (. , ! space [] )")