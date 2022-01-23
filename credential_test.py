import unittest
from credential import Credentials #importing credentials from credentials.py

class TestAccounts(unittest.TestCase):
    def setUp(self) -> None:
        self.new_account = Credentials("facebook","uhururawlings","rawlings")
    def test_init(self):
        self.assertEqual(self.new_account.account_name, "facebook")
        self.assertEqual(self.new_account.user_name, "uhururawlings")
        self.assertEqual(self.new_account.user_password, "rawlings")
    def test_save_credentials(self):
        self.new_account.save_credentials()
        self.assertEqual(len(Credentials.account_details), 1)
    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        Credentials.account_details = []
    def test_save_multiple(self):
        self.new_account.save_credentials()
        test_contact = Credentials("instagram","uhuru","rawlings")
        test_contact.save_credentials()
        self.assertEqual(len(Credentials.account_details), 2)
    def test_delete_credentials(self):
        self.new_account.save_credentials()
        test_contact = Credentials("twiter","uhuru1","rawlings1") # new contact
        test_contact.save_credentials()
        self.new_account.delete_credentials()
        self.assertEqual(len(Credentials.account_details), 1)
    def test_find_by_username(self):
        self.new_account.save_credentials()
        test_accounts = Credentials("telegrams","uhurus","rawlings") # new contact
        test_accounts.save_credentials()
        found_accounts = Credentials.search_by_username("uhurus")
        self.assertEqual(found_accounts.user_name , test_accounts.user_name)
    def test_find_by_account(self):
        self.new_account.save_credentials()
        test_account = Credentials("telegram","uhuru3","rawlings3") # new contact
        test_account.save_credentials()
        found_account = Credentials.exist_credentials("telegram")
        self.assertEqual(found_account.account_name , test_account.account_name)

    def test_display_all_contact(self):
        self.assertEqual(Credentials.display_credentials(),Credentials.account_details)
if __name__ == '__main__':
    unittest.main()