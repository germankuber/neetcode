import heapq
from collections import Counter, deque
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        executed_tasks = deque()
        heap = [-count for count in freq.values()]
        heapq.heapify(heap)

        cycle = 0

        while len(heap) > 0 or len(executed_tasks) > 0:
            cycle += 1

            if len(executed_tasks) > 0:
                if cycle - executed_tasks[0][1] > n:
                    task_to_execute = executed_tasks.popleft()
                    heapq.heappush(heap, -task_to_execute[0])

            if len(heap):
                task = -heapq.heappop(heap)
                task -= 1
                if task > 0:
                    executed_tasks.append((task, cycle))

        return cycle