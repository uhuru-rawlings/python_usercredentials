class Logins:
    """
    class to store all login Logins
    """
    user_login = []
    def __init__(self, user_name, passwords):
        '''
        creating instace of this class
        '''
        self.user_name = user_name
        self.passwords = passwords
    def save_login(self):
        Logins.user_login.append(self)
    # @classmethod
    # def find_account(cls, user_name):
    #     for details in cls.user_login:
    #         if(details.user_name)
    @classmethod
    def details_exist(cls, user_name):
        for details in cls.user_login:
            if(details.user_name == user_name):
                return True
        return False
