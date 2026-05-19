from cmath import sqrt
import heapq
from typing import List

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_values = []
        
        heapq.heapify(max_values)
        
        for x, y in points:
            
            distance = x * x + y * y
            
            if len(max_values) < k:
                heapq.heappush(max_values, (-distance, [x , y]))
            elif distance < -max_values[0][0]:
                heapq.heappushpop(max_values, (-distance, [x,y]))
                
        
        return [points for _, points in max_values]