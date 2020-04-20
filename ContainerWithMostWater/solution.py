class Solution:
    def maxArea(self, height: List[int]) -> int:
        '''Using two pointers starting at both ends of list
            keep track of the max_area seen and update if the 
            current area is more than the max_area seen. Move inward depending on
            which side is lower'''
        max_area = 0
        start = 0
        end = len(height) - 1

        while start < end:
            current_area = (end - start) * min(height[start], height[end])
            if current_area > max_area:
                max_area = current_area

            if height[end] < height[start]:
                end -= 1
            else:
                start += 1

        return max_area
