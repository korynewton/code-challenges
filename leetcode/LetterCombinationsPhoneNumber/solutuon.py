class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone = {
            "2" : ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x","y", "z"]
        }
        
        
        def recurse(combination, next_letters):
            if len(next_letters) == 0:
                output.append(combination)
            else:
                for letter in phone[next_letters[0]]:
                    recurse(combination + letter, next_letters[1:])
        
        
        output = []
        if digits:
            recurse('', digits)
        return output
        