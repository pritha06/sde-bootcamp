'''Program to find any two numbers in a list that sums up to k in Python'''
def find_num(nums,k):
    res=[]
    for num in nums:
        if (k-num) in res:
            return num,k-num
        else:
            res.append(num)
'''TC: O(n), SC:O(n)'''

'''approach 2: 
use a set to keep track of the elements we have seen so far
result = []
seen = set()
for num in nums:
    complement = k - num
    if complement in seen:
        result.append((num, complement))
    seen.add(num)
return result
this is valid for all pairs of numbers that add up to a particular value.
The time complexity of this algorithm is O(n), where n is the length of the given list. This is because we iterate over each element in the list once and perform constant time operations (such as set lookup and list append) for each element.

Space Complexity:
The space complexity of this algorithm is O(n), where n is the length of the given list. This is because we store the elements seen so far in a set and the result pairs in a list, both of which can have a maximum size of n

'''
nums = [45, 18, 9, 13, 12]
k=31
result=find_num(nums,k)
print(result)
