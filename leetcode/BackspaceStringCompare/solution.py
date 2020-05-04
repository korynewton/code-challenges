class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        s_arr = []
        t_arr = []
        
        s_ptr = t_ptr = 0
        
        for char in S:
            if char != '#':
                s_arr.append(char)
            elif len(s_arr):
                s_arr.pop()
        
        for char in T:
            if char != '#':
                t_arr.append(char)
            elif len(t_arr):
                t_arr.pop()
        
        return ''.join(s_arr) == ''.join(t_arr)
        
