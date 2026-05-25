from collections import deque
from typing import List, Set, Tuple, Deque
Cell = Tuple[int, int]  # alias para (fila, columna)
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        total_rows: int = len(heights)
        total_cols: int = len(heights[0])

        

        pacific_queue: Deque[Cell] = deque()
        atlantic_queue: Deque[Cell] = deque()
        reaches_pacific: Set[Cell] = set()
        reaches_atlantic: Set[Cell] = set()

        for row in range(total_rows):
            pacific_queue.append((row, 0))                 # borde izquierdo → Pacífico
            reaches_pacific.add((row, 0))
            atlantic_queue.append((row, total_cols - 1))   # borde derecho → Atlántico
            reaches_atlantic.add((row, total_cols - 1))

        for col in range(total_cols):
            pacific_queue.append((0, col))                 # borde superior → Pacífico
            reaches_pacific.add((0, col))
            atlantic_queue.append((total_rows - 1, col))   # borde inferior → Atlántico
            reaches_atlantic.add((total_rows - 1, col))

        def flood_from_ocean(queue: Deque[Cell], reached_cells: Set[Cell]) -> None:
            while queue:
                row, col = queue.popleft()
                current_height: int = heights[row][col]
                for row_offset, col_offset in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    neighbor_row: int = row + row_offset
                    neighbor_col: int = col + col_offset

                    is_inside_grid: bool = (
                        0 <= neighbor_row < total_rows
                        and 0 <= neighbor_col < total_cols
                    )
                    if not is_inside_grid:
                        continue
                    if (neighbor_row, neighbor_col) in reached_cells:
                        continue
                    # Vamos del mar hacia adentro: solo subimos o quedamos igual
                    if heights[neighbor_row][neighbor_col] < current_height:
                        continue

                    reached_cells.add((neighbor_row, neighbor_col))
                    queue.append((neighbor_row, neighbor_col))

        flood_from_ocean(pacific_queue, reaches_pacific)
        flood_from_ocean(atlantic_queue, reaches_atlantic)

        # La respuesta: celdas alcanzadas por AMBOS océanos
        result: List[List[int]] = []
        for row in range(total_rows):
            for col in range(total_cols):
                if (row, col) in reaches_pacific and (row, col) in reaches_atlantic:
                    result.append([row, col])
        return result