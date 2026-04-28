from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [[False] * 9 for _ in range(9)]
        columns = [[False] * 9 for _ in range(9)]
        quad = [[False] * 9 for _ in range(9)]
        
        for row_index, row in enumerate(board):

            current_row_quad = row_index // 3
            
            for col_index, value in enumerate(row):
                quad_index = self.get_quad_index(col_index, row_index)  
                current_col_quad = col_index // 3
                
                if value != ".":
                    if not rows[row_index][int(value) - 1]:
                        rows[row_index][int(value) - 1] = True
                    else:
                        return False
                    if not columns[col_index][int(value) - 1]:
                        columns[col_index][int(value) - 1] = True
                    else:
                        return False
                    # quad_index = self.get_quad_index(col_index, row_index)
                    if not quad[quad_index][int(value) - 1]:
                        quad[quad_index][int(value) - 1] = True
                    else:
                        return False
                
                
        # print(rows)
        return True
    
    def get_quad_index(self, col_index:int, row_index:int)-> int:
        quad = int((row_index / 3)) * 3 + int(col_index / 3)
        return  quad
