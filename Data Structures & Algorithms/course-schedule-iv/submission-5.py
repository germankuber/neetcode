from typing import List
from collections import defaultdict


class Solution:
    def checkIfPrerequisite(
        self,
        numCourses: int,
        prerequisites: List[List[int]],
        queries: List[List[int]],
    ) -> List[bool]:
        subject_pre_req: dict[int, List[int]] = defaultdict(list)
        
        
        for dependency, course  in prerequisites:
            subject_pre_req[course].append(dependency)
            
            
        direct_dependencies : dict[int, set[int]] = {}
        
        
        def iterate(course: int) -> set[int]:
            if course in direct_dependencies:
                return direct_dependencies[course]

            results: set[int] = set()
            
            direct_dependencies[course] = results
            
            for dependency in subject_pre_req[course]:
                
                result = iterate(dependency)
                
                for item in result:
                    results.add(item)
                
            results.add(course)
            
            return results
        
        
        
        for course in range(numCourses):
            iterate(course)

        results: List[bool] = []

        for course, dependency in queries:
            pre_req_of_dependency = direct_dependencies[dependency]
            is_pre_req = course in pre_req_of_dependency
            results.append(is_pre_req)

        return results
