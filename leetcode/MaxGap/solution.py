class Solution:
    def binaryGap(self, N: int) -> int:
        binary = bin(N)
        pointer_1 = pointer_2 = 0
        max_gap = 0

        for i in range(2,len(binary)):
            if binary[i] == '1':
                if pointer_1 == 0:
                    #set pointer_1 to index, will mark the first instance of 1
                    pointer_1 = i
                else:
                    # set pointer_2 to index
                    # set max_gap to the higher value: max_gap or difference between two pointers
                    pointer_2 = i
                    max_gap = max(pointer_2 - pointer_1, max_gap)
                    pointer_1 = pointer_2

        return max_gap



