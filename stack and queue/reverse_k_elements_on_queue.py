def reverse_k_elements(q,k):
    q1=[]
    for i in range(k):
        q1.append(q.pop(0)) #popping one by one element from front and appending them to q1 till k
    print(q1)
    q1=q1[::-1] #reverse q1 list 
    q1=q1+q #q contains only those elements which are not popped out
    return q1



q=[1,2,3,4,5]
k=3
result=reverse_k_elements(q,k)
print(result)