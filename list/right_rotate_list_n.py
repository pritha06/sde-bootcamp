'''Given a list and an integer n, write a Python program to right-rotate the list by n position.'''
def right_rotate(nums,k):
    '''one liner approach: Time complexity : O(n)
    print(nums[-k:]+nums[0:-k])'''
    '''approach 2: Approach #1 : Traverse the first list one by one and then put the elements at required places in a second list. '''
    output=[]
    k=k%len(nums)
    for i in range(len(nums)-k,len(nums)):
        output.append(nums[i])
    for i in range(0,len(nums)-k):
        output.append(nums[i])
    print(output)

n = 14
list_1 = [1, 2, 3, 4, 5, 6]
right_rotate(list_1,n)
