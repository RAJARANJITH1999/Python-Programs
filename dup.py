def dup(l):
    dup=set()
    for i in l:
        count=0
        for j in l:
            if(i==j):
                count=count+1
        if(count>1):
            dup.add(i)
    print("***the duplicate number in a list are***")
    print(list(dup))
l=[]
while True:
    n=input("enter the list data and * quit")
    if(n.isdigit()or n.islower() or n.isupper()):
        l.append((n))
    elif(n=='*'):
        break
dup(l)
