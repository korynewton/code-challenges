class Solution:
    def does_match(self, s1_arr: list, s2_arr: list) -> bool:
        #checks if the two lists are equal
        for i in range(26):
            if s1_arr[i] != s2_arr[i]:
                return False
        return True
        
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #if s1 is longer than s2 it is impossible for s1 to be a substring of s2
        if len(s1) > len(s2): return False
        
        #map letter frequencies in s1 to a list
        s1_arr = [0]*26
        for char in s1:
            s1_arr[ord(char) - ord('a')] += 1
        
        #using a sliding window map letter frequencies of s2
        #window length is the length of s1
        for i in range(len(s2)-len(s1)+1):
            s2_arr = [0]*26
            for j in range(len(s1)):
                s2_arr[ord(s2[i+j]) - ord('a')] += 1
            #after calculating the frequencies, see if the char frequencies
            #of s1 and the window of s2 match
            if self.does_match(s1_arr, s2_arr):
                return True
            
        return False
            
        

        
