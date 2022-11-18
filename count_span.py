def count_by_recursion_in_ascending_order(start, end):
    if(start>=end):
        print("End")
        return
    print(start)
    start +=1
    count_by_recursion_in_ascending_order(start, end)


def count_by_for_loop_in_ascending_order(start, end):
    for i in range(start,end+1):
        print(i)

# # count_by_recursion_in_ascending_order(1,10)
# count_by_for_loop_in_ascending_order(1,10)