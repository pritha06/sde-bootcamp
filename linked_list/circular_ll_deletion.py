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
            print(temp.data,"-->",end=" ")
            while temp.next!=self.head:
                temp=temp.next
                print(temp.data,"-->",end=" ")
            print(temp.next.data) #to check if tail points to head or not
    
    def len_list(self):
        
        if self.head is None:
            # print("List is empty")
            return 0
        else:
            length=1
            temp=self.head
            while temp.next!=self.head:
                length+=1
                temp=temp.next
            # print(length)
            return length

    
    def delete_at_beginning(self):
        if self.head is None:
            print("Empty list")
        else:
            if self.head==self.tail:
                self.head=None
            else:
                temp=self.head
                self.head=temp.next
                self.tail.next=self.head
                temp=None
    
    def delete_at_end(self):
        if self.head is None:
            print("Empty list")
        else:
            if self.head==self.tail:
                self.head=None
            else:
                temp=self.head
                while (temp.next!=self.tail):
                    temp=temp.next
                self.tail=None
                self.tail=temp
                temp.next=self.head
    
    def delete_between_nodes(self,pos):
        if pos<=0 or pos>self.len_list():
            print("Invalid position!!")
            return
        if pos==1:
            self.delete_at_beginning()
        else:
            temp1=self.head
            temp2=self.head.next
            for i in range(1,pos-1):
                temp1=temp1.next
                temp2=temp2.next
            temp1.next=temp2.next
            
            #check for last element
            if temp2.next==self.tail:
                self.tail=temp1
            temp2=None

    
CLL=CircularLL()
n1=Node(10)
CLL.head=n1
CLL.tail=n1
CLL.tail.next=CLL.head
# print("Adding first node")
# CLL.display()
# print("deleting first node")
# CLL.delete_at_beginning()
# CLL.display() #there should be no node
n2=Node(20)
CLL.tail.next=n2
CLL.tail=n2
CLL.tail.next=CLL.head
# print("Adding second node")
# CLL.display()
n3=Node(30)
CLL.tail.next=n3
CLL.tail=n3
CLL.tail.next=CLL.head
# print("Adding third node")
# CLL.display()
n4=Node(40)
CLL.tail.next=n4
CLL.tail=n4
CLL.tail.next=CLL.head
# print("Adding fourth node")
CLL.display()
# print("deleting last node")
# CLL.delete_at_end()
# CLL.display() #there should be 3 nodes
# print("deleting between node")
# CLL.delete_between_nodes(2)
# CLL.display() #there should be 3 nodes