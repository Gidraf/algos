
def find_median_two_sorted_arrays_of_same_sizes(arra1, arra2):
    m = len(arra1)
    n = len(arra2)
    arra3 = [None] * (m + n)
    median = 0.0
    i = 0
    j = 0
    k = 0
    while(i + j  < m + n):
        if(j != n and (i == m or arra1[i] > arr2[j])):
            arra3[k] = arr2[j]
            k = k + 1
            j = j + 1
        else:
            arra3[k] = arra1[i]
            i = i + 1
            k = k + 1
    if (m+n)%2 ==0:
        f_index = int(((m+n))/2)
        s_index = int((((m+n))/2)-1)
        print(arra3[f_index])
        print(arra3[s_index])
        print(arra3)
        median = (arra3[f_index] + arra3[s_index])/2
    else:
        f_index = int((m+n)/2)
        median = arra3[f_index]
    return median

# arr = [1, 12, 15, 26, 38]
# arr2 = [2, 13, 17, 30, 45]

arr = [ 900 ]
arr2  = [ 5, 8, 10, 20 ]
res = find_median_two_sorted_arrays_of_same_sizes(arr,arr2)

print(res)
