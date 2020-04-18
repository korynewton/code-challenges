class ValidWordAbbr(object):

    def __init__(self, dictionary):
        """
        :type dictionary: List[str]
        """
        self.dictionary = dictionary

    def isUnique(self, word):
        """
        :type word: str
        :rtype: bool
        """

        for dict_word in self.dictionary:
            if word == dict_word:
                continue

            len_dict_word = len(dict_word)
            len_word = len(word)

            if (len_dict_word == len_word and dict_word[0] == word[0] and dict_word[len_dict_word-1] == word[len_word-1]):
                return False
        return True


# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param_1 = obj.isUnique(word)
