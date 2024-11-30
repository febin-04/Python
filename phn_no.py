"""
Auther:Febin Noble
Date: 30-11-2024
Python program to check whether a phone number is valid or not
Version:1.0
"""
def phone_number (phn_no):
    length=len(phn_no)
    if length==10 and phn_no[0] in "789":
        print("The phone number is valid")
    else:
        print("The phone number is not valid")
phn_no=input("Enter the phone number :")
phone_number(phn_no)


