from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        results = []
        def backtrack(current: str, open_count: int, close_count: int):
            if open_count == n and close_count == n:
                results.append(current)
                

            can_open = open_count < n
            
            can_close =  close_count < open_count

            if can_open:
                backtrack(current + "(", open_count + 1, close_count)

            if can_close:
                backtrack(current + ")", open_count, close_count + 1)
            
        
        
        
        backtrack("", 0, 0)
        
        return results