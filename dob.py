lis={}
while True:
    s=input('enter date of birth in the format(d-m-y)')
    if(s!=''):
        l=s.split(' ')
        print('-'.join(l))
        l1=['day','month','year']
        lis.update(zip(l,l1))
    else:
        break
print(lis)
