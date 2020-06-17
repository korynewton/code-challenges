class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        #create matrix
        matrix = [[0]*m for i in range(n)]
        
        #loop through indices
        for idx in indices:
            row = idx[0]
            col = idx[1]
            
            #increment row and column appropriately
            for i in range(m):
                matrix[row][i] += 1
            for i in range(n):
                matrix[i][col] += 1
            
        #count the number of odd values
        count = 0
        for i in range(n):
            for j in range(m):
                num = matrix[i][j]
                if num % 2 != 0:
                    count += 1
        return count
