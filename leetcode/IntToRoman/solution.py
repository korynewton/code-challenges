class Solution:
    def intToRoman(self, num: int) -> str:
        ref = {
            1000: "M",
            900: "CM",
            500: "D",
            400: "CD",
            100: "C",
            90: "XC",
            50: "L",
            40: "XL",
            10: "X",
            9: "IX",
            5: "V",
            4: "IV",
            1: "I"
        }

        result = []

        # Loop through all int representations of posible roman
        # numerals from greatest to least
        for integer in ref.keys():
            # the first one that passes this evaluation is the next optimal numeral to add
            if integer <= num:
                # determine how many times this symbol will be needed
                # (i.e.) so "III" can be done in one pass as opposed to "I"
                # on 3 different passes
                num_times = num // integer
                to_add = ref[integer] * num_times
                result.append(to_add)

                # decrement num by the amount we are adding to our result
                num -= integer * num_times
            else:
                continue

        return ''.join(result)
