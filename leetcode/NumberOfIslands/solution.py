class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if len(grid):
            # find upper bounds of rows/cols
            m, n = len(grid), len(grid[0])
        else:
            return 0

        count = 0

        # loop through grid
        for row in range(m):
            for col in range(n):
                # if not land, move to next location in grid
                if grid[row][col] == "0":
                    continue

                # location is a "1" on grid, set to "0" so that we dont count it again
                grid[row][col] = "0"

                # start a BFS queue for this location
                queue = [(row, col)]

                # find all neighboring "1"s while in a single while loop
                while queue:
                    i, j = queue.pop(0)

                    for x, y in (i+1, j), (i-1, j), (i, j-1), (i, j+1):
                        if 0 <= x < m and 0 <= y < n and grid[x][y] == "1":
                            grid[x][y] = "0"
                            queue.append((x, y))
                # after completing while loop that will represent a single island
                # increment count by 1
                count += 1
        return count
