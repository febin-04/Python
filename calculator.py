'''
Auther : Febin Noble

'''
operator = input("Enter an operator (+ - * /) :")
num1 = float(input("Enter the 1st number :"))
num2 =float(input("Enter the 2nd number :"))
if operator == "+":
    result1 = num1 + num2
    print(round(result1 , 3))
elif operator == "-":
    result2 = num1 - num2
    print(round(result2 , 3))
elif operator == "*":
    result3 = num1 * num2
    print(round(result3 , 3))
elif operator =="/":
    result4  = num1 / num2
    print(round(result4 , 3))
else :
    print(f"The {operator} is not a valid operator")
