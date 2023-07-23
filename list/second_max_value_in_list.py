'''find second max value in a list'''
def find_second(nums):
    '''Traverse once to find the largest and then once again to find the second largest. 
    Time Complexity: O(N) Auxiliary Space: O(1)
'''
    secondLargest=0
    largest=min(nums)
    for i in range(len(nums)):
        if nums[i]>largest:
            secondLargest=largest
            largest=nums[i]
        else:
            secondLargest=max(secondLargest,nums[i])
    return secondLargest

    '''Sort the list in ascending order and print the second last element in the list.
    Time Complexity: O(nlogn)
Auxiliary Space: O(1)
'''
'''code:
    # list2=list(set(nums))
    # list2.sort()
    # return list2[-2]'''

    

nums=[8,15,90,89,20]
result=find_second(nums)
print(result)