class Solution:
    def trap(self, height: List[int]) -> int:
        # find max up until index from left
        max_from_left = [None] * len(height)
        current_max = 0
        for i in range(len(height)):
            block = height[i]
            current_max = max(block, current_max)
            max_from_left[i] = current_max

        # find max up until index from right
        max_from_right = [None] * len(height)
        current_max = 0
        for i in range(len(height)-1, -1, -1):
            block = height[i]
            current_max = max(block, current_max)
            max_from_right[i] = current_max

        # the difference between the minimum of the two max lists and the current height will
        # be the amount of water that will fill up that index
        total = 0
        for i in range(len(height)):
            total += min(max_from_right[i], max_from_left[i]) - height[i]

        return total
