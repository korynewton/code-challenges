class Solution:
    def optimalDivision(self, nums: List[int]) -> str:
        length = len(nums)
        if length == 1:
            return str(nums[0])
        elif length == 2:
            return str(nums[0]) + "/" + str(nums[1])
        else:
            result = str(nums[0]) + "/(" + str(nums[1])
            for i in range (2,length):
                result += "/" + str(nums[i])
            result += ")"
            return result
    
