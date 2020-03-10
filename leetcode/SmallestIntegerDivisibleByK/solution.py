class Solution:
    def smallestRepunitDivByK(self, K: int) -> int:
        if K % 2 == 0 or K % 5 == 0:
            return -1
        
        N = 1
        mod = N % K
        
        while mod:
            N = N * 10 + 1
            mod = N % K

            
        return len(str(N))
                
                
            
