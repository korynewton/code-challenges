class Solution:
    def is_vowel(self, char: str) -> bool:
        return char.lower() in ["a", "e", "i", "o", "u"]
    
    def reverseVowels(self, s: str) -> str:
        #convert string to list of chars as strings are immutable
        s = list(s)
        
        #declare two pointers on either end of list
        start = 0
        end = len(s) - 1
        
        while start < end:
            #loop until finding vowel starting from begining
            #increasing index each time a vowel is not found
            while start < end:
                if not self.is_vowel(s[start]):
                    start += 1
                else:
                    break
            #loop until finding a vowel starting from end
            #decreasing index each time a vowel is not found
            while start < end:
                if not self.is_vowel(s[end]):
                    end -= 1
                else:
                    break
                    
            #store vowel at start index in temp variable, then swap
            temp = s[start]
            s[start] = s[end]
            s[end] = temp
            start += 1
            end -= 1
        
        return ''.join(s)
