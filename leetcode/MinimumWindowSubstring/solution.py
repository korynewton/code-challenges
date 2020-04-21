class Solution:
    def minWindow(self, s: str, t: str) -> str:
        '''
        Move end index to the right unil window is found, 
        then move start index right to find a smaller window.
        '''
        char_count = {}
        for char in t:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1

        start, end = 0, 0

        current_min_window = len(s)
        current_min_start = 0

        letters_in_target = len(t)

        while end < len(s):
            if s[end] in char_count:
                if char_count[s[end]] > 0:
                    letters_in_target -= 1
                char_count[s[end]] -= 1

            while letters_in_target == 0:
                if end - start < current_min_window:
                    current_min_window = end - start
                    current_min_start = start

                if s[start] in char_count:
                    char_count[s[start]] += 1

                    if char_count[s[start]] > 0:
                        letters_in_target += 1
                start += 1

            end += 1

        if current_min_window == len(s):
            return ''
        else:
            return s[current_min_start: current_min_start + current_min_window + 1]
