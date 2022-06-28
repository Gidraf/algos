"""
Given two sorted arrays, the task is to merge them in a sorted manner.
Examples: 

Input: arr1[] = { 1, 3, 4, 5}, arr2[] = {2, 4, 6, 8} 
Output: arr3[] = {1, 2, 3, 4, 4, 5, 6, 8}
Input: arr1[] = { 5, 8, 9}, arr2[] = {4, 7, 8} 
Output: arr3[] = {4, 5, 7, 8, 8, 9}

"""


from array import array


def merge_sorted_arrays(arr1, arra2):
    m = len(arra2)
    n = len(arr1)
    arra3 = [None] * (m + n)
    i = 0
    j = 0
    k = 0
    for i in range(len(arr1)):
        counter = 0
        while counter < len(arr2):
            if arr1[i] > arr2[counter]:
                temp = arr1[i]
                arr1[i] = arr2[counter]
                arr2[counter] = temp
            # else:
            #     temp = arra2[counter]
            #     arra2[counter] = arr1[i]
            #     arr1[i] = temp
            counter = counter + 1
            

    arr1.sort()
    arr2.sort()
    return arr1 + arr2 if arra2[0] > arr1[-1] else arra2 + arr1


arr2 = [10,22,33,40,58] 
arr1 = [600,700,800,900,9001]

sorted_array = merge_sorted_arrays(arr1, arr2)

print(sorted_array)
