"""
Project: user name function
Author: Devam A

Description: if user gives no input (i.e, press enter without typing anything) then error is raised.
"""
user_name = input("Enter your name:")
user_name_boolean = bool(user_name)


def user_name_function():
    if user_name_boolean == True:
        print(f"Hello,{user_name.title()}")
    else:
        raise ValueError("Invalid User Name!! Please Enter A Valid Name:")

user_name_function()