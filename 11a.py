# Program to define a matrix and prints
X = [[12,7,3],
[4 ,5,6],
[7 ,8,9]]
# iterate through rows
for i in range(len(X)):
    # iterate through columns
    for j in range(len(X[0])):
        print(X[i][j],end='\t')
    print()
