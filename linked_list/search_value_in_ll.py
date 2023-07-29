from singly_linkedlist import LinkedList,Node

def search_value(first_list,val):
    currNode=first_list.head
    if currNode is None:
        print("List is empty")
        return
    flag=0
    currPos=0
    while currNode:
        if currNode.data==val:
            print("The element {} is found at position {}".format(val,currPos))
            flag=1
        currPos+=1
        currNode=currNode.next
    if flag==0:
        print("{} is not present in list.".format(val))


first_list=LinkedList()
first=Node("1")
second=Node("3")
third=Node("4")
first_list.insert_at_end(first)
first_list.insert_at_end(second)
first_list.insert_at_end(third)
print("printing first list")
first_list.print_list()
print("Search for given value starts:")
search_value(first_list,"5")
search_value(first_list,"3")
search_value(first_list,"2")
search_value(first_list,"1")