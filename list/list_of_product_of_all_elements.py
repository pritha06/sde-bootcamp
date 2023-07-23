'''find the product of the elements in the array'''

def find_product(nums):
    prod=1
    for num in nums:
        prod*=num
    return prod


arr=[2,4,6,8,10]
result=find_product(arr)
print(result)
