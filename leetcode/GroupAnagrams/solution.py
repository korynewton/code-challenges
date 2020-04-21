class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = dict()

        for word in strs:
            # sort word
            sorted_word = ''.join(sorted(word))

            # if we've seen this sorted word before, add to list of corresponding anagrams
            if sorted_word in anagrams:
                anagrams[sorted_word].append(word)
            else:
                # else add anagram to dictionary, starting a new list
                anagrams[sorted_word] = [word]

        return anagrams.values()
