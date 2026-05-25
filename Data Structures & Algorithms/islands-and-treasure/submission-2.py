from collections import deque
from typing import List


class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        
        to_process = deque()
        visited = set()
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 0:
                    to_process.append((row, col))
                    visited.add((row, col))
        
        
        def add_place(row:int, col:int):
            in_limits = 0 <= row < ROWS and 0 <= col < COLS
            if not in_limits:
                return
            if (row, col) in visited or grid[row][col] == -1:
                return
            visited.add((row, col))
            to_process.append((row, col))
            
        distance = 0        
        while to_process:
            
            for _ in range(len(to_process)):
                x_address, y_address = to_process.popleft()
                grid[x_address][y_address] = distance
                add_place(x_address + 1, y_address )
                add_place(x_address - 1, y_address)
                add_place(x_address, y_address + 1)
                add_place(x_address, y_address - 1)
            
            distance += 1