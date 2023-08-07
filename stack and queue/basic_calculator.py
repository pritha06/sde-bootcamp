def calculate(s):
    if not s:
        return 0
    stack,curr,oper=[],0,"+"
    #starting operation with plus operator so that the value gets appended to stack initially.
    all_operators={"+","-","*","/"}
    nums=set(str(x) for x in range(10))
    for indx in range(len(s)):
        char=s[indx]
        if char in nums:
            curr=curr*10+int(char)
        if char in all_operators or indx==len(s)-1:
            if oper=='+':
                stack.append(curr)
            elif oper=='-':
                stack.append(-curr)
            elif oper=='*':
                stack[-1]*=curr
            elif oper=='/':
                #consider -3//4 and 3//4 
                if stack[-1] >=0 :
                    stack[-1] //= curr
                else:
                    stack[-1] = -(-stack[-1]//curr)    
            curr=0
            oper=char
    return sum(stack)

s="24+10*6-2/2"
print(calculate(s))