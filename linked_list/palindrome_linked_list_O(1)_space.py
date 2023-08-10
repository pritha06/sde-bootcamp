'''O(1) memory and O(n) Time space, two ptrs approach fast and slow
when fast reaches EOL, slow reaches middle, fast+=2, slow+=1
reverse LL after middle is found '''
from singly_linkedlist import LinkedList,Node

def check_palindrome(linked_list):
    fast=linked_list.head
    slow=linked_list.head
    while fast and fast.next:
        fast=fast.next.next
        slow=slow.next
    #at end of above loop slow=middle

    #reverse second half
    prev=None #this prev becomes last node at end of loop which is now after middle
    while slow:
        tmp=slow.next
        slow.next=prev
        prev=slow
        slow=tmp
    
    #check palindrome
    left,right=linked_list.head,prev
    while right:
        if left.data!=right.data:
            return False
        left=left.next
        right=right.next
    return True
    

first_list=LinkedList()
first=Node("1")
second=Node("2")
third=Node("4")
first_list.insert_at_end(first)
first_list.insert_at_end(second)
first_list.insert_at_end(third)
first_list.insert_at_end(Node("2"))
first_list.insert_at_end(Node("1"))
print("printing first list")
first_list.print_list()
print("\ncheck if palindrome or not:")
print(check_palindrome(first_list))