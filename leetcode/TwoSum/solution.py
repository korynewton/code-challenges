
nums = [2,7,11,15]
target = 9


def two_sums():
    nums_seen = dict()
    for i in range(len(nums)):
        current = nums[i]
        matching_pair = target - current
        
        #check if we've seent the matching_pair num before
        #if so return with indices
        if matching_pair in nums_seen.keys():
            return [nums_seen[matching_pair],i]

        nums_seen[current]=i

    return False
print(two_sums())
