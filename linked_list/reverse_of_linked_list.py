class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    def insert_at_beginning(self,newNode):
        temp=self.head
        self.head=newNode
        newNode.next=temp
        del temp
    
    def print_list(self):
        curr=self.head
        while True:
            if curr is None:
                break
            print(curr.data,end=" ")
            curr=curr.next

    #The head starts pointing to the last element of the list.
    '''
    ITerative approach: 
    previous: Initially pointing at None (line 3), this variable points to the previous 
    element so the node.next link can be reversed using it (line 9).
     This is then updated to the node next to it, i.e., current (line 10).

current: Initially pointing to head (line 4), the node being pointed to by this 
variable gets its node.next set to the previous item in the list (line 9). This is 
then updated to the node next to it,​ i.e., following (line 11).

following: Initially pointing to the second node (line 5), this is used so the current
 pointer may move one step ahead (line 12-13) in each iteration.
'''
 #Recursive approach uses stack implementation O(n) space.
    def reverse(self):
        previous = None         # `previous` initially points to None
        current = self.head     # `current` points at the first element
        # go till the last element of the list 
        while current:
            nxt=current.next #nxt points at second element
            current.next = previous # reverse the link
            previous = current      # move `previous` one step ahead
            current = nxt         # move `current` one step ahead
        self.head=previous
    
    def reverse_recursive(self):

        def _reverse_recursive(cur, prev):
            if not cur:
                return prev

            nxt = cur.next
            cur.next = prev
            prev = cur 
            cur = nxt 
            return _reverse_recursive(cur, prev)

        self.head = _reverse_recursive(cur=self.head, prev=None)

    

first=Node(1)
second=Node(2)
third=Node(3)
ll=LinkedList()
ll.insert_at_beginning(first)
ll.insert_at_beginning(second)
ll.insert_at_beginning(third)
print("List before reversal")
ll.print_list()
# ll.reverse()
ll.reverse_recursive()
print("\n List after reversal")
ll.print_list()