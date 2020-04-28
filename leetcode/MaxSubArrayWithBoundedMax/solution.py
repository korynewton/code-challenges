class Solution:
    def numSubarrayBoundedMax(self, A: List[int], L: int, R: int) -> int:
        start = 0
        count = 0

        while start < len(A):
            end = start + 1

            while end < len(A)+1:
                current_max = max(A[start:end])
                if current_max > R:
                    # if the current max is greater than R we should break this while loop
                    # as there is no reason to continue adding to this subarray
                    break
                elif current_max <= R and current_max >= L:
                    count += 1
                # if we havent broken the while loop, keep increasing end to extend the subarray
                end += 1

            # once we have stopped the inner while loop, move to next index
            start += 1

        return count
