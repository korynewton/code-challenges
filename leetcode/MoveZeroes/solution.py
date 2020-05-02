class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        last_index = len(nums)-1
        current = 0
        while current <= last_index:
            # if the element at the current index is 0, append to end of list
            # then decrement the last index we will check for 0
            if nums[current] == 0:
                nums.append(nums.pop(current))
                last_index -= 1
            # only increment current when the current item isnt a zero
            else:
                current += 1

        return nums
