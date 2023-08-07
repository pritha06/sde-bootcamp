def sortStack(stack):
    tempstack=[]
    while stack:
        temp=stack.pop()
        while tempstack!=[] and tempstack[-1]>temp:
            stack.append(tempstack.pop())
            
        tempstack.append(temp)
    return tempstack



stack=[5,3,2,6,11]
print("Input stack: ",stack)
tmpstack=sortStack(stack)
print(tmpstack)
