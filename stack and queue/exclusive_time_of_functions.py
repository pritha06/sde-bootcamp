'''
Time:  O(n)
Space: O(n)

Given the running logs of n functions that are executed
in a nonpreemptive single threaded CPU, find the exclusive time of these functions.

Each function has a unique id, start from 0 to n-1.
A function may be called recursively or by another function.

A log is a string has this format : function_id:start_or_end:timestamp.
For example, "0:start:0" means function 0 starts from the very beginning of time 0.
"0:end:0" means function 0 ends to the very end of time 0.

Exclusive time of a function is defined as the time spent within this function,
the time spent by calling other functions should not be considered as
this function's exclusive time.
You should return the exclusive time of each function sorted by their function id.

Example 1:
Input:
n = 2
logs =
["0:start:0",
 "1:start:2",
 "1:end:5",
 "0:end:6"]
Output:[3, 4]

Explanation:
Function 0 starts at time 0, then it executes 2 units of time and reaches the end of time 1.
Now function 0 calls function 1, function 1 starts at time 2, executes 4 units of time and end at time 5.
Function 0 is running again at time 6, and also end at the time 6, thus executes 1 unit of time.
So function 0 totally execute 2 + 1 = 3 units of time, and function 1 totally execute 4 units of time.

Note:
Input logs will be sorted by timestamp, NOT log id.
Your output should be sorted by function id,
which means the 0th element of your output corresponds to the exclusive time of function 0.
Two functions won't start or end at the same time.
Functions could be called recursively, and will always end.
1 <= n <= 100
'''
def exclusive_time(n,logs):
    result=[0]*n #to maintain output
    stack=[] #to maintain start of funcns
    prev=0 #to maintain end values
    for log in logs: #run loop over log values
        tokens=log.split(":")
        if tokens[1]=='start': #if start append func id to stack
            if stack:
                result[stack[-1]]+=int(tokens[2])-prev #if stack already exist, modify last value in result list
            stack.append(int(tokens[0])) 
            prev=int(tokens[2]) #set prev to track start time of func
        else: #if end is given, pop last inserted id from stack and set its corresponding result as end time-start time+1
            result[stack.pop()]+=int(tokens[2])-prev+1
            prev=int(tokens[2])+1 #set prev to end time now
    return result

n = 2
logs =["0:start:0", "1:start:2","0:start:4", "0:end:5", "0:start:6","0:end:7","1:end:8","0:end:10"]
print(exclusive_time(n,logs))