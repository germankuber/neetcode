from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        values = {}
        max = 0
        for num in nums:
            if num not in values:
                values[num] = True
            if num > max:
                max = num
                
        for value in range(1, max + 2):
            if value not in values:
                return value