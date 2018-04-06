import math
class square:
    def area1(self,x):
        print('square  area of x',x*x)
class circle(square):
    def area(self,x):
        print("area of circle",(math.pi*x*x))
c=circle()
c.area(9)
c.area1(7)
s=square()
s.area1(8)
