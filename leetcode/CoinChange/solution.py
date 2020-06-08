class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:        
        # Values in this array equal the number of coins needed to achieve the cost of the index
        min_coins = [amount + 1] * (amount + 1)
        min_coins[0] = 0
        
        for i in range(1, amount + 1):
            # Loop through every coin value
            for coin in coins:
                # Check that the coin is not bigger than the current amount
                if coin <= i:
                    # min_coins[i]: number of coins needed to make amount i
                    # min_coins[i-coin]: number of coins needed to make the amount before adding 
                    #                   the current coin to it (+1 to add the current coin)
                    min_coins[i] = min(min_coins[i], min_coins[i-coin] + 1)

        
        # Check if any combination of coins was found to create the amount
        if min_coins[amount] == amount + 1:
            return -1
        
        # Return the optimal number of coins to create the amount
        return min_coins[amount]
        