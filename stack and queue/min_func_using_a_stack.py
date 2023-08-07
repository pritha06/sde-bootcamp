class minStack:
    def __init__(self):
        self.stack=[]
        self.minstack=[]
    
    def push(self,val):
        self.stack.append(val)
        val=min(val,self.minstack[-1] if self.minstack else val)
        self.minstack.append(val)
    
    def pop(self):
        self.stack.pop()
        self.minstack.pop()
    
    def top(self):
        return self.stack[-1]
    
    def getmin(self):
        return self.minstack[-1]

ms=minStack()
ms.push(4)
ms.push(-2)
ms.push(10)
ms.push(-2)
# ms.push(-6)
print(ms.getmin())