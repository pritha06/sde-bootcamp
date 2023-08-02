class MyQueue:
    def __init__(self):
        self.s1=[]
        self.s2=[]
    
    def push(self,x):
        while self.s1:
            self.s2.append(self.s1.pop())        
        self.s1.append(x)
        while self.s2:
            self.s1.append(self.s2.pop())
    
    def pop(self):
        return self.s1.pop()
    
    def peek(self):
        return self.s1[-1]
    
    def isempty(self):
        return not self.s1
    
    def display(self):
        for ele in self.s1:
            print(ele)

q=MyQueue()
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