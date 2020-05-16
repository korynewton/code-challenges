class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # sort by second element in each interval (end point)
        intervals.sort(key=lambda x: x[1])
        count = 0
        current_min = float('-inf')
        for interval in intervals:
            if interval[0] >= current_min:
                current_min = interval[1]
                count += 1

        # return difference of # of intervals vs # of non overlaps
        return len(intervals) - count
