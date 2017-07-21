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
        self.activity_class_obj.activity_list.append(
            "{'bucket': u'Wed', 'name': u'Shopping'}")
        msg = self.activity_class_obj.add_activity("Wed", "Shopping")
        self.assertEqual(msg, "Activity name already exists.")

    def test_special_characters_name(self):
        """Check for special characters in activity name
        """
        msg = self.activity_class_obj.add_activity("Wed", "Shopp-ing")
        self.assertEqual(msg, "No special characters (. , ! space [] )")

    def test_correct_output_activity(self):
        """Check for correct activity creation
        """
        msg = self.activity_class_obj.add_activity("Wed", "Shopping")
        self.assertEqual(msg, [{'bucket': 'Wed', 'name': 'Shopping'}])

    def test_delete_activity(self):
        """Check to see if activity is deleted
        """
        self.activity_class_obj.activity_list = [{'bucket': 'Wed', 'name': 'Swim'}, {
            'bucket': 'Wed', 'name': 'Honeymoon'}, {'bucket': 'Wed', 'name': 'Shopping'}]
        msg = self.activity_class_obj.delete_activity('Shopping')
        self.assertEqual(msg, ['Swim', 'Honeymoon'])

    def test_editing_activity(self):
        """Check for edits to activity name
        """
        self.activity_class_obj.activity_list = [
            {'bucket': 'Race', 'name': 'Cycle'}, {'bucket': 'Race', 'name': 'Jump'}]
        msg = self.activity_class_obj.edit_activity('Cycling', 'Cycle', 'Race')
        self.assertEqual(msg, ['Cycling', 'Jump'])

    def test_edit_existing_activityname(self):
        """Check if edit name provided is similar to an existing activity
        """
        self.activity_class_obj.activity_list = [
            {'bucket': 'Race', 'name': 'Cycle'}, {'bucket': 'Race', 'name': 'Jump'}]
        msg = self.activity_class_obj.edit_activity('Jump', 'Cycle', 'Race')
        self.assertEqual(msg, "Activity name already exists")
        