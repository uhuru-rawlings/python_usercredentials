#!/usr/bin/env python3.6
from ast import Break, Pass
from login import Logins
from credential import Credentials

def create_Account(user_name, passwords):
    newLogins = Logins(user_name, passwords)
    return newLogins
def save_login(newLogins):
    newLogins.save_login()
def login_user(newLogins):
    newLogins.save_login()
def login_exists(user_name):
    Logins.details_exist(user_name)
def create_Accounts(account_name, user_name, user_password):
    account = Credentials(account_name, user_name, user_password)
    return account
def save_account(account):
    account.save_credentials()
def delete_account(account):
    account.delete_credentials()
def search_account(account):
    return Credentials.search_by_username(account)
def search_accountname(account):
    return Credentials.exist_credentials(account)
def logout():
    exit()


def main():
    print("#" * 100)
    print("#" * 1 + " " * 98 + "#" * 1)
    print("#" * 1 + " " * 31 + "WELCOME TO PYTHON SAVE CREDENTIALS" + " " * 33 + "#")
    print("#" * 1 + " " * 98 + "#" * 1)
    print("#" * 100)
    print(" " * 100)
    print("Please pick a number that represent an action")
    print("(A)=> LOGIN, (B)=>SIGNUP")
    print(" " * 100)
    select = input("Selection ?__")
    if(select.upper() == "A"):
        print("SELECTED => LOGIN")
        print(" " * 100)
        print("Enter USERNAME")
        username = input("username ?")
        print("ENTER PASSWORD")
        password = input("password ?")
        logins = login_exists(username)
        if(logins):
            print("LOGIN SUCCESSFULL")
        else:
            print("DETAILS DONT EXIST")
    elif(select.upper() == "B"):
        print("SELECTED => SIGNUP")
        print(" " * 100)
        print("ENTER USERNAME")
        username = input("username ?")
        print("ENTER PASSWORD")
        password = input("password ?")
        savelogin = save_login(create_Account(username,password))
        print("WELCOME " + username)
        print("ACCOUNT CREATED SUCCESFULLY")
        print("PLEASE PICK AN OPTION THAT REPRESENT AN ACTION")
        print("(A)=> SAVE ACCOUNT \n (B)=>SEARCH ACCOUNT \n (C)=> DELETE ACCOUNT \n (D)=> EXIT PROCES")
        options = input("Selection ?")
        if(options.upper() == "A"):
            print("SELECTED => SAVE ACCOUNT")
            print("ENTER ACCOUNT_NAME e.g facebook")
            account = input("Account ?")
            print("ENTER USER-NAME")
            username = input("Username ?")
            print("ENTER PASSWORD")
            password = input("Password ?")
            saveaccount = save_account(create_Accounts(account, username, password))
            print("DETAILS ADDED SUCCESSFULLY")
            print("PLEASE PICK AN OPTION THAT REPRESENT AN ACTION")
            print("(A)=>SEARCH ACCOUNT \n (B)=> DELETE ACCOUNT \n (C)=> EXIT PROCES")
            options1 = input("Selection ?")
            if(options1.upper() == "A"):
                print("SELECTION => SEARCH ACCOUNT")
                print("ENTER USERNAME OR ACCOUNT NAME")
                searchdet = input("search ?")
                accountres = search_account(searchdet)
                if(accountres):
                    print("Account:__" + accountres.account_name)
                    print("UserName:__"+ accountres.user_name)
                    print("Password:__" + accountres.user_password)
                    print("PLEASE PICK AN OPTION THAT REPRESENT AN ACTION")
                    print("(A)=> DELETE ACCOUNT \n (B)=> EXIT PROCES")
                else:
                    print("ACCOUNT " + searchdet +" DOESNT EXIST")
                options2 = input("selecetion ?")
                if(options2.upper() == "A"):
                    print("SELCTION => DELETE ACCOUNT")
                    print("ENTER ACCOUNT TO DELETE")
                    account_del = input("account ?")
                    if(delete_account(search_accountname(account_del))):
                         print("ACCOUNT " + account_del.upper() + "DELETED SUCCESSFULLY")
                         logout()
                    else:
                        print("ACCOUNT " + account_del.upper() + "DOES NOT EXIST")
                        logout()
            elif(options1.upper() == "B"):
                pass
            elif(options1.upper() == "C"):
                pass
            else:
                print("UN-RECOGNISED ACCTION")
        elif(options.upper() == "B"):
            print("SELECTION => SEARCH ACCOUNT")
            print("ENTER USERNAME OR ACCOUNT NAME")
            searchdet = input("search ?")
            accountres = search_account(searchdet)
            if(accountres):
                print("Account:__" + accountres.account_name)
                print("UserName:__"+ accountres.user_name)
                print("Password:__" + accountres.user_password)
            else:
                print("NO ACCOUNT SAVED")
        elif(options.upper() == "C"):
            print("SELCTION => DELETE ACCOUNT")
            print("ENTER ACCOUNT TO DELETE")
            account_del = input("account ?")
            if(delete_account(search_accountname(account_del))):
                    print("ACCOUNT " + account_del.upper() + "DELETED SUCCESSFULLY")
                    logout()
            else:
                print("ACCOUNT " + account_del.upper() + "DOES NOT EXIST")
                logout()
        elif(options.upper() == "D"):
            print("SELECTED => EXIT")
            print("THANK YOU FOR USING THIS APP...")
            logout()
        else:
            print("UN-RECOGNISED ACCTION")
    else:
        print("UNRECOGNISED SELECTION")
if __name__ == '__main__':
    main()