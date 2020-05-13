class Solution:
    def reverse(self, x: int) -> int:
        positive = True if x > 0 else False
        
        #base cases if only one digit
        if (x < 10 and positive) or (not positive and x > -10):
            return x
        
        #insure x is now positive
        x = abs(x)
        
        #build string of new num by removing last digit from x on each loop
        new_num = ''
        while x > 0:
            last_digit = x % 10
            new_num += str(last_digit)
            x //= 10
        
        #check if new_num exceeds range of 32 bit signed integer
        if int(new_num) > 2**31-1:
            return 0
        elif positive:
            return int(new_num)
        else:
            return int('-'+new_num)
