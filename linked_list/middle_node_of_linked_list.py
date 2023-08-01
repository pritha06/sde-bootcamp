from singly_linkedlist import LinkedList,Node

def middle_node(LL):
    slow=LL.head
    fast=LL.head
    #to check it's not last node still
    while fast and fast.next is not None:
        fast=fast.next.next
        slow=slow.next
    return slow

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
middle=middle_node(LL)
print("\n middle node is: ",middle.data)
