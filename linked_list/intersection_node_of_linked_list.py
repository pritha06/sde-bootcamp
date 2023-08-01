from singly_linkedlist import Node,LinkedList

def intersection_node(LL1,LL2):
    l1=LL1.head
    l2=LL2.head
    while l1!=l2:
        l1=l1.next if l1 else LL2.head
        l2=l2.next if l2 else LL1.head
    return l1

n1=Node(1)
n2=Node(2)
n3=Node(3)
n4=Node(4)
n5=Node(5)
LL1=LinkedList()
LL1.insert_at_end(n1)
LL1.insert_at_end(n2)
LL1.insert_at_end(n3)
LL1.insert_at_end(n4)
LL1.insert_at_end(n5)
print("List1")
LL1.print_list()
n6=Node(9)
n7=Node(8)
n8=Node(7)
n9=Node(6)
n10=Node(5)
n11=Node(4)
LL2=LinkedList()
LL2.insert_at_end(n6)
LL2.insert_at_end(n7)
LL2.insert_at_end(n8)
LL2.insert_at_end(n9)
LL2.insert_at_end(n10)
LL2.insert_at_end(n11)
print("\nList2")
LL2.print_list()
intersection_node=intersection_node(LL1,LL2)
print("Intersection node is : ",intersection_node)