import random
import math
print("WELCOME TO FUN CALCULATOR")
print("Here computer will choose the number you need to guess it and need to do fun activities.")
computer_choice=random.randint(0,10)
while True:
    try:
        n=int(input("enter the value"))
        if n==computer_choice:
            print("Congratulations, you guessed the correct number")
            break 
        else:
            print("you guessed it wrong, try again.")
    except:
        print("there is an error")
print("Random fun activities to do now")
print("studing," "playing,","watching a movie,", "reading,")
print("select any activity from this to do now")
a=1.2
b=3.4
print(math.ceil(b))
print(math.fabs(a))

