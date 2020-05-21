class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        #how many squares of all ones can be found
        #i.e squares with only 1 side (a single one),
        # squares with 2 sides (4 ones) etc, etc.
        
        rows = len(matrix)
        cols = len(matrix[0])
        
        dp_matrix = [[0 for i in range(cols)] for j in range(rows)]
        
        result = 0
        for i in range(rows):
            for j in range(cols):
                if i == 0 or j == 0:
                    dp_matrix[i][j] = matrix[i][j]
                elif matrix[i][j] == 1:
                    dp_matrix[i][j] = min(dp_matrix[i-1][j-1], dp_matrix[i-1][j], dp_matrix[i][j-1]) + 1
                result += dp_matrix[i][j]
                    
        return result
                    
        
        