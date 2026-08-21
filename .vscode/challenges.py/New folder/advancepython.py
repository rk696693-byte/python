list1=[1,"sara",2,3,4,5]
print(list1)
list2=[i for i in list1 if i !=3]
print(list2)

items=["pencil","eraser","notebook","pens"]
stock=[1,2,3,4]
inventory=list(zip(items,stock))
print(inventory)
name=list(map(lambda p:p+5,stock))
print(name)
