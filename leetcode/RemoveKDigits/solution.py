class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        #if k is equal to our larger than the length of num, return '0'
        if len(num) <= k:
            return '0'
        
        for i in range(k):
            j = 1
            while j < len(num):
                #greedy algorithm. Remove the first number when the number on the right
                #is lower than the number on the left. This will leave us with the lowest
                #posible number for each for loop 
                if num[j-1] > num[j]:
                    num = num[:j-1] + num[j:]
                    break
                #if we've gotten to the end and only seen decreasing numbers, remove the last digit
                elif j == len(num)-1:
                    num = num[:-1]
                else:
                    j += 1
                    
        if num == '0':
            return num
        else:
            #remove leading zeroes before returning
            k = 0
            while k < len(num) and num[k] == '0':
                k += 1
            num = num[k:]
            
            #if the string contained only '0's, num will be an empty string at this point
            return '0' if not num else num
                
                
            
