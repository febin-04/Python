limit=int(input("Enter the number of rows :"))
for i in range(limit):
    for j in range(limit-(i)):
        print("*",end=" ")
    print()