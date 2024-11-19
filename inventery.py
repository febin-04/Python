""""
Python program to manage the inventory of a shop
Auther:Febin Noble
Date:19-11-2004
Version:1.0
"""
largest=0

inventory=[
    ("laptop",50000,50),
    ("headphone",500,10),
    ("speaker",1000,10),
    ("monitor",10000,30)

]
for item in inventory:
    item_name,quantity,price=item
    stock_value=quantity*price
    print("Item_name :",item_name,", stock_value :",stock_value)
    if stock_value>=largest:
        largest=stock_value
print(largest)
