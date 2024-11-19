"""
Python program to separate even numbers from odd numbers
Auther:Febin Noble
Version:1.0
Date: 19-11-2004
"""



elements_list1=int(input("Enter the number of elements in list1 :"))
list1=[]
list2=[]
print("Enter the elements of list1")
for i in range (elements_list1):
    list1.append(int(input()))
elements_list2=int(input("Enter the number of elements in list2 :"))
for j in range(elements_list2):
    list2.append(int(input()))
print("The elements in list1 are",list1)
print("The elements in list2 are",list2)
list3=list1+list2
print(f"The elements in list3 are:{list3}")
even_list=[]
odd_list=[]
for k in list3:
    if k%2==0:
        even_list.append(k)
    else:
          odd_list.append(k)
print(f"The list of even numbers are {even_list}")
print(f"The list of odd numbers are {odd_list}")
merged_list=even_list+odd_list
print(merged_list)






