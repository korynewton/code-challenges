class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # keep track of the sum that is closest to target
        result = None
        closest_diff = None

        nums.sort()

        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l, r = i+1, len(nums)-1

            while l < r:
                if i > 0 and nums[i] == nums[i-1]:
                    continue

                sum = nums[i] + nums[l] + nums[r]
                diff = abs(sum - target)

                # if diff is 0, return the sum
                if not diff:
                    return sum
                elif result == None or diff < closest_diff:
                    result = sum
                    closest_diff = diff

                if sum < target:
                    l += 1
                else:
                    r -= 1

        return result
