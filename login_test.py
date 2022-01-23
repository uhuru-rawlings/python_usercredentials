import unittest
from login import Logins #importing login Logins class

class TestLogins(unittest.TestCase):
    def setUp(self):
        self.new_Logins = Logins("uhururawlings","rawlings")
    def test_init(self):
        self.assertEqual(self.new_Logins.user_name,"uhururawlings")
        self.assertEqual(self.new_Logins.passwords,"rawlings")

    def test_save_details(self):
        self.new_Logins.save_login()
        self.assertEqual(len(Logins.user_login), 1)
    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        Logins.user_login = []
    def test_details_exist(self):
        self.new_Logins.save_login()
        test_contact = Logins("uhururawlings40","uhururawlings")
        test_contact.save_login()
        details_exists = Logins. details_exist("uhururawlings40")
        self.assertTrue(details_exists)
if __name__ == '__main__':
    unittest.main()