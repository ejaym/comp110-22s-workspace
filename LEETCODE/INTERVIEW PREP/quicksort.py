"""Implement quick sort in Python.
Input a list.
Output a sorted list."""


def quicksort(array):
    if len(array) <= 1:
        return array
    
    pivot = array[-1]  # Choose the last element as the pivot
    smaller = []
    equal = []
    larger = []

    for num in array:
        if num < pivot:
            smaller.append(num)
        elif num == pivot:
            equal.append(num)
        else:
            larger.append(num)

    return quicksort(smaller) + equal + quicksort(larger)


test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print(quicksort(test))