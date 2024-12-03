def product_of_two_numbers(n1,n2):
    if n2==1:
        return n1
    else:
        return n1 + product_of_two_numbers(n1,n2-1)
n1=int(input("Enter num1:"))
n2=int(input("Enter num2: "))
print(product_of_two_numbers(n1,n2))