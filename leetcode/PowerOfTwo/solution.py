class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        #keep track of current value
        current = 1
        #keep track of exponent
        exponent = 0
    
        #loop while current remains less than n,
        #if current is greater than n, then it is not a power of two 
        while current <= n:
            #set current to 2 raised to the current exponent
            current = 2 ** exponent
            
            #check if current equals the number we are looking for which
            #would indicate if it is a power of two
            if current == n:
                return True
            #if not increase the exponent
            else:
                exponent += 1
        
        return False
        