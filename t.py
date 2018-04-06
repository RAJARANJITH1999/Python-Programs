import sys
f=open("prime.py",'r')
text=f.read()
n=input("enter the character to search")
c=0
for line in text:
    if(line==n):
        c+=1
print("the character",n,"present in",c,"times")
f.close()
 
