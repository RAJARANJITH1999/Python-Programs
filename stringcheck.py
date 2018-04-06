def str_analysis(n):
    if(n.isdigit()):
        if(int(n)>99):
            print(n," is a pretty big number")
        else:
            print(n,"is a smaller number than expected")
    elif(n.isalpha()):
        print(n," is all alphabetical characters!")
    else:
        print("entered message  neither alpha not digit")
while True:
    n=input("enter word or integer:")
    if(n.isdigit() or n.isalpha):
        str_analysis(n)
        break
