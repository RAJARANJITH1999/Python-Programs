num=(input("enter the values"))
lis=list(num.split(','))
count=0
print(lis)
for i in lis:
    if(i=='5'):
        count+=1
        continue
    else:
        print(i)
print("the number t is present in the list are",count)
