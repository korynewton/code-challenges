class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # add up the difference between all local valleys and peaks
        profit = 0
        for i in range(1, len(prices)):
            prev = prices[i-1]
            current = prices[i]

            if current > prev:
                profit += current - prev

        return profit
