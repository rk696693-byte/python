#NESTED LOOP WITH WHILE CONDITION
i=1
while i<=11:
    j=1
    while j<=10:
        print(j,end="")
        j=j+1
    print() 
    i=i+1

#NESTED LOOP WITH FOR CONDITION
for i in range(1,11):
    print(i,end="")
    for j in range(1,11):
        print(j,end="")
    print()