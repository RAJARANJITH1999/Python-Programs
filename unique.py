def unique(l):
    u=[]
    for i in l:
        count=0
        for j in l:
            if(i==j):
                count=count+1
        if(count==1):
            u.append(i)
    print("***the unique numbers in the list are***")
    print((u))
l=[]
while True:
    n=input("enter the list data and q for quit ")
    if(n.isdigit()):
        l.append(int(n))
    else:
        break
unique(l)
