from typing import List, Optional

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        courses = {}
        
        
        for course, dependency in prerequisites:
            if course not in courses:
                courses[course] = {}
                
            if dependency not in courses:
                courses[dependency] = {}
                
            courses[course][dependency] = True
            
            
            
        global_visited = set()
        
        results = []
        
        def dfs(current: int, visited: set) -> Optional[List[int]]:
            
            if current in visited:
                return None
            
            if current in global_visited:
                return []
            
            
            visited.add(current)
            
            results = []
            
            dependencies = courses.get(current, {})
            
            for dependency in dependencies:
                result = dfs(dependency, visited)
                
                if result is None:
                    return None
                
                results.extend(result)
                
            
            visited.remove(current)
            
            results.append(current)
            
            global_visited.add(current)
            
            return results
        
        
        for item in range(numCourses):
            result = dfs(item, set())
            if result is None:
                return  []
            results.extend(result)
            
        return results
            