def enqueue():
    n=input("Enter the element you want to insert in queue")
    queue.append(n)
    

def dequeue():
    if len(queue)==0:
        print("Queue is empty")
    else:
        del queue[0]

def display():
    if len(queue)==0:
        print("queue is empty")
    else:
        print("Displaying the elements of the queue")
        for ele in queue:
            print(ele,end=" ")
        print("\nFront of the queue is: ",queue[0])
        print("\nRear of the queue is: ",queue[-1])




queue=list()
while(1):
    print("\n Enter the option: \n 1-Enqueue Operation \n 2-Dequeue Operation \n 3-Display \n 4-Enter any key to break the loop")
    user_option=int(input())
    if user_option==1:
        print("Enqueue operation")
        enqueue()
    elif user_option==2:
        print("Dequeue Operation")
        dequeue()
    elif user_option==3:
        print("Display Operation")
        display()
    else:
        print("EXIT From the loop")
        break