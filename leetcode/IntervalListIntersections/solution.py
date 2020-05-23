class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        answer = []
        
        i = j = 0  
        while i < len(A) and j < len(B):
            # the max of the two current starting points
            # and the min of the two end point will be the intersection
            # as  long as start <= end
            start = max(A[i][0], B[j][0])
            end = min(A[i][1], B[j][1])
            
            if start <= end:
                answer.append([start,end])
                
            #determine which pointer to increment
            # if the A end point is less than B endpoint,
            # increment A since there could still be a h 
            # intersection wit the current B range
            if A[i][1] <= B[j][1]:
                i += 1
            else:
                j += 1
        
        return answer
