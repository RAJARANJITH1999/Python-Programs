even=0
n=[]
odd=0
counte=0
counto=0
while((int(input("enter the value"))!=-1):
      
      if(n%2==0):
          even+=n
          counte+=1
      elif(n%2==1):
           odd+=n
           counto+=1
print("the sum of even number are:",even)
print("the sum of odd number are:",odd)
print("the avg of even sum:",even/counte)
print("the avg of odd sum:",odd/counto)
print("the total sum is:",sum(even,odd))
print("the avg of total sum:",sum(even,odd)/sum(counte+counto))
print("total numbers you entered is:",(counto+counte))
