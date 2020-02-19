#Boyer-Moore majority vote algorithm:
#Initialize an element m and a counter i with i = 0
#For each element x of the input sequence:
#If i = 0, then assign m = x and i = 1
#else if m = x, then assign i = i + 1
#else assign i = i − 1
#Return m



class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        answer = None
        
        for num in nums:
            if count == 0:
                answer = num
            count += 1 if answer == num else -1
        return answer
