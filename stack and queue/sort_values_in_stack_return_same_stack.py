def sortStack(stack):
    curr=0 #temp variable
    temp=[] #temp stack
    while stack!=[]: #run loop for all elements of stack
        curr=stack.pop() #curr hold values popped from end of stack
        #if temp is empty or curr value is greater than the last element of temp,append curr to temp
        if len(temp)==0 or curr>temp[len(temp)-1]: 
            temp.append(curr)
        else:
            j=True #set a flag
            while j:
                #if curr is less than last element in temp, append the last element of temp back to stack
                if curr<temp[len(temp)-1]:
                    stack.append(temp.pop())
                    #until temp becomes empty,run the loop, then break when it becomes empty
                    if len(temp)==0:
                        j=False
                else:
                    j=False
            temp.append(curr)
    #append temp to stack until it becomes empty, set in ascending order
    stack.append(temp)
    return stack


stack=[5,3,2,6,11]
print(sortStack(stack))