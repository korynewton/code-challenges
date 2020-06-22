class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        #loop through nums, keep track of count
        seen = dict()
        for num in nums:
            if num in seen:
                seen[num] += 1
            else:
                seen[num] = 1
                
        #loop through counted numbers, return the first time the value is 1
        for num in seen:
            if seen[num] == 1:
                return num
