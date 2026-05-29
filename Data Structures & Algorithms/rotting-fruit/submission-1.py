from collections import deque
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        ROWS, COLS = len(grid), len(grid[0])
        
        fruit_to_process = deque()
        fresh = 0
        for row in range(ROWS):
            for col in range(COLS):
                current = grid[row][col]
                if current == 2:
                    fruit_to_process.append((row, col))
                    
                if current == 1:
                    fresh += 1
                    
                    
        
        
        def process_fruit(row:int, col:int):
            nonlocal fresh
            if row < 0 or row >= ROWS or col < 0 or col >= COLS:
                return
            
            current = grid[row][col]
            
            if current == 1:
                grid[row][col]= 2 
                fruit_to_process.append((row, col))
                fresh -= 1
        
        
        counter = 0
        while fruit_to_process and fresh > 0:
            
            for _ in range(len(fruit_to_process)):
                row, col = fruit_to_process.popleft()
                process_fruit(row + 1, col)
                process_fruit(row - 1, col)
                process_fruit(row, col + 1)
                process_fruit(row, col - 1)
            counter += 1
                
        return counter if fresh == 0 else -1
    