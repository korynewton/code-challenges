class Solution:
    def reverseVowels(self, s: str) -> str:
        index = []
        vowels = []
        s = list(s)
        
        for i in range(len(s)):
            if s[i].lower() in ["a", "e", "i", "o", "u"]:
                index.append(i)
                vowels.append(s[i])
                
        for idx in index:
            s[idx] = vowels.pop()
        
        
        return ''.join(s)
            
