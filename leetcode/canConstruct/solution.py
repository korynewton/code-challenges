class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        letter_count = dict()
        for char in magazine:
            if char in letter_count:
                letter_count[char] += 1
            else:
                letter_count[char] = 1
        
        for char in ransomNote:
            if char in letter_count and letter_count[char] > 0:
                letter_count[char] -= 1
            else:
                return False
            
        return True
        
