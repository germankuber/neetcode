from collections import defaultdict, deque
from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        # Construir patterns
        patterns = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i+1:]
                patterns[pattern].append(word)
        
        def get_neighbors(word):
            neighbors = []
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i+1:]
                neighbors.extend(patterns[pattern])
                patterns[pattern] = []         # ← clave para evitar TLE
            return neighbors
        
        # BFS
        queue = deque([(beginWord, 1)])
        visited = {beginWord}
        
        while queue:
            word, level = queue.popleft()
            
            if word == endWord:
                return level
            
            for neighbor in get_neighbors(word):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, level + 1))
        
        return 0