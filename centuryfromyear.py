def centuryFromYear(year):
    if(1 <=year<=2005):
        return(1 + (year - 1) // 100)  
print(centuryFromYear(1929))
