"""
Python program to explain while looop

"""

food=input("Enter your favourite food(q to quit):")
while not food=='q':
    print(f"You like  {food}")
    food=input("Enter another food you like :")
print("Bye")