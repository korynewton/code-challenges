class Solution:
    def myAtoi(self, str):
        # strip whitespace
        str_list = list(str.lstrip())
        if len(str_list) == 0:
            return 0

        # determine if positive of negative
        sign = -1 if str_list[0] == "-" else 1

        # remove sign from list
        if str_list[0] in ["-", "+"]:
            str_list.pop(0)

        # loop through list adding elements until end or non digit is reached
        res, i = 0, 0
        while i < len(str_list) and str_list[i].isdigit():
            res = res*10 + ord(str_list[i]) - ord('0')
            i += 1

        MININT = -2**31
        MAXINT = 2**31 - 1
        result = res * sign

        if result > MAXINT:
            return MAXINT
        elif result < MININT:
            return MININT
        else:
            return result
