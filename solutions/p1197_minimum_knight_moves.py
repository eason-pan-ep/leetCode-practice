"""
LeetCode #1197: Minimum Knight Moves
Difficulty: Medium
Topics: Breadth-First Search, Graph
Companies: Amazon, Meta
URL: https://leetcode.com/problems/minimum-knight-moves/
"""

from collections import deque

class Solution:
    def min_knight_moves_solution_2(self, x: int, y: int) -> int:
        """BFS, time: O(n), space: O(n), moves to 8 directions, target maps to quadrant I"""
        directions = [(2, 1), (1, 2), (2, -1), (1, -2), (-2, 1), (-1, 2), (-2, -1), (-1, -2)]

        visited = set()
        steps = 0
        queue = deque()
        queue.append((0, 0))
        visited.add((0, 0))
        
        # map given position to only the quadrant I
        x_check = abs(x)
        y_check = abs(y)

        while queue:
            for _ in range(len(queue)):
                cur_x, cur_y = queue.popleft()
                if cur_x == x_check and cur_y == y_check:
                    return steps

                for direction in directions:
                    new_x = cur_x + direction[0]
                    new_y = cur_y + direction[1]
                    new_pos = (new_x, new_y)

                    # restriction will be one step away from quadrant I or one step away from goal pos
                    # otherwise, we would need extra steps only to move back to prev step
                    if new_pos not in visited and -2 <= new_x <= x_check + 2 and -2 <= new_y <= y_check + 2:
                        queue.append(new_pos)
                        visited.add(new_pos)
            
            steps += 1

    
    def min_knight_moves_solution_1(self, x: int, y: int) -> int:
        """BFS, time: O(n), space: O(n), moves to 8 directions, target is as given"""
        directions = [(2, 1), (1, 2), (2, -1), (1, -2), (-2, 1), (-1, 2), (-2, -1), (-1, -2)]

        visited = set()
        steps = 0
        queue = deque()
        queue.append((0, 0))
        visited.add((0, 0))

        while queue:
            for _ in range(len(queue)):
                cur_x, cur_y = queue.popleft()
                if cur_x == x and cur_y == y:
                    return steps

                for direction in directions:
                    new_x = cur_x + direction[0]
                    new_y = cur_y + direction[1]
                    new_pos = (new_x, new_y)

                    if new_pos not in visited:
                        queue.append(new_pos)
                        visited.add(new_pos)
            
            steps += 1