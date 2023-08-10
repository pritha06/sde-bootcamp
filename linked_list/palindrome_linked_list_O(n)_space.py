'''
palindrome deals with if list is reversed it should stay the same.
converting LL to array and then checking like usual'''

from singly_linkedlist import LinkedList,Node

def check_palindrome(linked_list):
    nums=[]
    curr=linked_list.head
    while curr:
        nums.append(curr.data)
        curr=curr.next
    print(nums)
    l,r=0,len(nums)-1
    while l<=r:
        if nums[l]!=nums[r]:
            return False
        l+=1
        r-=1
    return True




first_list=LinkedList()
first=Node("1")
second=Node("2")
third=Node("4")
first_list.insert_at_end(first)
first_list.insert_at_end(second)
first_list.insert_at_end(third)
first_list.insert_at_end(Node("2"))
first_list.insert_at_end(Node("3"))
print("printing first list")
first_list.print_list()
print("\ncheck if palindrome or not:")
print(check_palindrome(first_list))