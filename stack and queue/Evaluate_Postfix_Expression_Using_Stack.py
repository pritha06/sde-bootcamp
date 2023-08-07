'''Time complexity: O(n)

Space complexity: O(n)
A stack can be used to evaluate a postfix expression by following these steps:

Step 1: Create an empty stack.

Step 2: Iterate through the postfix expression from left to right.

Step 3: For each element in the postfix expression, do the following:

If the element is an operand (a number), push it onto the stack.
If the element is an operator (+, -, *, /, etc.), pop the top two elements from the stack, apply the operator to these elements, and push the result back onto the stack.
Step 4: After all elements have been processed, the result of the expression will be the single element left on the stack.'''


def postfix_expression(exp):
    operators=["+","-","*","/","**"]
    operand=[]
    for ele in exp:
        if ele not in operators:
            operand.append(ele)
        else:
            num1=operand.pop()
            num2=operand.pop()
            if ele=='+':
                operand.append(num2+num1)
            elif ele=='-':
                operand.append(num2-num1)
            elif ele=='*':
                operand.append(num2*num1)
            elif ele=='/':
                operand.append(num2/num1)
            else:
                operand.append(num2**num1)
       
    return operand[0]


exp=[4,5,"*",6,3,"+","-",18,2,'/','+']
print(postfix_expression(exp))