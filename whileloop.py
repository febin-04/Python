"""
 Python program to generate n odd numbers
 Auther : Febin Noble
 Date; 15-20-24
 Version : 1.0

"""
limit = int(input("Enter the limit:"))
odd_number=1
count=0
while count<limit:
    print(odd_number ,"\t" ,  end="" )
    count+=1
    odd_number+=2
