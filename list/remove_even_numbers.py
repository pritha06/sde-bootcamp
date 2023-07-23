'''Write a Python Program to remove the Even Numbers from a given List using for loop.'''
def remove_even(nums):
    for i in nums:
        if i%2==0:
            nums.remove(i)
    print(nums)

nums= [11, 22, 31, 44, 51, 65, 71, 82, 91]
remove_even(nums)