class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # prods right will contain products of all elements to the right of element in nums
        prods_right = [None] * (len(nums)-1) + [1]
        for j in range(len(nums)-2, -1, -1):
            prods_right[j] = prods_right[j+1] * nums[j+1]

        # prods left will contain products of all elements to the left of element in nums
        prods_left = [1] + [None] * (len(nums)-1)
        for i in range(1, len(nums)):
            prods_left[i] = prods_left[i-1] * nums[i-1]

        # the product of the elements at the same index in each array will
        # product of all elements of original array except self
        return [prods_left[k] * prods_right[k] for k in range(len(nums))]
