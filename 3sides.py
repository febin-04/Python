"""
Auther:Febin Noble
Date: 30-11-2024
Python program to check whether a given sides are aprt of the right triangle
Version:1.0
"""
def right_trinagle(side1,side2,side3):
    sides=[side1,side2,side3]
    sides.sort()
    if sides[2]**2 == sides[0]**2 + sides[1]**2:
        return True
    return False
side1=int(input("Enter side1 :"))
side2=int(input("Enter side2 :"))
side3=int(input("Enter side3 :"))
if right_trinagle(side1,side2,side3):
    print("The given sides are part of a right triangle")
else:
    print("The given sides are not part of a right triangle")