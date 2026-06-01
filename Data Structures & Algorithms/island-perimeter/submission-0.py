from typing import List

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        perimeter = 0
        
        DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # arriba, abajo, izq, der
        
        for row in range(rows):
            for col in range(cols):
                is_land = grid[row][col] == 1
                if not is_land:
                    continue
                
                for row_offset, col_offset in DIRECTIONS:
                    neighbor_row = row + row_offset
                    neighbor_col = col + col_offset
                    
                    is_out_of_bounds = (
                        neighbor_row < 0 or neighbor_row == rows or
                        neighbor_col < 0 or neighbor_col == cols
                    )
                    is_water = not is_out_of_bounds and grid[neighbor_row][neighbor_col] == 0
                    
                    if is_out_of_bounds or is_water:
                        perimeter += 1
        
        return perimeter