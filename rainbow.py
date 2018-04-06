rainbow=['red','green','blue','yellow','voilet','orange','indigo']
chances=4
while True:
  answer=input("enter the correct color in rainbow ")
  chances-=1
  if(chances>0):
    if(answer in rainbow):
      print("the answer is correct")
      break
    else:
      print("answer is incorrect still there are",chances,'chances')
  else:
    print("game over buddy ")
    break
print("chance left:",chances)
