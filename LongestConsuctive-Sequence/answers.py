def longest_consecutive(nums):
    # This is to remove any duplicate value that the array may contain
    set_integers = set(nums)
    for i in nums:
        if nums[i]-1 not in set_integers:
            j = nums[i]
            while(set.contains(j)):
                j = j+1
            if result < j - nums[i]:
                result = j- nums[i]
    return result
