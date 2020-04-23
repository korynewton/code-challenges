class Solution:
    def firstUniqChar(self, s: str) -> int:
        if not s:
            return -1

        seen = {}

        # iterate once to count occurances
        for char in s:
            if char in seen:
                seen[char] += 1
            else:
                seen[char] = 1
        # iterate a second time returning the first key which has a value of 1
        # we know now that this was the first unique character in the string
        for i in range(len(s)):
            char = s[i]
            if seen[char] == 1:
                return i

        return -1
