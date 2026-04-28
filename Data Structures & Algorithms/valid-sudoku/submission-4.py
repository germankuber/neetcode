from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen_in_row = [[False] * 9 for _ in range(9)]
        seen_in_col = [[False] * 9 for _ in range(9)]
        seen_in_box = [[False] * 9 for _ in range(9)]

        for row in range(9):
            for col in range(9):
                cell = board[row][col]
                if cell == ".":
                    continue

                digit = int(cell) - 1
                box = (row // 3) * 3 + (col // 3)

                already_seen = (
                    seen_in_row[row][digit]
                    or seen_in_col[col][digit]
                    or seen_in_box[box][digit]
                )
                if already_seen:
                    return False

                seen_in_row[row][digit] = True
                seen_in_col[col][digit] = True
                seen_in_box[box][digit] = True

        return True