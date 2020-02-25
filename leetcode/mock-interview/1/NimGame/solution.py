class Solution:
    def canWinNim(self, n: int) -> bool:
        # Only false when n is divisible by 4
        # i.e. if n is 8, you can take 1-3 and opponent can remove the amount that would leave only 4 left
        # Otherwise it is posible to win
        if n % 4 == 0:
            return False
        else:
            return True

