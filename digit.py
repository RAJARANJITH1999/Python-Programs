n=int(input("enter the number to calculate the sum"))
sum1=0
while(n>0):
    rem=n%10
    sum1=sum1+rem
    n=n//10
print(sum1)   
