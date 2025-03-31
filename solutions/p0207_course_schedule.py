"""
LeetCode #207: Course Schedule
Difficulty: Medium
Topics: Depth-First Search, Breadth-First Search, Graph, Topological Sort
Companies: Amazon, Meta, Google, TikTok, Microsoft, Oracle, Paypal, Swiggy, Cruise
URL: https://leetcode.com/problems/course-schedule/
"""

from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # put all know prereq info to an adjacency list
        check_map = { i:[] for i in range(numCourses)}
        for course, prereq in prerequisites:
            check_map[course].append(prereq)
        
        # run dfs and check all nodes
        visiting = set()

        def dfs(course: int) -> bool:
            if course in visiting:  # a loop
                return False
            
            # all prereq for this course has been taken or doesn't have prereq
            if len(check_map[course]) == 0:  
                return True
            
            visiting.add(course)
            for crs in check_map[course]:
                if not dfs(crs):
                    return False
            visiting.remove(course)
            check_map[course] = []
            return True
        
        # run through every courses
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True