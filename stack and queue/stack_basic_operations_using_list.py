def push():
    n=input("Enter the element you want to insert in stack")
    if len(stack)==0:
        stack.append(n)
    else:
        stack.insert(0,n)

def pop():
    if len(stack)==0:
        print("Stack is empty")
    else:
        del stack[0]

def display():
    if len(stack)==0:
        print("Stack is empty")
    else:
        print("Displaying the elements of the stack")
        for ele in stack:
            print(ele,end=" ")




stack=list()
while(1):
    print("\n Enter the option: \n 1-Push Operation \n 2-Pop Operation \n 3-Display \n 4-Enter any key to break the loop")
    user_option=input()
    if user_option=='1':
        print("Push operation")
        push()
    elif user_option=='2':
        print("Pop Operation")
        pop()
    elif user_option=='3':
        print("Display Operation")
        display()
    else:
        print("EXIT From the loop")
        break