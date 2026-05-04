from typing import List


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        result = 0
        cols_to_iterate = list(range(col1, col2 + 1))
        rows_to_iterate = list(range(row1, row2 + 1))
        for col_index in cols_to_iterate:
            for row_index in rows_to_iterate:
                result += self.matrix[row_index][col_index] 
        return result