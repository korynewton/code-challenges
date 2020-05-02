class Solution:
    def isHappy(self, n: int) -> bool:
        def helper(num, seen=[]):
            # base case, we've found a happy number
            if num == 1:
                return True
            # make sure we havent seen this number before
            # would indicate we have hit a cycle
            elif num in seen:
                return False
            else:
                seen.append(num)
                sum = 0
                while num:
                    last_digit = num % 10
                    sum += last_digit**2
                    num = num//10
                return helper(sum, seen)

        return helper(n)
