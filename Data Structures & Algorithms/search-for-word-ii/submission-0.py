from collections import defaultdict
from typing import List


class TreeNode:
    
    def __init__(self):
        self.children = defaultdict(TreeNode)
        self.is_word = False
        
    def add_word(self, word: str):
        current = self
        for letter in word:
            current = current.children[letter]
        
        current.is_word = True
                

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        ROWS, COLS = len(board), len(board[0])
        
        root = TreeNode()
        
        for word in words:
            root.add_word(word=word)
            
        result = set()
        visited = set()
        
        
        def dfs(row: int, col: int, node: TreeNode, word:str):
            if row < 0 or col < 0:
                return
            if row == ROWS or col == COLS:
                return
            if (row, col) in visited:
                return
            
            letter = board[row][col]
            
            if letter not in node.children:
                return
            
            visited.add((row, col))
            
            node = node.children[letter]
            word += letter
            
            if node.is_word:
                result.add(word)
            
            dfs(row + 1, col, node, word)
            dfs(row - 1, col, node, word)
            dfs(row, col + 1, node, word)
            dfs(row, col - 1, node, word)
            
            
            visited.remove((row, col))
            
        
        for row in range(ROWS):
            for col in range(COLS):
                dfs(row, col, root, "")
            
        return list(result)
        