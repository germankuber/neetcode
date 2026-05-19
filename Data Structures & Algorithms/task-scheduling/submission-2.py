import heapq
from collections import Counter, deque
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        freq = Counter(tasks)
        
        tasks_freq = [-n for n in freq.values()]
        
        heapq.heapify(tasks_freq)
        
        waiting_room = deque()
        
        cycle = 0
        while len(waiting_room) > 0 or len(tasks_freq) > 0:
            cycle += 1
            if len(waiting_room) > 0:
                if cycle - waiting_room[0][1] > n:
                    task_to_process, _ = waiting_room.popleft()
                    heapq.heappush(tasks_freq, - task_to_process)
                    
                    
            if len(tasks_freq) > 0:
                task_to_process = -heapq.heappop(tasks_freq)
                task_to_process -= 1
                
                if task_to_process > 0:
                    waiting_room.append((task_to_process, cycle))
        
            
        return cycle

