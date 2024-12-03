def add_numbers(n1,n2):

    if n2==0:
        return n1
    else:
        return add_numbers(n1+1,n2-1)
n1=int(input("Enter num1:"))
n2=int(input("Enter num2: "))
print(add_numbers(n1,n2))
