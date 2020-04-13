# Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # copy of list
        front = nums[:]
        # reverse of list
        back = nums[::-1]

        # iterate through both front and back array keeping track of the product of subarrays within
        for i in range(1, len(nums)):
            front[i] *= (front[i-1] or 1)
            back[i] *= (back[i-1] or 1)

        # return the maximum from both front and back array after tallying products
        return max(max(front), max(back))
