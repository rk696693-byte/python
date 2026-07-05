#title=nested condition
age=int(input("enter your age"))
if age>18:
    if age<20:
        print("age is between 18 and 20 years")
        else:
            print("age is greater than 20")
else:
    print("age is below 10")