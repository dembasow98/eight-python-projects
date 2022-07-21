import time

#implementation of naive search algorithm

def naive_search(list, target):
    for item in range(len(list)):
        if list[item] == target:
            return item
    return -1



#Binary Search uses a divide and conquer approach to search for a target value in a sorted list.
#The divide and conquer approach is a divide and conquer strategy where the list is divided into two halves,
#and the target is searched in the two halves.
#If the target is not found, the search is repeated on the two halves.
#The divide and conquer approach is a recursive strategy.
#The base case is when the list is empty or the target is not found.
#The recursive case is when the target is found or the list is not empty.
#The recursive case is when the target is not found and the list is not empty.


def binary_search(list,first, last,target):
    #base case
    if last>=first:
        midlle = (first+last) // 2
        #The element at the middle of the list is the target itself
        if list[midlle] == target:
            return midlle
        #The element at the middle of the list is greater than the target
        elif list[midlle] > target:
            return binary_search(list, first, midlle-1, target)
        #The element at the middle of the list is less than the target
        elif list[midlle] < target:
            return binary_search(list, midlle+1 , last, target)
    #The element is not present in the list
    else:
        return -1


#Run the code
list = [1,2,3,4,5,6,7,8,9,10]

print("\n-------------Naive Search:----------------")
start_time = time.time()
#Lets test the naive search algorithm (By implementing the time it takes to search for the target)
naive = naive_search(list, 5)
print("The time taken to find the target by the naive search: %s seconds." % (time.time() - start_time))
print("Your target is at index: %s" % naive)

#Lets test the binary search algorithm (By implementing the time it takes to search for the target)

print("\n-------------Binary Search:----------------")
start_time = time.time()
#Lets test the naive search algorithm (By implementing the time it takes to search for the target)
binary = binary_search(list, 0, len(list)-1, 5)
print("The time taken to find the target by the binary search: %s seconds." % (time.time() - start_time))
print("Your target is at index: %s" % binary)