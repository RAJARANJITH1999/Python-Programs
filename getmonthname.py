'''def getMonthName(mo):
    month={1:'Jan',2:'Feb',3:'Mar',4:'Apr',5:'May',6:'Jun',7:'Jul',8:'Aug',9:'Sep',10:'Oct',11:'Nov',12:'Dec'}
    if( 1<= mo <=12):
        print("getMonthName(",mo,")=",month[mo])
    else:
        print("invalid month")
while True:
    data=(input("enter the integer number which map to a month ,  want to exit type exit(upper or lower)"))
    if(data.isdigit()):
        getMonthName(int(data))
    elif(data.lower()=='exit'):
        break
    else:
        print("type only integer numbers")'''
import datetime
def getMonthName():
  td=5
  str1=td.strftime("%a")
  print(str1)
  print(date.today())

  
