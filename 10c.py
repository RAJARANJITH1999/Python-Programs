gcd = lambda x,y: x if y == 0 else gcd(y,x%y)
lcm = lambda a,b: (a*b)/gcd(a,b)

print(gcd(40,20))
print(lcm(40,20))
