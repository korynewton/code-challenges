class Solution:
    def countElements(self, arr: List[int]) -> int:
        arr.sort()
        count = 0
        success = dict()
        for i in range(len(arr)-1, -1, -1):
            current = arr[i]
            if current in success:
                count += 1

            # store the current - 1 so if we see current - 1 we will count it
            success[current-1] = True

        return count
