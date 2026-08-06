n=int(input("enter your value"))
for i in range(1,n+1):
    for j in range(0,i):
        print("*",end=" ")
    print()
n=int(input("enter your value"))
for i in range(0,n+1):
    for j in range(n-i):
        print("*",end=" ")
    print()