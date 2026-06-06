from typing import List

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # crítico: agrupa duplicados para poder saltarlos
        result = []
        used = [False] * len(nums)
        path = []

        def backtrack():
            if len(path) == len(nums):
                result.append(path[:])
                return

            for i in range(len(nums)):
                if used[i]:
                    continue
                # Skip duplicates: si el anterior igual no fue usado en esta rama,
                # ya exploramos esta posibilidad antes
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue

                used[i] = True
                path.append(nums[i])
                backtrack()
                path.pop()
                used[i] = False

        backtrack()
        return result