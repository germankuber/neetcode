from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[str]]) -> int:
        row_size , col_size = len(grid), len(grid[0])
        
        total_islands = 0
        
        max_size = 0
        def dfs(x_position: int, y_position: int) -> int:
            
            if x_position >= 0 and x_position < row_size and y_position >= 0 and y_position < col_size and grid[x_position][y_position] == 1:
                grid[x_position][y_position] = 0
                return 1 + dfs(x_position - 1, y_position) + dfs(x_position + 1, y_position) +dfs(x_position, y_position - 1) + dfs(x_position, y_position + 1)
                
            else:
                return 0
            
        
        
        
        for x_position in range(row_size):
            for y_position in range(col_size):
                
                if grid[x_position][y_position] == 1:
                    total_islands += 1
                    max_counter = dfs(x_position, y_position)
                    if max_counter > max_size:
                        max_size = max_counter
        
        return max_size
        