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

        


    def add_at_beginning(self,newNode):
        new=newNode
        if self.head is None:
            self.head=new
            self.tail=new
            self.tail.next=self.head
        else:
            new.next=self.head
            self.tail.next=new
            self.head=new
    
    def add_at_end(self,newNode):
        new=newNode
        if self.head is None:
            self.head=new
            self.tail=new
            self.tail.next=self.head
        else:
            self.tail.next=new
            self.tail=new
            self.tail.next=self.head

    def add_at_position(self,newNode,pos):
        new=newNode
        if self.head is None:
            self.head=new
            self.tail=new
            self.tail.next=self.head
        else:
            if pos<=0 or pos>self.len_list():
                print("Invalid position!!")
                return
            if pos==1:
                self.add_at_beginning(newNode)
            else:
                temp=self.head
                for i in range(1,pos-1):
                    temp=temp.next
                new.next=temp.next
                temp.next=new

    def search_element(self):
        x=int(input("Element to be searched: "))
        temp=self.head
        count,flag=0,0
        while (temp!=self.tail):
            if x==temp.data:
                flag=1
                break
            temp=temp.next
            count+=1
        #check last position
        if x==temp.data:
            flag=1
        if flag==1:
            print("{} is found at position {}".format(x,count+1))
        else:
            print("not found")




CLL=CircularLL()
n1=Node(10)
# CLL.len_list()
CLL.add_at_beginning(n1)
# CLL.len_list()
n2=Node(20)
CLL.add_at_end(n2)
n3=Node(30)
CLL.add_at_position(n3,2)
CLL.display()
CLL.search_element()
# CLL.len_list()
# n1=Node(10)
# CLL.head=n1
# CLL.tail=n1
# CLL.tail.next=CLL.head
# print("Adding first node")
# CLL.display()
# n2=Node(20)
# CLL.tail.next=n2
# CLL.tail=n2
# CLL.tail.next=CLL.head
# print("Adding second node")
# CLL.display()
# n3=Node(30)
# CLL.tail.next=n3
# CLL.tail=n3
# CLL.tail.next=CLL.head
# print("Adding third node")
# CLL.display()