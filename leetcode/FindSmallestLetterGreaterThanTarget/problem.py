#Given a list of sorted characters letters containing only lowercase letters, and given a target letter target, find the smallest element in the list that is larger than the given target.
#
#Letters also wrap around. For example, if the target is target = 'z' and letters = ['a', 'b'], the answer is 'a'.


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        for char in letters:
            if char > target:
                return char
        return min(letters)
        
