""" testcases-bucketlist.py"""
import unittest
from app import app
# import module useraccounts
from app.useraccounts import UserClass

class AccountTestCases(unittest.TestCase):
    """
    Test for duplicate accounts(user already exists)
    Test for short passwords
    Test for correct output/account creation
    Test login with no account
    Test login with wrong password
    Test login with existing email and password
    """
    
    def setup(self):
        """Setting up UserClass before anything
        """
        self.user = UserClass()

    def teardown(self):
        """Removing UserClass after everything
        """
        del self.user

    def test_case_pwd_equals_cpwd(self):
        """
        Args
            password =! confrim password
        Returns
            error message
        """
        msg = self.user.registeruser(
            "Chris", "mainachris@gmail.com", "chrismaina", "chrismainaw")
        self.assertEqual(msg, "Password mismatch")

    def test_case_existing_user(self):
        """
        Args
            registered user
        Returns
            error message
        """
        self.user.user_list = [
            {'username': u'chris', 'password': u'chrismaina', 'email': u'mainachrisw@gmail.com'}]
        msg = self.user.registeruser(
            "chris", "mainachris@gmail.com", "chrismaina", "chrismaina")
        self.assertEqual(msg, "User already exists")

    def test_case_short_pwd(self):
        """
        Args
            username
            email
            short password
        Returns
            error message
        """
        msg = self.user.registeruser(
            "Chris", "mainachris@gmail.com", "chris", "chris")
        self.assertEqual(
            msg, "Your password should be at least 6 characters long")

    def test_case_correct_input(self):
        """
        Args
            username(string):name of user
            email(string):user email
            password(string):user password
        Returns
            success message
        """
        msg = self.user.registeruser(
            "Chris", "mainachris@gmail.com", "chrismaina", "chrismaina")
        self.assertEqual(msg, "Successfully registered. You can now login!")
        