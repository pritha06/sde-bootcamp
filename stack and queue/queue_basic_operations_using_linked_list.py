class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Queue:
    def __init__(self):
        self.front=None
        self.rear=None

    def enqueue(self):
        n=input("Enter the element you want to insert in queue")
        new=Node(n)
        if self.front is None:
            self.front=new
            self.rear=new
        else:
            self.rear.next=new
            self.rear=new
          
    def dequeue(self):
        if self.front is None:
            print("Queue is empty")
        elif self.front.next is None:
            print("Popped element is: ",self.front.data)
            self.front=None
        else:
            temp=self.front
            print("Popped element is: ",self.front.data)
            self.front=temp.next
            temp=None


    def display(self):
        if self.front is None:
            print("Queue is empty")
        else:
            print("Displaying the elements of the queue")
            temp=self.front
            while temp:
                print(temp.data,"-->",end=" ")
                temp=temp.next

            print("\nFront of the queue is: ",self.front.data)
            print("\nRear of the queue is: ",self.rear.data)




q=Queue()
while(1):
    print("\n Enter the option: \n 1-Enqueue Operation \n 2-Dequeue Operation \n 3-Display \n 4-Enter any key to break the loop")
    user_option=int(input())
    if user_option==1:
        print("Enqueue operation")
        q.enqueue()
    elif user_option==2:
        print("Dequeue Operation")
        q.dequeue()
    elif user_option==3:
        print("Display Operation")
        q.display()
    else:
        print("EXIT From the loop")
        break