import sys
import os.path
'''filename=input('enter the file name read')
with open (filename)as f:
    text=f.read()
    letter=input('enbter the character to search in file')
    count=0
    for i in text:
        if(i==letter):
            count+=1
    print(letter,'appears in',count,'time in the ',filename)'''
#print(os.listdir("F:\R"))
fname=open("prime.py",'r')
while (len(fname))>0:
    print(fname[::-1])
    fname.readline()
for i in fname:
    print(i)
