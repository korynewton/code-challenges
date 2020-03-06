class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        0=red
        1=white
        2=blue
        
        One pass in constant space. Iterate over list once. If iterator points to 0 remove element
        and place in front, increase iterator. If 2 remove element and append to end of list, 
        decrease num that iterator will reach by one so we dont check the last element twice. 
        If 1 only increase iterator.
        """
        
        length = len(nums)
        i=0
        while i < length:
            if nums[i] == 0:
                nums.insert(nums.pop(i), 0)
                i+=1
            elif nums[i] == 2:
                nums.append(nums.pop(i))
                length -= 1
            else:
                i+=1
        return nums
