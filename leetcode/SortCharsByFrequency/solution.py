class Solution:
    def frequencySort(self, s: str) -> str:
        if not s:
            return ''
        #convert string to list for sorting ability and sort
        string_to_list = list(s)
        string_to_list.sort()
        
        #group same characters together
        grouped_chars = list()
        current_substr = [string_to_list[0]]
        for char in string_to_list[1:]:
            if current_substr[-1] != char:
                grouped_chars.append(''.join(current_substr))
                current_substr = []
            current_substr.append(char)
        grouped_chars.append(''.join(current_substr))
        
        #sort grouped_chars by length of each element
        grouped_chars.sort(key=lambda str : len(str), reverse=True)
                
        #return as string
        return ''.join(grouped_chars)
        
