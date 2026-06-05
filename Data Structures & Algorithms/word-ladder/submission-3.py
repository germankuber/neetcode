from collections import defaultdict, deque
from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        patterns: defaultdict[str, list[str]] = defaultdict(list)

        for word in wordList:
            
            for index in range(len(word)):
                key = word[:index] + "*" + word[index + 1 :]
                patterns[key].append(word)
                
                
        
        def get_neighbors(word: str) -> list[str]:
            result = []
            for index in range(len(word)):
                key = word[:index] + "*" + word[index + 1 :]
                
                for items in patterns[key]:
                    result.append(items)
                
                patterns[key] = []
                
            return result
        
        
        
        queue = deque([(beginWord, 1)])
        
        
        visited = { beginWord }
        
        while queue:
            
            word, index = queue.popleft()
            
            if word == endWord:
                return index
            
            
            for neighbor  in get_neighbors(word):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, index + 1))
        
        
        
        return 0