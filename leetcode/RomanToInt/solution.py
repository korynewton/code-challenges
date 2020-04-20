class Solution:
    def romanToInt(self, num: int) -> str:
        ref = {
            "M": 1000,
            "D": 500,
            "C": 100,
            "L": 50,
            "X": 10,
            "V": 5,
            "I": 1
        }

        i = 0
        total = 0

        while i < len(num):
            current = ref[num[i]]
            next = ref[num[i+1]] if i + 1 < len(num) else 0

            if next > current:
                total += next - current
                i += 2
            else:
                total += current
                i += 1

        return total
