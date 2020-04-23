class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:

        for punc in "!?',;.":
            paragraph = paragraph.replace(punc, " ")

        count = {}
        answer = ''
        max = 0

        for word in paragraph.split(" "):
            if word == '':
                continue

            lower_word = word.lower()

            if lower_word not in banned:
                if lower_word in count:
                    count[lower_word] += 1
                else:
                    count[lower_word] = 1

                if count[lower_word] > max:
                    max = count[lower_word]
                    answer = lower_word
        return answer
