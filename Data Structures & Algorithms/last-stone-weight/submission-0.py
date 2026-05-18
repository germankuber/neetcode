import heapq
from typing import List

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-n for n in stones]
        heapq.heapify(max_heap)
        
        while len(max_heap) > 1:
            first = -heapq.heappop(max_heap)   # el más grande
            second = -heapq.heappop(max_heap)  # el segundo más grande
            
            if first != second:
                heapq.heappush(max_heap, -(first - second))
        
        return -max_heap[0] if max_heap else 0