''' Using two pointers and swapping:
Time complexity: O(n)
where n is the length of the list.
Auxiliary space: O(1)
As we are not using any extra space to store the elements.
Loop until left pointer crosses the right pointer:
a. Check if the left element is negative and right element is positive, swap them.
b. If the left element is positive, move the left pointer to the right.
c. If the right element is negative, move the right pointer to the left.
The list is sorted with positive numbers before negative numbers
'''
def rearrange(nums):
    left=0
    right=len(nums)-1
    while left<=right:
        # check if the left element is negative and right element is positive
        if nums[left]<0 and nums[right]>=0:
            nums[left],nums[right]=nums[right],nums[left]
        # if the left element is positive, move the left pointer to the right
        if nums[left]>=0:
            left+=1
        if nums[right]<=0:
            right-=1
    print(nums)




nums=[4, -8, -6, 3, -5, 8, 10, 5, -19]
rearrange(nums)