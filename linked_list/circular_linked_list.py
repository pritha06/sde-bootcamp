class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    
class CircularLL:
    def __init__(self):
        self.head=None
        self.tail=None
    
    def display(self):
        if self.head is None:
            print("Empty list")
        else:
            temp=self.head
            print(temp.data)
            while temp.next!=self.head:
                temp=temp.next
                print(temp.data)

CLL=CircularLL()
n1=Node(10)
CLL.head=n1
CLL.tail=n1
CLL.tail.next=CLL.head
print("Adding first node")
CLL.display()
n2=Node(20)
CLL.tail.next=n2
CLL.tail=n2
CLL.tail.next=CLL.head
print("Adding second node")
CLL.display()
n3=Node(30)
CLL.tail.next=n3
CLL.tail=n3
CLL.tail.next=CLL.head
print("Adding third node")
CLL.display()