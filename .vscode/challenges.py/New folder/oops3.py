class Parrot:
    age=12
    def __init__(self,color,food):
        self.color=color
        self.food=food
        
ob1=Parrot("red","chocolate")
ob2=Parrot("green","icecream")
print(f"the color of {ob1.color},the food of{ob2.food},the age of te parrot is {ob1.age}")