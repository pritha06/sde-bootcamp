

def balanced(A):
    stack=[]
    closeToOpen={")":"(","]":"[","}":"{"}
    #use hashmap to store pairs as dict
    #run a loop over elements
    for ch in A:
        #if closing element is present in A then check if top of stack points to opening bracket or not
        if ch in closeToOpen:
            #stack shouldn't be empty, if key pair is found  then pop that element, if not found return False
            if stack and stack[-1]==closeToOpen[ch]:
                stack.pop()
            else:
                return False
        #if it's an opening bracket, append to stack
        else:
            stack.append(ch)
    #after traversing, stack should be empty, all elements should be popped out
    if len(stack)==0:
        return True
    else:
        return False

A='[{)}]'
print(balanced(A))

