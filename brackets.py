data=input("enter the sentence ")
count=0
lis=[]
try:
    for i in data:
        if(i=='('):
            count+=1
            lis.append(i)
        elif(i==')'):
            count-=1
            lis.pop()
    if(count==0):
        print("brackets are matched")
    else:
        print("brakects are not matched")
except("IndexError"):
    print("not matched")


