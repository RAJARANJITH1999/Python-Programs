import matplotlib.pyplot as plt
import pandas as pd
import xlrd
import quandl
file='F:\Mileage.csv'
var=pd.ExcelFile(file)
print(var.sheet_names)
plt.plot(var.sheet_names)
plt.show()
