"""
Given two sorted arrays, the task is to merge them in a sorted manner.
Examples: 

Input: arr1[] = { 1, 3, 4, 5}, arr2[] = {2, 4, 6, 8} 
Output: arr3[] = {1, 2, 3, 4, 4, 5, 6, 8}
Input: arr1[] = { 5, 8, 9}, arr2[] = {4, 7, 8} 
Output: arr3[] = {4, 5, 7, 8, 8, 9}

"""

# Divice and Conqur


def merge_sorted_arrays_of_different_size(arr1, arra2):
    m = len(arr1)
    n = len(arra2)
    arra3 = [None] * (m + n)
    i = 0
    j = 0
    k = 0
    while(i + j  < m + n):
        if(j != n and (i == m or arr1[i] > arr2[j])):
            arra3[k] = arr2[j]
            k = k + 1
            j = j + 1
        else:
            arra3[k] = arr1[i]
            i = i + 1
            k = k + 1

    return arra3 



arr1 = [10, 40,30] 
arr2 = [1]

sorted_array = merge_sorted_arrays_of_different_size(arr1, arr2)

print(sorted_array)
