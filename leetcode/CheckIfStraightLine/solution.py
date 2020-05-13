class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        [ starting_x, starting_y ] = coordinates[0]
        [ second_x, second_y ] = coordinates[1]
        
        starting_rise = (second_y - starting_y)
        starting_run = (second_x - starting_x)
                
        if starting_run == 0:
            return False
        else:
            starting_slope = starting_rise/starting_run
        
        for i in range(1, len(coordinates)-1):
            #check if slope remains the same
            [current_x, current_y] = coordinates[i]
            [next_x, next_y] = coordinates[i+1]
            
            rise = next_y - current_y
            run = next_x - current_x
            
            if run == 0 or starting_slope != rise/run:
                return False
        
        
        return True
