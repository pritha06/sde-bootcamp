'''You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.'''


from singly_linkedlist import LinkedList,Node

def reorder_list(LL):
    slow=LL.head
    fast=LL.head.next
    #to find middle
    while fast and fast.next:
        fast=fast.next.next
        slow=slow.next
    #slow is middle ptr, reverse second half of list
    second=slow.next
    slow.next=None
    prev=None
    while second:
        tmp=second.next
        second.next=prev
        prev=second
        second=tmp
    #merge two halves
    first,second=LL.head,prev
    while second:
        tmp1,tmp2=first.next,second.next
        first.next=second
        second.next=tmp1
        first,second=tmp1,tmp2
    return LL


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
reordered_list=reorder_list(LL)
print("\nLL after reordering")
reordered_list.print_list()
