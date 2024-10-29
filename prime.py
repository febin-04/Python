"""
Auther: Febin
Date: 29-10-2024
Python program to find the prime numbers under a limit
Version 1.0
"""
limit=int(input("Enter your limit : "))
for number in range(2,limit+1):
    isprime=True
    for i in range(2,(number//2)+1):
        if number%i==0:
            isprime=False
    if isprime:
         print(number)