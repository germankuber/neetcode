from typing import List


class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        solutions = []
        iterations = []

        def process(index: int, total: int):
            # ÉXITO: la suma da justo el target
            if total == target:
                solutions.append(iterations[:])
                return

            # FRACASO: me pasé del target, o ya no quedan números
            if total > target or index >= len(nums):
                return

            current_element = nums[index]

            # RAMA A: incluyo current_element Y LO PUEDO REUSAR
            # (por eso paso 'index', no 'index + 1')
            iterations.append(current_element)
            process(index, total + current_element)
            iterations.pop()

            # RAMA B: descarto current_element para siempre
            # (avanzo a index + 1)
            process(index + 1, total)

        process(0, 0)
        return solutions