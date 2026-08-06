print("this is wender machine")
snackprice=int(input("enter your value"))
print("the price of snackprice is",snackprice)
print("you can only put 1,2 and 5 coin in the machine")
totalinserted=0
while True:
    coins=int(input("insert the coins only 1,2 and 5"))
    if coins!=1 and coins!=2 and coins!=5:
        print("invalid choice")
        continue
    totalinserted=totalinserted+coins
    if totalinserted>snackprice:
        print("enough money inserted")
        break