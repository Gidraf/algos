


def merge_two_sorted_arrays_of_different_sizes(arra1, arra2):
    arra3 = [None] * (len(arra1) + len(arra2))
    m = len(arra1)
    n = len(arra2)
    min_size = n if n < m else m
    i = 0
    j = 0
    k = 0

    while i < min_size and i < m and j < n:
        if(arra1[i] <= arra2[j]):
            arra3[k] = arra1[i]
            i = i + 1
            k = k + 1

        else:
            arra3[k] = arra2[j]
            j = j + 1
            k = k + 1
    while(i < m):
        arra3[k] = arra1[i]
        i = i + 1
        k = k + 1
    while (j < n):
        arra3[k] = arra2[j]
        j = j + 1
        k = k + 1

    return arra3


arr2 = [1,2,4,5,6,7,8,9,9,10,12,13]
arr = [10,11,12,13,14,15,16,17,80,80]

res = merge_two_sorted_arrays_of_different_sizes(arr,arr2)

print(res)