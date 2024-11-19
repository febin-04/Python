limit=int(input("Enter the number of rows:"))
for i in range (1,limit+1):
    for j in range(limit-i):
        print(" ",end="")
    for k in range(1,i*2):
        print("*",end="")
    print()




