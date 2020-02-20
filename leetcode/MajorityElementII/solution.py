# utilize modified Boyer-Moore majority algorithm to generate two majority candidates,
# loop through to validate

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        majority = []
        threshold = math.floor(len(nums)/3)
        
        candidate = [0,0]
        voting = [0,0]
        
        for num in nums:
            if num == candidate[0]:
                #increase count of first candidate
                voting[0] += 1
            elif num == candidate[1]:
                #increase count of second candidate
                voting[1] += 1
            elif voting[0] == 0:
                candidate[0] = num
                voting[0] = 1
            elif voting[1] == 0:
                candidate[1] = num
                voting[1] = 1
            else:
                voting[0] -= 1
                voting[1] -= 1
                

        #check if either of the majorities found are above the threshold
            
        total_votes = [0,0]
                
        for num in nums:
            if num == candidate[0]:
                total_votes[0] += 1
            elif num == candidate[1]:
                total_votes[1] += 1
        
        if total_votes[0] > threshold:
            majority.append(candidate[0])
        if total_votes[1] > threshold:
            majority.append(candidate[1])
        
        return majority
