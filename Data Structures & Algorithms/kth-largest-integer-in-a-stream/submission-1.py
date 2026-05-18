import heapq
from typing import List


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.mini_heap, self.k = nums, k
        
        heapq.heapify(self.mini_heap)
        
        while len(self.mini_heap) > self.k:
            heapq.heappop(self.mini_heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.mini_heap, val)
        
        if len(self.mini_heap) > self.k:
            heapq.heappop(self.mini_heap)
            
        return self.mini_heap[0]