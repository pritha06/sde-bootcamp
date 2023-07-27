from singly_linkedlist import LinkedList,Node

def final_merged_lists(first_list,second_list,merged_list):
    currentFirst=first_list.head
    currentSecond=second_list.head
    while True:
    #condition to break loop is when currentFirst becomes empty
        if currentFirst is None:
            merged_list.insert_at_end(currentSecond)
            break
        if currentSecond is None:
            merged_list.insert_at_end(currentFirst)
            break
        if currentFirst.data<currentSecond.data:
            currentFirstNext=currentFirst.next
            #set current first next to none because existing points nhi aane chahie only data ana chahie
            currentFirst.next=None
            merged_list.insert_at_end(currentFirst)
            currentFirst=currentFirstNext
        else:
            currentSecondNext=currentSecond.next
            #set current first next to none because existing points nhi aane chahie only data ana chahie
            currentSecond.next=None
            merged_list.insert_at_end(currentSecond)
            currentSecond=currentSecondNext


#FirstList
first_list=LinkedList()
first=Node("1")
second=Node("3")
third=Node("4")
first_list.insert_at_end(first)
first_list.insert_at_end(second)
first_list.insert_at_end(third)
print("printing first list")
first_list.print_list()

#SecondList
second_list=LinkedList()
four=Node("2")
five=Node("7")
six=Node("9")
second_list.insert_at_end(four)
second_list.insert_at_end(five)
second_list.insert_at_end(six)
print("printing second list")
second_list.print_list()

#Merged List
merged_list=LinkedList()
final_merged_lists(first_list,second_list,merged_list)
del first_list
del second_list
print("Final merged list")
merged_list.print_list()