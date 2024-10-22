"""
Python program calculate the greatest of 3 numbers
Auther : Febin Noble
Version : 1.0
Date : 22-10-2024
"""
num1=int(input("Enter number1 : "))
num2=int(input("Enter number2 : "))
num3=int(input("Enter number3 : "))
if num1>num2:
    largest=num1
else:
    largest =num2
if largest>num3:
    print(f"The larger number is : {largest}")
else :
    print(f'The larger number is : {num3}')
