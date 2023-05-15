"""You're going to write a binary search function.
You should use an iterative approach - meaning
using loops.
Your function should take two inputs:
a Python list to search through, and the value
you're searching for.
Assume the list only has distinct elements,
meaning there are no repeated values, and 
elements are in a strictly increasing order.
Return the index of value, or -1 if the value
doesn't exist in the list."""


def binary_search(input_array, value):
    """Your code goes here."""
    input_array1 = input_array
    for ele in input_array:
        midpoint = len(input_array1) // 2
        if (value > input_array1[midpoint]):
            input_array1 = input_array1[midpoint:len(input_array1)]
        elif (value < input_array1[midpoint]):
            input_array1 = input_array1[0:midpoint]
        elif (value == input_array1[midpoint]):
            return input_array.index(value)
        elif (midpoint == 1 and value != input_array1[midpoint]):
            return -1
    return -1

# ChatGPT's solution, which does not use .index operator (which may be considered cheating in regards to doing a binary search)
# def binary_search(input_array, value):
    # low = 0
    # high = len(input_array) - 1
    # while low <= high:
    #     mid = (low + high) // 2
    #     if input_array[mid] == value:
    #         return mid
    #     elif input_array[mid] < value:
    #         low = mid + 1
    #     else:
    #         high = mid - 1
    # return -1

test_list = [1, 3, 9, 11, 15, 19, 29]
test_val1 = 25
test_val2 = 15
print(binary_search(test_list, test_val1))
print(binary_search(test_list, test_val2))