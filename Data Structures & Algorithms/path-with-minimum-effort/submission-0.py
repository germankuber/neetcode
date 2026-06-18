import heapq
from typing import List


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
    
        ROWS, COLS = len(heights), len(heights[0])
        
        
        min_heap = [(0, 0, 0)]
        
        visited = set()
        
        
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        
        
        while min_heap:
            
            distance , row, col = heapq.heappop(min_heap)
            
            if (row, col) in visited:
                continue
            
            
            visited.add((row, col))
            
            
            if (row, col) == (ROWS - 1, COLS - 1):
                return distance
            
            
            for row_add, col_add in directions:
                
                new_row, new_col = row + row_add, col + col_add
                
                
                if new_row < 0 or new_col < 0 or new_row == ROWS or new_col == COLS or (new_row, new_col) in visited:
                    continue
                
                new_max_distance = max(distance ,abs(heights[row][col] - heights[new_row][new_col]))
                heapq.heappush(min_heap, (new_max_distance, new_row, new_col))