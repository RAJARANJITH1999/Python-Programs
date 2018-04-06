n=int(input("enter the binary number (1's and 0's)"))
base=1
decimal=0
binary=n
while(n>0):
    rem=n%10
    decimal=decimal+rem*base
    n=n//10
    base=base*2
n1=int(input("enter the decimal number to convert into binary"))
base2=1
bi=0
dec=n1
while(n1>0):
    rem1=n1%2
    bi=bi+rem1*base2
    n1=n1//2
    base2=base2*10
print(" binary number =",binary)
print("decimal number =",decimal)
print("decimal number =",dec)
print("binary number =",bi)
