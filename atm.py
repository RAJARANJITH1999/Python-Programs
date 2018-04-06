from bank import Bank,SavingsAccount

class ATM():
    SECRET_CODE = "CloseItDown"

    def __init__(self,bank):
        self._account=None
        self._bank=bank
        self._methods =  {}
        self._methods["1"]=self._getBalance
        self._methods["2"]=self._deposit
        self._methods["3"]=self._withdraw
        self._methods["4"]=self._quit

    def run(self):
        while True:
            name = input("Enter Your Name: ")
            if name == ATM.SECRET_CODE:
                break
            pin = input("Enter Your PIN: ")
            self._account = self._bank.get(pin)
            if self._account == None:
                print("Error, Unrecognized PIN")
            elif self._account.getName() != name:
                print("Error, Unrecognized Name")
                self._account=None
            else:
                self._processAccount()

    def _processAccount(self):
        while True:
            print("1. View Your Balance")
            print("2. Make a Deposit")
            print("3. Make a WithDrawl")
            print("4. Quit\n")
            number = input("Enter a Number: ")
            theMethod = self._methods.get(number,None)
            if theMethod == None:
                print("Unrecognized Number")
            else:
                theMethod()
                if self._account == None:
                    break

    def _getBalance(self):
        print("Your Balance is Rs.",self._account.getBalance())

    def _deposit(self):
        amount = float(input("Enter the amount to deposit: "))
        self._account.deposit(amount)

    def _withdraw(self):
        amount = float(input("Enter the amount to withdraw: "))
        message = self._account.withdraw(amount)
        if message:
            print(message)

    def _quit(self):
        self._bank.save()
        self._account = None
        print("Have a Nice Day....")

def main():
    bank = Bank("bank.dat")
    atm = ATM(bank)
    atm.run()

def createBank(number = 0):
    bank = Bank()
    for i in range(number):
        bank.add(SavingsAccount('Name'+str(i+1),str(1000+i),100.00))
    bank.save("bank.dat")

if __name__ == "__main__":
    createBank(5)
    main()

'''
Execution Sequence:
>>> 
====================== RESTART: F:/Python Class/atm.py ======================
Enter Your Name: Name1
Enter Your PIN: 1000
1. View Your Balance
2. Make a Deposit
3. Make a WithDrawl
4. Quit

Enter a Number: 1
Your Balance is Rs. 100.0
1. View Your Balance
2. Make a Deposit
3. Make a WithDrawl
4. Quit

Enter a Number: 2
Enter the amount to deposit: 325
1. View Your Balance
2. Make a Deposit
3. Make a WithDrawl
4. Quit

Enter a Number: 1
Your Balance is Rs. 425.0
1. View Your Balance
2. Make a Deposit
3. Make a WithDrawl
4. Quit

Enter a Number: 3
Enter the amount to withdraw: 50
1. View Your Balance
2. Make a Deposit
3. Make a WithDrawl
4. Quit

Enter a Number: 1
Your Balance is Rs. 375.0
1. View Your Balance
2. Make a Deposit
3. Make a WithDrawl
4. Quit

Enter a Number: 4
Have a Nice Day....
Enter Your Name: Name7
Enter Your PIN: 1006
Error, Unrecognized PIN
Enter Your Name: Name9
Enter Your PIN: 10009
Error, Unrecognized PIN
Enter Your Name: Name8
 Enter Your PIN: 1000
Error, Unrecognized Name
Enter Your Name: 
Enter Your PIN: 
Error, Unrecognized PIN
Enter Your Name: CloseItDown
>>> 
'''
