
def find_median_two_sorted_arrays_of_same_sizes(arra1, arra2):
    arra3 = [None] * (len(arra1) + len(arra2))
    m = len(arra1)
    n = len(arra2)
    min_size = n if n < m else m
    i = 0
    j = 0
    k = 0
    if (m!=n):
        return 
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
    f_index = int(((m+n)+1)/2)
    s_index = int((((m+n)-1)/2 ))
    print(arra3[f_index])
    print(arra3[s_index])
    print(arra3)
    median = (arra3[f_index] + arra3[s_index])/2
    return median


arr = [1, 12, 15, 26, 38]
arr2 = [2, 13, 17, 30, 45]

res = find_median_two_sorted_arrays_of_same_sizes(arr,arr2)

print(res)