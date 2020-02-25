class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        # use bitwise xor to find bits that differentiate, convert to '0bxxxx' format string
        # count and return number of ones in string which indicate where corrisponding bits were different.
        xy_xor = bin(x ^ y)
        num_1s = 0
        for i in range(2,len(xy_xor)):
            if xy_xor[i] == '1':
                num_1s += 1
        return num_1s
        
        
