a={1,2,3,4,5,8,9,0}
b={1,3,2,4}
print('a=',a,end=' \n')
print('b=',b) 
print('0 in a:',0 in a)
print('a union b:',a.union(b))
print('a intersection b',a.intersection(b))
print('this also union:',a|b)
print('a is superset of b:',a.issuperset(b))
print('a is subset of b:',a.issubset(b))
