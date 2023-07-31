'''two nodes n1 and n2
n1 has prev=None data next=pointing to n2
n2 has prev=pointing to n1 data next=None(or pointing to next node)
n2.prev=n1
n1.next=n2

'''


class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None

class DoublyLinkedList:
    def __init__(self):
        self.head=None

    def len_list(self):
        temp=self.head
        length=0
        while temp:
            length+=1
            temp=temp.next
        # print(length)
        return length

    #Inserting Items to Empty List
    def insert_at_beginning(self,newNode):
        if self.head is None:
            self.head=newNode
        else:
            n=newNode
            temp=self.head
            temp.prev=n
            n.next=temp
            self.head=n
    
    def insert_at_end(self,newNode):
        if self.head is None:
            self.head=newNode
            return
        n=newNode
        curr=self.head
        while curr.next is not None:
            curr=curr.next
        curr.next=n
        n.prev=curr
    
    def insert_at_position(self,newNode,pos):
        if pos<0 or pos>self.len_list():
            print("Invalid position")
            return
        if pos==0:
            self.insert_at_beginning(newNode)
            return
        temp=self.head
        for i in range(1,pos-1):
            temp=temp.next
        n=newNode
        n.prev=temp
        n.next=temp.next
        temp.next.prev=n
        temp.next=n

    def delete_at_beginning(self):
        if self.head is None:
            print("No data to delete, list is empty")
            return
        temp=self.head
        self.head=temp.next
        temp.next=None
        self.head.prev=None


    '''
    1. verify if the list is empty or if the list has a single element.
    2. If single element, we will assign the start node to NULL. 
    3. else traverse through the list until the last node reaches NULL.
    4. Once we reach the last node, we assign the next address of the node 
    previous to the last node, to NULL which actually deletes the last node. 
    '''
    def delete_at_end(self):
        if self.head is None:
            print("No data to delete, list is empty")
            return
        
        temp=self.head.next
        before=self.head
        while temp.next is not None:
            temp=temp.next
            before=before.next
        before.next=None
        temp.prev=None

    def delete_between_nodes(self,pos):
        if pos<0 or pos>self.len_list():
            print("Invalid position")
            return
        if pos==0:
            self.delete_at_beginning(newNode)
            return
        temp=self.head.next
        before=self.head
        for i in range(1,pos-1):
        
            temp=temp.next
            before=before.next
        before.next=temp.next
        temp.next.prev=before
        temp.next=None
        temp.prev=None

    def print_list(self):
        if self.head is None:
            print("List is empty")
            return
        else:
            curr=self.head
            while curr:
                print(curr.data,"->",end=" ")
                curr=curr.next
    

first=Node(10)
second=Node(20)
third=Node(30)
fourth=Node(40)
fifth=Node(50)
sixth=Node(60)
NewDoublyLinkedList = DoublyLinkedList()
NewDoublyLinkedList.insert_at_beginning(first)
NewDoublyLinkedList.insert_at_beginning(second)
NewDoublyLinkedList.insert_at_end(third)
NewDoublyLinkedList.insert_at_position(fourth,3)
# NewDoublyLinkedList.len_list()
# NewDoublyLinkedList.head=first
# second.prev=first
# first.next=second
# third.prev=second
# second.next=third

# print("Insert to empty list")
# NewDoublyLinkedList.delete_at_start()
print("\n List after insertion")
NewDoublyLinkedList.print_list()
NewDoublyLinkedList.delete_at_beginning()
print("\n List after deletion at start")
NewDoublyLinkedList.print_list()
print("\n List after deletion at position")
NewDoublyLinkedList.delete_between_nodes(1)
NewDoublyLinkedList.print_list()
NewDoublyLinkedList.delete_at_end()
print("\n List after deletion at end")
NewDoublyLinkedList.print_list()

# NewDoublyLinkedList.delete_at_start()
# NewDoublyLinkedList.print_list()
# NewDoublyLinkedList.insert_at_end(third)
# NewDoublyLinkedList.insert_at_end(fourth)
# NewDoublyLinkedList.insert_at_end(fifth)
# NewDoublyLinkedList.insert_at_end(sixth)
# NewDoublyLinkedList.delete_at_start()
# NewDoublyLinkedList.delete_at_end()
# NewDoublyLinkedList.print_list()

