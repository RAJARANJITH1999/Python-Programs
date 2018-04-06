
alpha=['a','b','c','d','e','f','g','h','j','i','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
message=input("eneter the message")
key=3
ceaser=" "
chiper=" "
for i in message:
        if(i!=' '):
           ceaser+=alpha[(alpha.index(i)+key)%len(alpha)]
           #key+=1
        else:
           ceaser+=i
           #key+=1
for i in ceaser:
        if(i!=' '):
           chiper+=alpha[(alpha.index(i)-key)%len(alpha)]
           #key+=1
        else:
           chiper+=i
           #key+=1
print(ceaser)
print(chiper)


