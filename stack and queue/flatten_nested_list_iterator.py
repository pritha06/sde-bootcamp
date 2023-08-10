class NestedIterator:
    def __init__(self,nestedList):
        self.res = []
        self.index = 0
        self.getVal(nestedList)
    
    #suppose nestedlist is of type List<NestedInteger> which has inbuilt methods like isInteger()
    #getInteger(), getList()
    def getVal(self,NestedList):
        for item in NestedList:
            if isinstance(item, int): #if item.isInteger():
                self.res.append(item) #item can be replaced by item.getInteger()
            else:
                self.getVal(item) #item.getList() Call the func recursively until a flat list is obtained


    def next(self):
        self.index+=1
        return self.res[self.index-1] #return self.res.pop(0)
    
    def has_next(self):
        if self.index == len(self.res):
            return False
        return True

NL=[[1,1],2,[1,1]]
nl=NestedIterator(NL)
while nl.has_next():
    print(nl.next())

'''Suppose we have a nested list of integers; we have to implement an iterator to flatten it. Each element is either an integer, or a list. The elements of that list may also be integers or other lists. So if the input is like [[1, 1], 2, [1, 1]], then the output will be [1, 1, 2, 1, 1]

To solve this, we will follow these steps −

In the initializing section, it will take the nested list, this will work as follows −

set res as empty list, index := 0, call getVal(nestedList)

The getVal() will take nestedIntegers, this will work as −

for i in nestedIntegers

if i is an integer, then insert the i into res array, otherwise call getVal(the i list)

The next() method will return the value pointed by index, and increase index by 1

the hasNext() will return true, when there is an element next to it, otherwise false'''
'''It is easiest to apply our flattening method (flatten()) during the class construction process, so that we only ever store the flattened list (data) in our class instance. Since there can be multiple layers of nesting, we should make flatten a recursive function.

With flatten, we should iterate through the given list and if the current element (el) is an integer we should push its contained value onto data, otherwise we should recursively call flatten on the nested list contained in el.

Once our data is successfully flattened, next() should be as easy as removing and returning the lead element of data. When data is reduced to a length of 0, then hasNext() can return false.'''