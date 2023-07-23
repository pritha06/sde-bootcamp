'''Find first non-repeating element in a given Array of integers'''

def find_non_repeating(nums):
    dic={}                 #initializing a dictionary
    for i in nums:           #creating a dictionary , with mapping
        dic[i]=0              # frequency of element
    print(dic)
    for i in nums:
        dic[i] +=1
    print(dic)
    for i in nums:          # running a loop in arr
        if dic[i] ==1:       # to check , which element has frequency ==1
            return i
'''using dict:
Time Complexity: O(N).
 Auxiliary Space: O(N)
 
'''
'''Time Complexity: O(n*n), Checking for each element n times
Auxiliary Space: O(1)
approach:
n=len(nums)
    for i in range(n):
        j=0
        while j<n:
            if (i!=j) and (nums[i]== nums[j]):
                break
            j+=1
            if(j==n):
                return nums[i]
    return -1
    '''


nums=[9, 4, 9, 6, 7, 4]
result=find_non_repeating(nums)
print(result)