from collections import defaultdict
from typing import List

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        
        for asteroid in asteroids:
            
            asteroid_alive = True
            
            while len(stack):
                top = stack[-1]
                if top > 0 and asteroid < 0:
                    if abs(asteroid) > abs(top):
                        stack.pop()
                        asteroid_alive = True
                    elif abs(asteroid) == abs(top):
                        stack.pop()
                        asteroid_alive = False
                        break
                    else:
                        asteroid_alive = False
                        break
                else:
                    break
                    
            
            if asteroid_alive:  
                stack.append(asteroid)    
        return stack