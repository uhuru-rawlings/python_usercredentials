from curses.ascii import CR


class Credentials :
    """
    class that contains accounts credentials
    """
    account_details = []
    def __init__(self, account_name, user_name, user_password):
        '''
        instanciating
        '''
        self.account_name = account_name
        self.user_name = user_name
        self.user_password = user_password
    def save_credentials(self):
        Credentials.account_details.append(self)
    def delete_credentials(self):
        Credentials.account_details.remove(self)
    @classmethod
    def search_by_username(cls, user_name):
        for details in Credentials.account_details:
            if(details.user_name == user_name):
                return details
    @classmethod
    def exist_credentials(self, accounts_name):
        for details in Credentials.account_details:
            if(details.account_name == accounts_name):
                return details
    @classmethod
    def display_credentials(cls):
        return Credentials.account_details