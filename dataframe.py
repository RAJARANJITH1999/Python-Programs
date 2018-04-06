import matplotlib.pyplot as plt
import pandas as pd
import quandl

d={"country":['brazil','usa','china','dubai','india'],
   "capitals":['uday','washington','beging','soudi arabia','delhi'],
   'population':[12345,87654,3456,987654,96522],
   'areas':[10,14,12,17,68]}
var=pd.DataFrame(d)
var.index=[99,98,97,96,95]
print(var)
plt.scatter(var[["country"]],var[["areas"]])
print(type(var[["country"]]))
plt.show()
