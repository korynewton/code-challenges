import math
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #store target number that must be reached to determine the majority element
        target = math.ceil(len(nums)/2)
        
        
        count = dict()
        #iterate over nums storing the count of each num, return when count == target
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
                
            if count[num] == target:
                return num
                
        
