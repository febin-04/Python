"""
Python project to find the fare of people visiting the park
Auther : Febin Noble
Date : 15-10-2024
Version 1.0
"""
age=float(input("Enter your age : "))
if age <10:
    print("Your ticket fare is $7")
elif age>=10 and age<60:
    print("Your ticket  fare is $10")
else:
    print("Your ticket fare is $5")