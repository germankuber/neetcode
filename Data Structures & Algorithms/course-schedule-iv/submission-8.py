from collections import defaultdict
from typing import List


class Solution:
    def checkIfPrerequisite(
        self,
        numCourses: int,
        prerequisites: List[List[int]],
        queries: List[List[int]],
    ) -> List[bool]:
        
        graph  = defaultdict(list)
        
        for dependency, subject in prerequisites:
            
            graph[subject].append(dependency)
            graph[dependency]
            
        
        all_dependencies  = defaultdict(list)    
        def dfs(subject: int) -> set[int]:
            if subject in all_dependencies:
                return all_dependencies[subject]
            
            to_return = set()
            for dep in graph[subject]:
                results = dfs(dep)
                for result in results:
                    to_return.add(result)
            to_return.add(subject)
            
            all_dependencies[subject] = to_return   # ← cache antes del return
            return to_return
                
        
        
        
        
        
        for course in range(numCourses):
            dependencies = dfs(course)
            all_dependencies[course] = dependencies
            
            
            
        result = []
        
        for dependency, course in queries:
            if course in all_dependencies:
                if dependency in all_dependencies[course]:
                    result.append(True)
                else:
                    result.append(False)
            else:
                result.append(False)
            
        return result
        