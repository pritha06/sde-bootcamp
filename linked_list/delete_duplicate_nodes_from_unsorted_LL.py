from singly_linkedlist import Node,LinkedList

'''Delete duplicate value nodes from a sorted linked list'''
def delete_unsorted_duplicate_nodes(LL):
    curr=LL.head
    prev=None
    dict_values=dict()
    while curr is not None:
        if curr.data in dict_values:
            prev.next=curr.next
            #delete the node
            curr=None
        else:
            dict_values[curr.data]=1
            prev=curr
        curr=prev.next
    

n1=Node(1)
n2=Node(6)
n3=Node(1)
n4=Node(4)
n5=Node(2)
n6=Node(2)
n7=Node(4)
LL=LinkedList()
LL.insert_at_end(n1)
LL.insert_at_end(n2)
LL.insert_at_end(n3)
LL.insert_at_end(n4)
LL.insert_at_end(n5)
LL.insert_at_end(n6)
LL.insert_at_end(n7)
print("\n LL before")
LL.print_list()
delete_unsorted_duplicate_nodes(LL)
print("\n LL after")
LL.print_list()
