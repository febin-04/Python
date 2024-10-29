""""
Auther: Febin
Date: 29-10-2024
Python program to check if a number is prime or not
Version 1.0
"""
prime="is prime"
num=int(input("Enter your number : "))
for j in range(2,num//2+1):
   if num%j==0:
        prime="is not prime"
print(f"{num} {prime}")



