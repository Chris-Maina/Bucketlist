"""test_buckets.py"""
import unittest
from app.buckets import BucketClass


class TestCasesBuckets(unittest.TestCase):
    """
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

    def test_existing_bucket(self):
        """Check to see bucket name exists or not
         """
        self.bucket_class_obj.buckets = [{'owner': 'mainachrisw@gmail.com', 'name': 'Rave'},
                                         {'owner': 'mainachrisw@gmail.com', 'name': 'Adventure'}]
        msg = self.bucket_class_obj.create_bucket(
            "Rave", "mainachrisw@gmail.com")
        self.assertEqual(msg, "Bucket name already exists.")

    def test_special_characters(self):
        """Check for special characters in bucket name
        """
        user = "mainachrisw@gmail.com"
        msg = self.bucket_class_obj.create_bucket("Huwai.Gems-2018", user)
        self.assertEqual(msg, "No special characters (. , ! space [] )")

    def test_correct_output(self):
        """Check for correct bucket creation
        """
        msg = self.bucket_class_obj.create_bucket(
            'Rave', "mainachrisw@gmail.com")
        self.assertEqual(
            msg, [{'owner': 'mainachrisw@gmail.com', 'name': 'Rave'}])

    def test_delete_bucket(self):
        """Check to see if bucket is deleted
        """
        self.bucket_class_obj.buckets = [{'owner': 'mainachrisw@gmail.com', 'name': 'Rave'}, {
            'owner': 'mainachrisw@gmail.com', 'name': 'Adventure'}, {'owner': 'mainachrisw@gmail.com', 'name': 'Shagz'}]
        msg = self.bucket_class_obj.delete_bucket(
            'Rave', "mainachrisw@gmail.com")
        self.assertEqual(msg, [{
            'owner': 'mainachrisw@gmail.com', 'name': 'Adventure'}, {'owner': 'mainachrisw@gmail.com', 'name': 'Shagz'}])

    def test_editing_buckets(self):
        """Check for edits to bucket name
        """
        self.bucket_class_obj.buckets = [{'owner': 'mainachrisw@gmail.com', 'name': 'Rave'}, {
            'owner': 'mainachrisw@gmail.com', 'name': 'Shagz'}]
        msg = self.bucket_class_obj.edit_bucket(
            'Swim', 'Rave', "mainachrisw@gmail.com")
        self.assertEqual(msg, [{'owner': 'mainachrisw@gmail.com', 'name': 'Swim'}, {
            'owner': 'mainachrisw@gmail.com', 'name': 'Shagz'}])

    def test_edit_existing_bucketname(self):
        """Check if edit name provided is similar to an existing bucket
        """
        self.bucket_class_obj.buckets = [{'owner': 'mainachrisw@gmail.com', 'name': 'Rave'}, {
            'owner': 'mainachrisw@gmail.com', 'name': 'Shagz'}]
        msg = self.bucket_class_obj.edit_bucket('Shagz', 'Rave', "mainachrisw@gmail.com")
        self.assertEqual(msg, "Bucket name already exists")
        