#Given an array A of positive lengths, return the largest perimeter of a triangle with non-zero area, formed from 3 of these lengths.
#
#If it is impossible to form any triangle of non-zero area, return 0




class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        # sort A decending
        A.sort(reverse=True)

        # the third side of a triangle must be less than
        # the other two sides added to themselves
        
        for i in range(len(A)-2):
            c = A[i]
            b = A[i+1]
            a = A[i+2]
            
            if c < b + a:
                return c + b + a
        
        return 0
            
