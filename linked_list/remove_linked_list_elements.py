'''Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.
Input: head = [1,2,6,3,4,5,6], val = 6
Output: [1,2,3,4,5]
'''

from singly_linkedlist import LinkedList,Node

def removeElements(dummy,LL,val):
    #make a dummy node which will forever pt to head of list
    
    prev=dummy
    curr=LL.head
    while curr:
        
        nxt=curr.next
        if curr.data==val:
            prev.next=nxt
        else:
            prev=curr
        curr=nxt
    



n1=Node(10)
n2=Node(20)
n3=Node(30)
n4=Node(40)
n5=Node(50)
n6=Node(60)
LL=LinkedList()
LL.insert_at_end(n1)
LL.insert_at_end(n2)
LL.insert_at_end(n3)
LL.insert_at_end(n4)
LL.insert_at_end(n5)
LL.insert_at_end(n6)
print("\nLL before")
LL.print_list()
val=40
dummy=Node(60)
dummy.next=LL.head
removeElements(dummy,LL,val)
print("\nLL after")
LL.print_list()
