dict={"stduent":{"maths":45,"science":50},"toppers":{"uday":95,"murthy":100}}
for i,j in dict.items():
    print("the",i,"marks are")
    for key,values in j.items():
        print(key,":",values)
        
