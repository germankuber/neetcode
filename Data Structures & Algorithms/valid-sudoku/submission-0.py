from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [[False] * 9 for _ in range(9)]
        columns = [[False] * 9 for _ in range(9)]
        quad = [[False] * 9 for _ in range(9)]
        
        for row_index, row in enumerate(board):
            
            for col_index, value in enumerate(row):
            
                if value != ".":
                    if not rows[row_index][int(value) - 1]:
                        rows[row_index][int(value) - 1] = True
                    else:
                        return False
                    if not columns[col_index][int(value) - 1]:
                        columns[col_index][int(value) - 1] = True
                    else:
                        return False
                    if not quad[self.get_quad_index(col_index, row_index)][int(value) - 1]:
                        quad[self.get_quad_index(col_index, row_index)][int(value) - 1] = True
                    else:
                        return False
                    
                
        # print(rows)
        return True
    
    def get_quad_index(self, col_index:int, row_index:int)-> int:
        current_row_quad = row_index // 3
        current_col_quad = col_index // 3
        if current_col_quad == 0 and current_row_quad == 0:
            return 0
        if current_col_quad == 0 and current_row_quad == 1:
            return 1
        if current_col_quad == 0 and current_row_quad == 2:
            return 2
        if current_col_quad == 1 and current_row_quad == 0:
            return 3
        if current_col_quad == 1 and current_row_quad == 1:
            return 4
        if current_col_quad == 1 and current_row_quad == 2:
            return 5
        if current_col_quad == 2 and current_row_quad == 0:
            return 6
        if current_col_quad == 2 and current_row_quad == 1:
            return 7
        if current_col_quad == 2 and current_row_quad == 2:
            return 8
        