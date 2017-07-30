"""test_activity.py"""
import unittest
from app.activity import ActivityClass


class TestCasesBuckets(unittest.TestCase):
    """
    Test for existence of activity in activity creation
    Test for special character activitynames
    Test for correct output(activity creation)
    Test for deletion of existing activity
    Test for editing activity names
    Test for editing activity names with existing activity names
    Test for deletion of bucket with its activities
    """

    def setUp(self):
        """Setting up ActivityClass
        """
        self.activity_class_obj = ActivityClass()

    def tearDown(self):
        """Removing ActivityClass
        """
        del self.activity_class_obj

    def test_existing_activity(self):
        """Check to see activity name exists or not
         """
        self.activity_class_obj.activity_list = [{'owner': 'mainachrisw@gmail.com', 'bucket': 'Adventure', 'name': 'Cycling'}, {
            'owner': 'mainachrisw@gmail.com', 'bucket': 'Adventure', 'name': 'Hike'}]
        msg = self.activity_class_obj.add_activity(
            "Adventure", "Cycling", "mainachrisw@gmail.com")
        self.assertEqual(msg, "Activity name already exists")

    def test_special_characters_name(self):
        """Check for special characters in activity name
        """
        msg = self.activity_class_obj.add_activity(
            "Adventure", "Cycling!", "mainachrisw@gmail.com")
        self.assertEqual(msg, "No special characters (. , ! space [] )")

    def test_correct_output_activity(self):
        """Check for correct activity creation
        """
        msg = self.activity_class_obj.add_activity(
            "Adventure", "Cycling", "mainachrisw@gmail.com")
        self.assertEqual(
            msg, [{'owner': 'mainachrisw@gmail.com', 'bucket': 'Adventure', 'name': 'Cycling'}])

    def test_delete_activity(self):
        """Check to see if activity is deleted
        """
        self.activity_class_obj.activity_list = [{'owner': 'mainachrisw@gmail.com', 'bucket': 'Adventure', 'name': 'Cycling'}, {
            'owner': 'mainachrisw@gmail.com', 'bucket': 'Adventure', 'name': 'Hike'}]
        msg = self.activity_class_obj.delete_activity(
            'Cycling', "mainachrisw@gmail.com")
        self.assertEqual(msg, ['Hike'])

    def test_editing_activity(self):
        """Check for edits to activity name
        """
        self.activity_class_obj.activity_list = [{'owner': 'mainachrisw@gmail.com', 'bucket': 'Adventure', 'name': 'Cycling'}, {
            'owner': 'mainachrisw@gmail.com', 'bucket': 'Adventure', 'name': 'Hike'}]
        msg = self.activity_class_obj.edit_activity(
            'Cycle', 'Cycling', 'Adventure', "mainachrisw@gmail.com")
        self.assertEqual(msg, [{'owner': 'mainachrisw@gmail.com', 'bucket': 'Adventure', 'name': 'Cycle'}, {
            'owner': 'mainachrisw@gmail.com', 'bucket': 'Adventure', 'name': 'Hike'}])

    def test_edit_existing_activityname(self):
        """Check if edit name provided is similar to an existing activity
        """
        self.activity_class_obj.activity_list = [{'owner': 'mainachrisw@gmail.com', 'bucket': 'Adventure', 'name': 'Cycling'}, {
            'owner': 'mainachrisw@gmail.com', 'bucket': 'Adventure', 'name': 'Hike'}]
        msg = self.activity_class_obj.edit_activity(
            'Hike', 'Cycling', 'Adventure', "mainachrisw@gmail.com")
        self.assertEqual(msg, "Activity name already exists")

    def test_deleted_bucket(self):
        """Check if bucket deleted will have its activities deleted to
        """
        self.activity_class_obj.activity_list = [{'owner': 'mainachrisw@gmail.com', 'bucket': 'Adventure', 'name': 'Cycling'}, {
            'owner': 'mainachrisw@gmail.com', 'bucket': 'Adventure', 'name': 'Hike'}]
        res = self.activity_class_obj.deleted_bucket_activities('Adventure')
        self.assertEqual(res, None)
