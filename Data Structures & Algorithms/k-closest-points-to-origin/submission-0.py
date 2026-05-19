from cmath import sqrt
import heapq
from typing import List

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        heapq.heapify(heap)
        
        for x,y in points:
            distance = x * x + y * y
            
            if len(heap) < k:
                heapq.heappush(heap, (-distance,[x , y]))
            else:
                heapq.heappushpop(heap, (-distance, [x , y]))
                
        
        return [x for _,x in heap]
