from typing import List


class NumMatrix:
    """
    2D Range Sum Query using a 2D prefix sum (summed-area table).

    Construction:  O(ROWS * COLS)
    Each query:    O(1)
    Space:         O(ROWS * COLS)
    """

    def __init__(self, matrix: List[List[int]]):
        ROWS, COLS = len(matrix), len(matrix[0])

        # Prefix matrix with one extra row and one extra column of zeros (padding).
        # This avoids special-casing the first row/column when building or querying:
        # any "out-of-bounds" lookup naturally lands on a zero cell.
        # self.matrix[r + 1][c + 1] will store the sum of the rectangle
        # from (0, 0) to (r, c) in the original matrix, both inclusive.
        self.matrix = [[0] * (COLS + 1) for _ in range(ROWS + 1)]

        for r in range(ROWS):
            # `prefix` is the running sum of the current row, from column 0 up to c.
            # It resets to 0 at the start of every row.
            prefix = 0
            for c in range(COLS):
                # Extend the row's running sum with the current cell.
                prefix += matrix[r][c]

                # `above` is the full prefix sum of the rectangle that ends
                # one row above, in the same column range [0..c].
                # Thanks to the padding row, this is also valid when r == 0
                # (it just reads a zero).
                above = self.matrix[r][c + 1]

                # The rectangle (0, 0) .. (r, c) decomposes into two disjoint parts:
                #   - everything above row r           -> `above`
                #   - the current row from col 0 to c  -> `prefix`
                # No overlap, so we just add them. No subtraction needed.
                self.matrix[r + 1][c + 1] = prefix + above

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # Shift all coordinates by +1 to account for the padding row/column.
        # After this, (row1, col1) and (row2, col2) refer to indices in self.matrix.
        row1, col1, row2, col2 = row1 + 1, col1 + 1, row2 + 1, col2 + 1

        # Inclusion-exclusion on the prefix matrix:
        #
        #   total_square  = sum of the rectangle (0, 0) .. (row2, col2)
        #   above         = sum of the strip above the target rectangle
        #   left          = sum of the strip to the left of the target rectangle
        #   extra         = the top-left corner that has been subtracted twice
        #
        # Visually:
        #
        #        col1-1     col2
        #          |          |
        #          v          v
        #     +----+----------+
        #     | E  |    A     |  <- row1-1
        #     +----+----------+
        #     |    |          |
        #     | L  |   X      |  <- row2 (X is the rectangle we want)
        #     |    |          |
        #     +----+----------+
        #
        # X = total - above - left + extra
        total_square = self.matrix[row2][col2]
        above        = self.matrix[row1 - 1][col2]
        left         = self.matrix[row2][col1 - 1]
        extra        = self.matrix[row1 - 1][col1 - 1]

        return total_square - above - left + extra