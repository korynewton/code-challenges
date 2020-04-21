class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # move sliding window the size of needle across the hackstack to find a match
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1
