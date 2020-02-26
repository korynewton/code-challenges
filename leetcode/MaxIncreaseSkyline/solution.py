class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        total = 0
        row_max = []
        col_max = []
        
        for i in range(len(grid)):
            row_max.append(max(grid[i]))
        
        for j in range(len(grid[0])):
            temp_max = 0
            for k in range(len(grid)):
                if grid[k][j]>temp_max:
                    temp_max = grid[k][j]
            col_max.append(temp_max)
                    
        
        for l in range(len(grid)):
            for m in range(len(grid[0])):
                current = grid[l][m]
                new_val = min(row_max[l],col_max[m])
                total += new_val - current
        
        return total 
