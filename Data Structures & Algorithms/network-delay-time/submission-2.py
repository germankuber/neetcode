from collections import defaultdict
import heapq
from typing import List

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        adjacent_list = defaultdict(list)
        
        for source, target, time in times:
            adjacent_list[source].append((target, time))
            
            
        shortest_path = {}
        
        heap = [(0,k)]
        
        max_time = 0
        
        
        while heap:
            
            time, node = heapq.heappop(heap)
            
            if node in shortest_path:
                continue
            
            max_time = max(max_time, time)
            
            shortest_path[node] = time
            
            
            for nei, current_time in adjacent_list[node]:
                if nei not in shortest_path:
                    heapq.heappush(heap, (current_time + time, nei))
                    
        
        return max_time if len(shortest_path) == n else  -1