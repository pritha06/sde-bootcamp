from singly_linkedlist import Node,LinkedList

'''Delete duplicate value nodes from a sorted linked list'''
def delete_duplicate_nodes(LL):
    temp=LL.head
    while temp.next is not None:
        if temp.data==temp.next.data:
            #delete the node
            temp.next=temp.next.next
        else:
            temp=temp.next
    return LL.head

n1=Node(10)
n2=Node(10)
n3=Node(20)
n4=Node(30)
n5=Node(40)
n6=Node(40)
LL=LinkedList()
LL.insert_at_end(n1)
LL.insert_at_end(n2)
LL.insert_at_end(n3)
LL.insert_at_end(n4)
LL.insert_at_end(n5)
LL.insert_at_end(n6)
print("\n LL before")
LL.print_list()
delete_duplicate_nodes(LL)
print("\n LL after")
LL.print_list()
