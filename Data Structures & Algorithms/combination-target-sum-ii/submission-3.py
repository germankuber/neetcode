from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()                  # 1. ordenar: duplicados quedan juntos
        solutions = []
        combinations = []

        def process(index: int, total: int):
            if total == target:
                solutions.append(combinations[:])
                return
            
            if total > target or index >= len(candidates) :
                return
            
            
            current = candidates[index]
            
            combinations.append(current)
            
            process(index + 1, total + current)
            
            combinations.pop()
            
            new_index = index  + 1
            while new_index < len(candidates) and candidates[new_index] == current:
                new_index += 1
                
            process(new_index, total)

        process(0, 0)
        return solutions