
def ticket_check(section,seats):
    if(section.startswith('g')):
        if(seats<=10):
                 print("available")
        else:
                 print("unvailable")
    elif(section.startswith('f')):
        if(seats<=4):
                print("available")
        else:
                print("unavailable")
    else:
        print("unavailable")

section=input("enter the section whether the ticket is available or not")
seats=int(input("enter number of seat to check available or not"))
ticket_check(section,seats)

