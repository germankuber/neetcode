from typing import List
import math


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        answer = right

        while left <= right:
            mid = (left + right) // 2
            hours = self.total_hours(piles, mid)

            if hours <= h:
                answer = mid
                right = mid - 1
            else:
                left = mid + 1

        return answer

    def total_hours(self, piles: List[int], speed: int) -> int:
        hours = 0
        for p in piles:
            hours += math.ceil(p / speed)
        return hours