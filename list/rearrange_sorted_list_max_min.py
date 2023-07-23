'''Rearrange an array in maximum minimum form using Two Pointer Technique
Given a sorted array of positive integers, rearrange the array alternately
 i.e first element should be a maximum value, at second position minimum value,
  at third position second max, at fourth position second min, and so on. 
'''
'''The idea is to use an auxiliary array.
 We maintain two pointers one to the leftmost or smallest element and the other to the 
 rightmost or largest element. We move both pointers toward each other and alternatively copy 
 elements at these pointers to an auxiliary array. Finally, we copy the auxiliary array back
  to the original array.'''

def rearrange(nums):
    # Auxiliary array to hold modified array
    n=len(nums)
    temp = n*[None]
    left=0
    right=n-1
    # To indicate whether we need to copy remaining
    # largest or remaining smallest at next position
    flag = True
    for i in range(n):
        if flag is True:
            temp[i] = nums[right]
            right -= 1
        else:
            temp[i]=nums[left]
            left+=1
        flag=bool(1-flag)
        # print(bool(1-flag))
    # Copy temp[] to nums[]
    for i in range(n):
        nums[i] = temp[i]
    return nums
# Time Complexity: O(N), Iterating over the array of size N 2 times.
# Auxiliary Space: O(N), since N extra space has been taken.
  
nums=[1, 2, 3, 4, 5, 6]
rearrange(nums)