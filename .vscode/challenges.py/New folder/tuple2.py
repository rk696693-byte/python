weather=(1,0,1,0,1,0,1,1,1,1,0,0,0,1,0)
count1=0
count0=0
for i in range(0,len(weather)):
    if weather[i]==1:
        count1=count1+1
    else:
        count0=count0+1
print("the number of ones in tuples is", count1)
print("the number of zeros in tuples is", count0)
if count1>count0:
    print("everyday")
else:
    print("sunnyday")
    
    