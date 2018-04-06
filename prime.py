n=int(input("enter any number"))
sum=0
for i in range(2,n+1):
    fact=0
    for j in range(2,int(i**0.5)+1):
        if(i%j==0):
            fact+=1
            break
    if(fact==0):
        sum=sum+i
print("sum=",sum)    
 
