class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        seen = dict()
        # keep track of count
        for num in nums:
            if num in seen:
                seen[num] += 1
            else:
                seen[num] = 1

        # loop through seen, return the first key whose value is 1
        for num in seen.keys():
            if seen[num] == 1:
                return num
