class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        map_pattern = dict()
        split_str = str.split()
        
        if len(pattern) != len(split_str):
            return False

        for i in range(len(pattern)):
            pattern_char = pattern[i]
            str_word = split_str[i]
            
            if pattern_char not in map_pattern:
                if str_word not in map_pattern.values():
                    map_pattern[pattern_char] = str_word
                else:
                    return False
            else:
                if map_pattern[pattern_char] != str_word:
                    return False
        return True
            
            
