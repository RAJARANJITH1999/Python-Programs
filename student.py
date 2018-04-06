m1,m2,m3,m4=[int(x) for x in input("enter the m1,m2,m3,m4 marks out of 50").split()]
total=m1+m2+m3+m4
agg=(total/200)*100
print("------student details------")
print("total =",total)
print("aggregate =",agg)
if(agg>=75):
    print("Grade = Distinction")
elif(agg>=60 and agg<75):
    print("Grade =1st Division")
elif(agg>=50 and agg<65):
    print("Grade = 2nd Division")
elif(agg>=40 and agg<50):
    print("Grade = 3rd Division")
else:
    print("Grade = fail")
print("----------------------------")
 
