'''
Example 1:
Input: “abbaca”
Output: “ca”
Explanation:
For example, in “abbaca” we could remove “bb” since the letters are adjacent and equal, 
and this is the only possible move. 
The result of this move is that the string is “aaca”, of which only “aa” is possible,
so the final string is “ca”.
The time complexity is O(N). Space complexity is O(N).
The ideal/optimal solution would be to use an additional stack data structure, 
pushes each character if it is not the same as the top of the stack. 
Remove the top of the stack if it matches the next character.'''
def remove_duplicates(s):
    ans=[]
    for i in s:
        if len(ans) and i==ans[-1]:
            ans.pop()
        else:
            ans.append(i)
    return ''.join(ans)


s="abbaca"
print(remove_duplicates(s))
