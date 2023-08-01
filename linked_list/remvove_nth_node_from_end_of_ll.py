from singly_linkedlist import Node,LinkedList

def delete_by_value(LL,n):
    '''Time complexity:O(n)
    Space:O(1)
    '''
    start=Node(2)
    start.next=LL.head
    left=start
    right=LL.head
    if n==LL.len_list():
        LL.delete_at_beginning()
    while n>0 and right:
        right=right.next
        n-=1
    while right:
        left=left.next
        right=right.next
    left.next=left.next.next
    return start.next

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
print("\n LL before")
LL.print_list()
print("\n LL after deleting nth node from end of LL")
delete_by_value(LL,6)
LL.print_list()