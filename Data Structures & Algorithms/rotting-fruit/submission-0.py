from collections import deque
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        fruits = deque()
        fresh = 0

        # Encolar podridas y contar frescas
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 2:
                    fruits.append((row, col))
                elif grid[row][col] == 1:
                    fresh += 1

        def add_fruit(row, col):
            if row < 0 or row >= ROWS or col < 0 or col >= COLS:
                return
            if grid[row][col] != 1:   # solo contagiamos frescas
                return
            grid[row][col] = 2        # se vuelve podrida (esto evita re-visitar)
            fruits.append((row, col))
            nonlocal fresh
            fresh -= 1

        minutes = 0
        while fruits and fresh > 0:
            for _ in range(len(fruits)):
                row, col = fruits.popleft()
                add_fruit(row + 1, col)
                add_fruit(row - 1, col)
                add_fruit(row, col + 1)
                add_fruit(row, col - 1)
            minutes += 1

        return minutes if fresh == 0 else -1