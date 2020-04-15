class Solution:
    def numSteps(self, s: str) -> int:
        # Convert from binary to int
        s = int(s, 2)

        steps = 0
        while s != 1:
            # if s is even divide by two, else add 1. Increment steps
            if s % 2 == 0:
                s = s // 2
            else:
                s += 1
            steps += 1
        return steps
