import random
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
        midlle = (first + last) // 2
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
if __name__ == '__main__':


    #Lets run the code with a list of 1000 random numbers and assume that each number is a target
    length = 1000
    random_list = set()
    for i in range(length):
        random_list.add(random.randint(-3*length, 3*length))
    

    #Sort the random list before searching
    sorted_list = sorted(list(random_list))

    #Lets test the naive search algorithm (By implementing the time it takes to search for the target)
    print("\n-------------Naive Search:----------------")

    naive_start_time = time.time()

    #Here we assume that every number in the list is a target
    for target in sorted_list:
        naive = naive_search(sorted_list, target)
    naive_end_time = time.time()

    print("The time taken by the naive search: %s seconds." % (naive_end_time - naive_start_time))
    print("The time taken by the naive search for one iteration:" ,(naive_end_time - naive_start_time)/length),"seconds."


    #Lets test the binary search algorithm (By implementing the time it takes to search for the target)

    print("\n-------------Binary Search:----------------")

    binary_start_time = time.time()

    #Here we assume that every number in the list is a target
    for target in sorted_list:
        binary = binary_search(sorted_list, 0, len(sorted_list)-1, target)

    binary_end_time = time.time()

    print("The time taken by the binary search: %s seconds." % (binary_end_time - binary_start_time))
    print("The time taken by the binary search for one iteration:",(binary_end_time - binary_start_time)/length," seconds.\n")
