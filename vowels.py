"""
Auther: Febin
Date: 29-10-2024
Python program to find all the vowels in a string
Version 1.0
"""

string=input("Enter your string : ")
vowels="aeiouAEIOU"
vowels_count=0
for char in string:
    if char in vowels:
        print(char)
        vowels_count+=1
print(f"No. of vowels in string is : {vowels_count}")