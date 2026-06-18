from collections import defaultdict
import heapq
from typing import List

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        adjacent_list = defaultdict(list)
        
        for source, target, time in times:
            adjacent_list[source].append((target, time))
            
            
            
        shortest_path = {}
        
        
        to_iterate = [(0, k)]
        
        max_time = 0
        while to_iterate:
            
            weight, node = heapq.heappop(to_iterate)
            
            if node in shortest_path:
                continue
            
            
            max_time = max(max_time, weight)
            shortest_path[node] = weight
            
            
            for destination, time in adjacent_list[node]:
                if destination not in shortest_path:
                    
                    heapq.heappush(to_iterate,(weight + time, destination))
                    
        return max_time if len(shortest_path) == n else -1