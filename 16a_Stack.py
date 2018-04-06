class Stack:
    def __init__(self):
        self.st = []

    def isempty(self):
        return self.st == []
 
    def push(self,element):
        self.st.append(element)

    def pop(self):
        if self.isempty():
            return -1
        else:
            return self.st.pop()

    def peep(self):
        n = len(self.st)
        if n == 0:
            return -1
        else:
            return self.st[n-1]

    def search(self,element):
        if self.isempty():
            return -1
        else:
            try:
                n = self.st.index(element)
                return len(self.st)-n
            except ValueError:
                return -2

    def display(self):
        return self.st

def main():
    s = Stack()
    choice = 0
    while choice < 5:
        print('STACK OPERATIONS')
        print('1. Push Element')
        print('2. Pop Element')
        print('3. Peep Element')
        print('4. Search Element')
        print('5. Exit')
        choice = int(input('Enter Your Choice: '))
        if choice == 1:
            element = int(input('Enter element: '))
            s.push(element)
        elif choice == 2:
            element = s.pop()
            if element == -1:
                print("The Stack is Empty...")
            else:
                print("Popped Element= ",element)
        elif choice == 3:
            element = s.peep()
            if element == -1:
                print("The Stack is Empty...")
            else:
                print("Top Most Element = ",element)
        elif choice == 4:
            element = int(input("Enter element: "))
            pos = s.search(element)
            if pos == -1:
                print("The Stack is Empty...")
            elif pos == -2:
                print("Element not found in the stack")
            else:
                print("Element found at position: ",pos)
        else:
            break
    print("Stack = ", s.display())

if __name__ == "__main__":
    main()
