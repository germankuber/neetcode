from collections import defaultdict, deque
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        dependency_courses = defaultdict(list)
        
        courses_dependencies_count = defaultdict(int)
        
        for course, dependency in prerequisites:
            dependency_courses[dependency].append(course)
            courses_dependencies_count[course] += 1
            
            
            
        courses_to_iterate = deque()
        
        for num_course in range(numCourses):
            if courses_dependencies_count[num_course] == 0:
                courses_to_iterate.append(num_course)
                
                
        counter = 0
        
        result = []
        while courses_to_iterate:
            
            course_done = courses_to_iterate.popleft()
            result.append(course_done)
            counter += 1
            
            for course_to_do in dependency_courses[course_done]:
                
                courses_dependencies_count[course_to_do] -= 1
                
                if courses_dependencies_count[course_to_do] == 0:
                    courses_to_iterate.append(course_to_do)
        if counter != numCourses:
            return []
        return result
        