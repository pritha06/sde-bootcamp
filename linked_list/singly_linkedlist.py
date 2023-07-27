#create nodes
#create linked list
#add nodes to linked list
#print LL
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
    
    def is_list_empty(self):
        if self.head is None:
            return True
        else:
            return False

    def len_list(self):
        currentNode=self.head #set currentnode as first node
        length=0
        while currentNode is not None: #keep checking until data exist on node
            length+=1
            currentNode=currentNode.next #set currentnode as next node
        return length
    
    def insert_at_beginning(self,newNode):
        #newnode will have data as Ms., and next as None
        #find a temp node which pts to current head, set the current head to new node
        #set current head's next to tempnode
        #delete temp node
        tempNode=self.head #Pritha
        self.head=newNode #Ms.
        self.head.next=tempNode
        del tempNode
    
    def insert_at_end(self,newNode):
        #check where it needs to be inserted
        #if head is empty, we make new node as head node
        if self.head is None:
            self.head=newNode
        #traverse to end of list if head is not empty
        #check lastnode's next should be ppointing to none
        #start from self.head(first node)
        else:
            lastNode=self.head
            #advance through all elements until we find last node
            while True:
                if lastNode.next is None:
                    break
                lastNode=lastNode.next
            #when last node is reached we break the connection and assign next of last node pointing to new node.
            lastNode.next=newNode
 
    def insert_at_position(self,newNode,position):
        if position<0 or position>self.len_list():
            print("Invalid position")
            return
        if position==0:
            self.insert_at_beginning(newNode)
            return
        currentPos=0
        currentNode=self.head
        while True:
            if currentPos==position:
                prevnode.next=newNode
                newNode.next=currentNode
                break
            prevnode=currentNode
            currentNode=currentNode.next
            currentPos+=1
        
    def delete_at_beginning(self):
        if self.is_list_empty() is False:
            prevhead=self.head
            self.head=self.head.next
            prevhead.next=None
        else:
            print("Linked list is empty...Delete failed")

    def delete_between_nodes(self,position):
        if position<0 or position>=self.len_list(): #>= because length might be 3 but position given will only be till 2
            print("Invalid position")
            return
        if self.is_list_empty() is False:
            if position==0:
                self.delete_at_beginning()
                return
            currentPos=0
            currentNode=self.head
            while True:
                if currentPos==position:
                    prevNode.next=currentNode.next
                    currentNode.next=None
                    break
                prevNode=currentNode
                currentNode=currentNode.next
                currentPos+=1

    def delete_at_end(self):
        lastNode=self.head
        while lastNode.next is not None:
            prevNode=lastNode
            lastNode=lastNode.next
        prevNode.next=None
        del lastNode
    
    def print_list(self):
        if self.head is None:
            print("List is empty")
            return
        currentNode=self.head
        #current node starts from head node, until it is none keep printing data and iterating it to point to next until next is none
        while True:
            if currentNode is None:
                break
            print(currentNode.data)
            currentNode=currentNode.next

first=Node("Pritha")
ll=LinkedList()
# ll.print_list()
ll.insert_at_end(first)
# ll.print_list()
second=Node("Shrivastava")
ll.insert_at_end(second)
# ll.print_list()
third=Node("Ms.")
ll.insert_at_beginning(third)
# ll.delete_at_end()
ll.delete_between_nodes(0)
# fourth=Node("10")
# ll.insert_at_position(fourth,0)
# fifth=Node("20")
# ll.insert_at_position(fifth,1)
# sixth=Node("15")
# ll.insert_at_position(sixth,1)
ll.print_list()
