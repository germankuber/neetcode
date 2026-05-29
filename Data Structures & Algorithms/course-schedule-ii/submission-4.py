from collections import defaultdict
from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        courses = defaultdict(dict)
        
        for course, dependency in prerequisites:
            # arista: dependency → course   (el prereq habilita al curso)
            courses[dependency][course] = True
        
        global_visited = set()
        results = []   # lista compartida, no se pasa por la recursión
        
        def dfs(current: int, visited: set) -> bool:
            if current in visited:
                return False    # ciclo
            if current in global_visited:
                return True
            
            visited.add(current)
            
            for nxt in courses[current]:
                if not dfs(nxt, visited):
                    return False
            
            visited.remove(current)
            global_visited.add(current)
            results.append(current)   # se cierra → va a la lista
            return True
        
        for item in range(numCourses):
            if not dfs(item, set()):
                return []
        
        return results[::-1]