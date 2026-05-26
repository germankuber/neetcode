from collections import defaultdict
from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        courses = defaultdict(dict)
        
        for dependency, course in prerequisites:
            courses[course][dependency] = True
            courses[dependency]
        
        
        global_visited = set()
            
        def dfs(current_course: int, visited : set) -> bool:
            if current_course in visited:
                return False
            
            if current_course in global_visited:
                return True
            
            visited.add(current_course)
            
            current_to_iterate = courses.get(current_course, {})
            
            for item in current_to_iterate.keys():
                if not dfs(item, visited):
                    return False
                
            
            visited.remove(current_course)
            global_visited.add(current_course)
            
            return True
        
        
        for course in range(numCourses):
            if not dfs(course, set()):
                return False
            
        return True
        