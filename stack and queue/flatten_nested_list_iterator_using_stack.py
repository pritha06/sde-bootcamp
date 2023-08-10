'''Time: O(n)
Space: O(n)
isInteger(), getInteger() and getList() are already defined.
 We can use stack to store the elements in nestedList in reversed order. In the hasNext function we will pop out the top element of the stack. If the top element is integer, we will return True and let next function return the top integer. If the top element is not integer, which means it is the nestedList, we will use getList interface function to get the nested list that this nestedInteger holds, then concatenate it to the previous stack and assign it to stack, this will recusivelt get the integer. The next function will return the top integer of the stack.
  def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

'''
class NestedIterator:
    def __init__(self, nestedList):
        self.stack = []
        self.addInteger(nestedList)
    
    def next(self) -> int:
        return self.stack.pop().getInteger()

    def hasNext(self) -> bool:
        while self.stack:
            top=self.stack[-1]
            if top.isInteger():
                return True
            self.stack=self.stack[:-1]+top.getList()[::-1]
        return False
    
    def addInteger(self, nestedList) -> None:
        while nestedList:
            self.stack.append(nestedList.pop())

NL=[[1,1],2,[1,1]]
nl=NestedIterator(NL)
while nl.hasNext():
    print(nl.next())