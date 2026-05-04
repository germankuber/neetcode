from typing import List


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        ROWS, COLS = len(matrix), len(matrix[0])
        self.matrix = [[0] * (COLS + 1) for _ in range(ROWS + 1)]
        
        
        for r in range(ROWS):
            prefix = 0                              # ← suma corrida de la fila actual
            for c in range(COLS):
                prefix += matrix[r][c]              # acumulo el valor en la fila
                above = self.matrix[r][c + 1]       # lo que ya está acumulado en la fila de arriba
                self.matrix[r + 1][c + 1] = prefix + above
        
                
                
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1, col1, row2, col2 = row1 + 1, col1 + 1, row2 + 1, col2 + 1
        
        total_square =  self.matrix[row2][col2]
        above =  self.matrix[row1 - 1][col2]
        left = self.matrix[row2][col1 - 1]
        extra = self.matrix[row1 - 1][col1 - 1]
        result = total_square - above - left + extra
        return result
            