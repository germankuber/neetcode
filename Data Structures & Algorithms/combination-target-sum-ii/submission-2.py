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
            if total > target or index >= len(candidates):
                return

            current = candidates[index]

            # RAMA A: uso current (una sola vez -> index + 1)
            combinations.append(current)
            process(index + 1, total + current)
            combinations.pop()

            # RAMA B: NO uso current -> salteo TODAS sus copias
            next_index = index + 1
            while next_index < len(candidates) and candidates[next_index] == current:
                next_index += 1
            process(next_index, total)

        process(0, 0)
        return solutions