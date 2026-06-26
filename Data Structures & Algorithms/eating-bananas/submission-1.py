from typing import List
import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        answer = right
        while left <= right:
            mid = (left + right) // 2
            hours = sum(math.ceil(p / mid) for p in piles)
            if hours <= h:        # mid is fast enough
                answer = mid
                right = mid - 1   # try slower
            else:
                left = mid + 1    # need faster
        return answer