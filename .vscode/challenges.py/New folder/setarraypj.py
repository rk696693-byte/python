snack1 = {"chips", "juice", "cake"}
snack2 = {"juice", "cake", "biscuits"}
snack1.add("chocolate")
print(snack1.intersection(snack2))


import array
snacks = array("i",[10,20,30])
snacks.insert(1,15)
snacks.append(40)
print("count",snacks.count(20))
print(snacks)