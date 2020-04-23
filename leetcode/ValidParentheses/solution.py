class Solution:
    def isValid(self, s: str) -> bool:
        matching = {
            "{": "}",
            "(": ")",
            "[":"]"
        }
        stack = []
        
        for char in s:
            if char in matching:
                stack.append(char)
            elif not stack or char !=  matching[stack.pop()]:
                return False
            
        return not stack
        

        