"""
Auther: Febin noble
Python program to check the username is in proper format
Version:1.0

"""

user_name=input("Enter your username :")
length=len(user_name)
if length>12:
    print('The username is too long ')
space=user_name.find(" ")
if space>=1:
    print("There should be no spaces")
if   not user_name.isdigit():
    print("There should be no digits")
else:
    print(f"Welcome {user_name}")

