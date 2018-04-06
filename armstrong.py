n=int(input("enter the number to check armstrong or not"))
sum1=0
temp=n
while(n>0):
    digit=n%10
    sum1=sum1+(digit**3)
    n=n//10
if(temp==sum1):
    print("given number is an armstrong")
else:
    print("given number is not a armstrong")
    
