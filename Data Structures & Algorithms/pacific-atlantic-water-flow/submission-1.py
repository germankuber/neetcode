from collections import deque
from typing import List

Cell = tuple[int, int]

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        total_rows: int = len(heights)
        total_cols: int = len(heights[0])

        reaches_pacific: set[Cell] = set()
        reaches_atlantic: set[Cell] = set()

        def flood_from_ocean(row: int, col: int, reached_cells: set[Cell], previous_height: int) -> None:
            is_inside_grid = 0 <= row < total_rows and 0 <= col < total_cols
            if not is_inside_grid:
                return
            if (row, col) in reached_cells:
                return
            # Vamos del mar hacia adentro: solo subimos o quedamos igual
            if heights[row][col] < previous_height:
                return

            reached_cells.add((row, col))
            current_height = heights[row][col]
            flood_from_ocean(row + 1, col, reached_cells, current_height)
            flood_from_ocean(row - 1, col, reached_cells, current_height)
            flood_from_ocean(row, col + 1, reached_cells, current_height)
            flood_from_ocean(row, col - 1, reached_cells, current_height)

        # Bordes Pacífico (arriba e izquierda) y Atlántico (abajo y derecha)
        for col in range(total_cols):
            flood_from_ocean(0, col, reaches_pacific, heights[0][col])
            flood_from_ocean(total_rows - 1, col, reaches_atlantic, heights[total_rows - 1][col])

        for row in range(total_rows):
            flood_from_ocean(row, 0, reaches_pacific, heights[row][0])
            flood_from_ocean(row, total_cols - 1, reaches_atlantic, heights[row][total_cols - 1])

        result: List[List[int]] = []
        for row in range(total_rows):
            for col in range(total_cols):
                if (row, col) in reaches_pacific and (row, col) in reaches_atlantic:
                    result.append([row, col])
        return result