
from collections import deque

class MyStack:
    def __init__(self):
        self.q=deque()
        
    
    def push(self,x):              
        self.q.append(x) #append to right only
       
    
    def pop(self):
        for i in range(len(self.q)-1): #run loop till second last value
            self.push(self.q.popleft()) 
        return self.q.popleft() #return the last added value O(n) TC
    
    def top(self):
        return self.q[-1]
    
    def isempty(self):
        return len(self.q)==0
    
    def display(self):
        for ele in self.q:
            print(ele)

q=MyStack()
q.push(4)
q.push(8)
q.push(10)
q.push(12)
# q.display()
# q.pop()
q.display()
q.pop()
print("After popping out the element")
q.display()