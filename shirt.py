white=['M','L']
blue=['M','S']
available=False
print("*****search for your color shirt and size it*****")
color=input("enter your shirt color")
if(color.lower()=='white'):
  size=input("enter your size")
  if((size.upper() in white)): 
    print("available")
    available=True
  else:
    print("unavailable")
elif( color.lower()=='blue'):
  size=input("enter your size")
  if(size.upper() in blue): 
    print("available")
    available=True
  else:
    print("unavailable")
else:
  print("unvailable")
if(available==True):
  name=input("enter your name ")
  address=input("enter the addres to place order")
  mobile=int(input("enter your mobile number"))
  print("********order confirmation*******")
  print("name:",name)
  print("address:",address)
  print("mobile:",mobile)
  print("***ordered shirt***\n","color:",color,"\nsize:",size.upper())
