def cum(l):
    cum=[]
    prod=1
    for i in l:
        prod=i*prod
        cum.append(prod)
    print(cum)
l=[1,2,3]
cum(l)
