year=int(input("enter the year to check leap year or not"))
if(year%400==0 and year%100==0 or year%4==0):
    print("given",year,"is a leap year")
else:
    print("given",year,"is not a leap year")
print("leap year checking compeleted successfully")
