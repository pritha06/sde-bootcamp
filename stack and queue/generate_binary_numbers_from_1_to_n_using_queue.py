def generate_binary_numbers(n):
    queue=list()
    ans=list()
    queue.append("1")
    for i in range(n):
        temp=queue.pop(0)
        ans.append(temp)
        queue.append(temp+"0")
        queue.append(temp+"1")
    return ans

result=generate_binary_numbers(10)
print(result)


