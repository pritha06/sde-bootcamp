from singly_linkedlist import Node,LinkedList

def delete_by_value(LL,x):
    if LL.head is None:
        print("List is empty")
        return
    if x==LL.head.data:
        LL.head=LL.head.next
        return
    temp1=LL.head
    temp2=LL.head.next
    while temp2 is not None:
        if x==temp2.data:
            break
        temp2=temp2.next
        temp1=temp1.next
    if temp2 is None:
        print("Last node reached, no value found in list")
    else:
        temp1.next=temp2.next
    
n1=Node(10)
n2=Node(20)
n3=Node(30)
n4=Node(40)
LL=LinkedList()
LL.insert_at_end(n1)
LL.insert_at_end(n2)
LL.insert_at_end(n3)
LL.insert_at_end(n4)
print("\n LL before")
LL.print_list()
print("\n LL after deletion ")
delete_by_value(LL,50)
LL.print_list()