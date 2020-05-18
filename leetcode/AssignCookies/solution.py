class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        i = j = 0
        count = 0
        print(g, s)
        while i < len(g) and j < len(s):
            current_greed = g[i]
            smallest_cookie = s[j]

            if current_greed <= smallest_cookie:
                # increase count, move to next child and cookie
                count += 1
                j += 1
                i += 1
            else:
                # move to next smallest cookie
                j += 1

        return count
