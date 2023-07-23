'''find the smallest number in given list'''
def find_min(nums):
    #list1.sort() #sort do in place sorting-O(nlogn) 
    #default min uses O(n)
    min_num=nums[0]
    for num in nums:
        if min_num>num:
            min_num=num
    return min_num

    

list1 = [10, 20, 4]
result=find_min(list1)
print(result)