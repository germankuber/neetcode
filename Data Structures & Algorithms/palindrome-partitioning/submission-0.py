from typing import Counter, List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        results = []
        
        
        palindrome = []
        
        def backtracking(index: int):
            if index >= len(s):
                results.append(palindrome[:])
                return
        
            
            for index_2 in range(index, len(s)):
                word = s[index:index_2 + 1]
                
                if word == word[::-1]:
                    palindrome.append(word)
                    backtracking(index_2 + 1)
                    palindrome.pop()
                    
        
        backtracking(0)
        return results
            