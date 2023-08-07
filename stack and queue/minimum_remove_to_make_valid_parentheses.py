def valid_parentheses(s):
    S=list(s)
    stack=[]
    for i,c in enumerate(S):
        if c==')':
            if stack:
                stack.pop()
            else:
                S[i]=""
        elif c=='(':
            stack.append(i)
    for i in stack:
        S[i]=""
    return ''.join(S)

s="m)n(o)p"
print(valid_parentheses(s))