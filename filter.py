import functools
characters=[1,2,3,4]
def vowel(x,y):
    vow=[1,2]
    if x in vow:
        return x+y
    
filterlist=list(functools.reduce(vowel,characters))
print(filterlist)
