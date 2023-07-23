'''Given two sorted lists, merge them so as to produce a combined sorted list'''
def merge_sorted_list(test_list1,test_list2):
    size1=len(test_list1)
    size2=len(test_list2)
    res=[]
    i,j=0,0
    while i<size1 and j<size2: #cannot use OR, goes out of index
        if test_list1[i]>test_list2[j]:
            res.append(test_list2[j])
            j+=1
        else:
            res.append(test_list1[i])
            i+=1
    
    res=res+test_list1[i:]+test_list2[j:]
    print(res)

'''TC:O(n),SC:O(n) for above approach'''

'''can also be done in 1 line using sorted(test_list1+test_list2)-
TC: O(nlogn)
Auxiliary Space: O(n), where n is the total number of elements in both lists combined, 
as sorted() creates a new list to store the sorted elements.'''


'''test_list1.extend(test_list2)
test_list1.sort()
Time Complexity: O(nlogn), where n is the total number of elements in both lists. 
Auxiliary Space: O(n), where n is the total number of elements in both lists. 
'''

test_list1 = [1, 5, 6, 9, 11]
test_list2 = [3, 4, 7, 8, 10]
merge_sorted_list(test_list1,test_list2)