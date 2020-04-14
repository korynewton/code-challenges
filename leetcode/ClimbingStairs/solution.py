class Solution:
    def climbStairs(self, n: int) -> int:
        '''The correct answer for any n will ultimately be the result of 
            adding the results of n-1 and n-2.
            recursively call helper function until we get result for n, utilizing memoization
            to store results along the way.
        '''
        memo = {}

        def recursive_helper(n: int) -> int:
            if n < 3:
                return n
            elif n not in memo:
                memo[n] = recursive_helper(n-1) + recursive_helper(n-2)
            return memo[n]

        return recursive_helper(n)
