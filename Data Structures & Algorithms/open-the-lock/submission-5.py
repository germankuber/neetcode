from collections import deque
from typing import List

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        dead = set(deadends)
        
        if "0000" in dead:
            return -1
        if target == "0000":
            return 0
        
        queue = deque(["0000"])
        visited = {"0000"}
        steps = 0
        
        while queue:
            steps += 1
            for _ in range(len(queue)):
                current = queue.popleft()
                
                for i in range(4):
                    digit = int(current[i])
                    for delta in (-1, 1):
                        new_digit = (digit + delta) % 10
                        new_combo = current[:i] + str(new_digit) + current[i+1:]
                        
                        if new_combo == target:
                            return steps
                        
                        if new_combo not in dead and new_combo not in visited:
                            visited.add(new_combo)
                            queue.append(new_combo)
        
        return -1