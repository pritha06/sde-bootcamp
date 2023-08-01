class StackInList:
    def __init__(self,stacksize):
        self.stacksize=stacksize
        self.array=[None]*stacksize
        self.ptr1=-1
        self.ptr2=stacksize
    
    def isFull(self):
        if self.ptr1+1==self.ptr2:
            return True
        return False
    
    def traverse(self,stack_number):
        if stack_number==1:
            print("Stack 1: ")
            for i in range(self.ptr1+1):
                print(self.array[i],end=" ")
        else:
            print("Stack 2: ")
            for i in range(self.ptr2,self.stacksize):
                print(self.array[i],end=" ")
                
    def traverse_both_stacks(self):
        for i in range(self.stacksize):
            print(self.array[i],end=" ")

    def push(self,stack_number,data):
        if stack_number==1:
            if not self.isFull():
                self.ptr1+=1
                self.array[self.ptr1]=data
        else:
            if not self.isFull():
                self.ptr2-=1
                self.array[self.ptr2]=data

    def pop(self,stack_number):
        if stack_number==1:
            if self.ptr1!=-1:
                x = self.array[self.ptr1]
                self.ptr1-=1
                return x
        else:
            if self.ptr2!=self.stacksize:
                x=self.array[self.ptr2]
                self.ptr2+=1
                return x

sil=StackInList(5)
sil.push(1,5)
sil.push(2,10)
sil.push(2,15)
sil.push(1,11)
sil.push(2,7)
# sil.traverse(2)
sil.traverse_both_stacks()
print("Popped element from stack 1 is "+str(sil.pop(1)))
sil.traverse_both_stacks()
sil.push(2,40)
print("Popped element from stack 2 is ", str(sil.pop(2)))
sil.traverse_both_stacks()
