"""
Python project to find the smallest of 3 numbers
Auther : Febin Noble
Date : 15-10-2024
Version 1.0
"""
num1=int(input("Enter num1 : "))
num2=int(input("Enter num2 : "))
num3=int(input("Enter num3 : "))
if num1<num2 and num1<num3:
    print(f"{num1} is the smallest")
elif num2<num1 and num2<num3:
    print(f"{num2} is the smallest")
else:
    print(f"{num3} is the smallest")