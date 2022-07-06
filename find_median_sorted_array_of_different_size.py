


from statistics import median


def merge_two_sorted_arrays_of_different_sizes(arra1, arra2):
    arra3 = [None] * (len(arra1) + len(arra2))
    m = len(arra1)
    n = len(arra2)
    mn = m + n
    i = 0
    j = 0
    k = 0

    while j+i < mn:
        if(i != m and (j==n or arra1[i]< arra2[j])):
            arra3[k] = arra1[i]
            i = i + 1
            k = k + 1
        else:
            arra3[k] = arra2[j]
            j = j + 1
            k = k + 1
    median = 0.0
    if (m+n)%2 == 0:
        f_index = int(((m+n))/2)
        s_index = int((((m+n))/2)-1)
        median = median = (arra3[f_index] + arra3[s_index])/2
    else:
        f_index = int(((m+n))/2)
        median = arra3[f_index]
    print(arra3)
    return median


arr2 = [1,2]
arr = [1,3]

res = merge_two_sorted_arrays_of_different_sizes(arr,arr2)

print(res)