class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_count, start = 0, 0
        # keep track of chars seen and index
        chars_seen = {}

        for i, char in enumerate(s):
            # if char has been seen, update the start index for the next substring
            if char in chars_seen:
                start = max(start, chars_seen[char] + 1)

            # continue increasing length of substring
            max_count = max(max_count, i - start + 1)
            chars_seen[char] = i

        return max_count
