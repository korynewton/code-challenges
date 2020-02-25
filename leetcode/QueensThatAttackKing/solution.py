class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        #check north, northeast, east, southeast, south, southwest,west,northwest
        results = []
        directions = [[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1],[-1,0],[-1,1]]
        for direction in directions:
            x,y = king
            while 0<=x<=8 and 0<=y<=8:
                x += direction[0]
                y += direction[1]
                if [x,y] in queens:
                    results.append([x,y])
                    break
        return results
