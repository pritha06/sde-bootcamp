'''Time Complexity:

Push operation: O(N), As all the elements need to be popped out from the Queue (q1) and push them back to Queue (q2).
Pop operation: O(1), As we need to remove the front element from the Queue.'''

'''Follow the below steps to implement the push(s, x) operation: 
Enqueue x to q2.
One by one dequeue everything from q1 and enqueue to q2.
Swap the queues of q1 and q2.
Follow the below steps to implement the pop(s) operation: 
Dequeue an item from q1 and return it.'''
from _collections import deque
class MyStack:
    def __init__(self):
        self.q1=deque()
        self.q2=deque()
    
    def push(self,x):
        # Push x first in empty q2   
        self.q2.append(x)
        # Push all the remaining
        # elements in q1 to q2.
        while (self.q1):
            self.q2.append(self.q1.popleft())
        # swap the names of two queues
        self.q1, self.q2 = self.q2, self.q1
    
    def pop(self):
         # if no elements are there in q1
        if self.q1:
            self.q1.popleft()
    
    def peek(self):
        if (self.q1):
            return self.q1[0]
        return None
    
    def isempty(self):
        return not self.q1
    
    def display(self):
        for ele in self.q1:
            print(ele)

s=MyStack()
s.push(4)
s.push(8)
s.push(10)
s.push(12)
s.display()
# q.pop()
print("Last inserted element is ",s.peek())
# s.pop()
# print(s.top())
# s.pop()
# print(s.top())
# s.display()
s.pop()
print("After popping out the element")
s.display()