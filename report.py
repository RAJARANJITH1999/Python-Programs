def adding_report(n="T"):
    items=[]
    total=0
    print('Input an integer to add to the total or "Q" to quit')
    while True:
            num=(input('Enter an integer or "Q":'))
            if(num.isdigit()):
                items.append(int(num))
            elif(num.isalpha() and num!='q'):
                print("invalid data ",num)
            elif(num=='q'):
                total=sum(items)
                break
    if(n.upper()=='A'):
        print("Items")
        for i in items:
            print(i)
    print('total\n',total)
adding_report(n="A")
