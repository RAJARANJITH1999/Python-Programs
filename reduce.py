import functools
def func(x,y):
     return (x+y)
num=['r','a','j','a']

sum1=(functools.reduce(func,num))
print(sum1)
