""""Let's hope this goes well"""

my_array = [[int]]


def main():
    groupSort([1,1,1,1,1,1])


def groupSort(arr):
    # Write your code here
    # Goal: create an array where the first element is a value in an array and second is that   
    # values frequency// HIGHEST FREQ COMES FIRST, IF TIE, BREAK BY SMALLEST VAL FIRST
    i = 0
    my_array = [[int]] * len(arr)
    while(i < len(arr)):
        if arr[i] in my_array:
            i += 1
        else:
            current_num = arr[i]
            x = arr.count(current_num)
            my_array[i][i] = current_num
            my_array[i][i + 1] = x
            i += 1
    return my_array











