class Solution:
    def fractionToDecimal(self, numerator, denominator):
        # if denominator is 0, return
        if not denominator:
            return
        #if numerator is 0, return "0"
        if not numerator:  # numerator is 0
            return "0"
        
        
        result = []
        #use XOR to see if one but not both are negative, if so append - sign
        if (numerator < 0) ^ (denominator < 0):
            result.append("-")  
        
        numerator, denominator = abs(numerator), abs(denominator)
        
        #add pre decimal integer to  result
        result.append(str(numerator//denominator))
        
        remainder = numerator % denominator
        # if no remainer then answer is a whole number, return result as string
        if not remainder:
            return "".join(result)
        
        #if we havent returned then work on decimal portion of answer 
        result.append(".")
        seen = {}
        while remainder:
            #if the current remainder has been seen, we have found the repeating sequence,
            #break loop and return
            if remainder in seen:
                result.insert(seen[remainder], "(")
                result.append(")")
                break
            #store remainder as seen storing length of remainder as value
            # result length will be used for index when repeating sequence is found
            else:
                seen[remainder] = len(result) 
                dividend, remainder = divmod(remainder*10, denominator)
                result.append(str(dividend))
                
        return "".join(result)





