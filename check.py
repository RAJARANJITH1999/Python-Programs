def str_analysis(n):
  if(n.isdigit()):
    if(int(n)<99):
       print(n,'is a smaller number than expected')
       print(n,'is a small number ')
    elif(int(n)>99):
      print(n,'is a pretty big number')
      print(n,'is abig number')
  elif(n.isalpha()):
      print(n,'is all alphabetical characters!')
      print(n,'is being all alpha')
  else:
    print(n,'is a multiple characters!')
    print(n,'is neither all alpha nor all digit')
  
while True:
  n=input('enter word or integer: ')
  if(n!=''):
    str_analysis(n)
    break

