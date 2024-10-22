"""
Python program convert temperature in one unit into another
Auther : Febin Noble
Version : 1.0
Date : 22-10-2024
"""
temperature=float(input("Enter the temperature : "))
unit=input("Is this in Celcious ,C or Farenheit , F:")
if unit=='C':
    f=((9/5)*temperature)+32
    print(f"The temperature in farenheit is {f}")
else:
    c=(5/9)*(temperature-32)
    print(f"The temperature in celcious is {c}")