'''While traversing the linked list one of these things will occur-

The Fast pointer may reach the end (NULL) this shows that there is no loop in the linked list.
The Fast pointer again catches the slow pointer at some time therefore a loop exists in the linked list.'''
'''Pseudocode:

Initialize two-pointers and start traversing the linked list.
Move the slow pointer by one position.
Move the fast pointer by two positions.
If both pointers meet at some point then a loop exists and if the fast pointer meets the end position then no loop exists.'''
'''Time complexity: O(n), as the loop is traversed once. 
Auxiliary Space: O(1), only two pointers are used therefore constant space complexity.'''
from singly_linkedlist import LinkedList,Node

# detect if there is a loop
# in the linked list
def detectLoop(LL):
	slowPointer = LL.head
	fastPointer = LL.head

	while (slowPointer != None
		and fastPointer != None
		and fastPointer.next != None):
		slowPointer = slowPointer.next
		fastPointer = fastPointer.next.next
		if (slowPointer == fastPointer):
			return 1

	return 0


n1=Node(10)
n2=Node(20)
n3=Node(30)
n4=Node(40)
n5=Node(50)
LL=LinkedList()
LL.insert_at_end(n1)
LL.insert_at_end(n2)
LL.insert_at_end(n3)
LL.insert_at_end(n4)
LL.insert_at_end(n5)
print("\nLL before")
LL.print_list()
# adding a loop for the sake
# of this example
temp = LL.head
while (temp.next != None):
	temp = temp.next

temp.next = LL.head

# loop added;
if (detectLoop(LL)):
	print("Loop exists in the Linked List")
else:
	print("Loop does not exists in the Linked List")

