class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Stack:
    def __init__(self):
        self.top=None

    def push(self):
        n=input("Enter the element you want to insert in stack")
        new=Node(n)
        if self.top is None:
            self.top=new
            self.top.next=None
        else:
            new.next=self.top
            self.top=new

    def pop(self):
        if self.top is None:
            print("Stack is empty")
        elif self.top.next is None:
            print("Popped element is: ",self.top.data)
            self.top=None
        else:
            temp=self.top
            print("Popped element is: ",self.top.data)
            self.top=temp.next
            temp=None

    def display(self):
        if self.top is None:
            print("Stack is empty")
        else:
            print("Displaying the elements of the stack")
            temp=self.top
            while temp:
                print(temp.data,"-->",end=" ")
                temp=temp.next




s=Stack()
while(1):
    print("\n Enter the option: \n 1-Push Operation \n 2-Pop Operation \n 3-Display \n 4-Enter any key to break the loop")
    user_option=input()
    if user_option=='1':
        print("Push operation")
        s.push()
    elif user_option=='2':
        print("Pop Operation")
        s.pop()
    elif user_option=='3':
        print("Display Operation")
        s.display()
    else:
        print("EXIT From the loop")
        break