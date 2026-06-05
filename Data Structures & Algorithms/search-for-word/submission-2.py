from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        visited = set()

        def backtracking(row: int, col: int, word_index: int) -> bool:
            if word_index == len(word):
                return True
            if row < 0 or row >= ROWS or col < 0 or col >= COLS:
                return False
            
            if (row, col) in visited:
                return False
            
            
            
            
            current_letter =  board[row][col]
            letter_to_compare = word[word_index]
            
            if current_letter != letter_to_compare:
                return False
            
            
            visited.add((row, col))
            
            result =(
                backtracking(row + 1, col, word_index + 1) or
                backtracking(row - 1, col, word_index + 1) or
                backtracking(row, col + 1, word_index + 1) or
                backtracking(row, col - 1, word_index + 1)
            )
            
            visited.remove((row, col))
            return result
            
            
        
        
        for row in range(ROWS):
            for col in range(COLS):
                if backtracking(row, col, 0):
                    return True
        
        return False