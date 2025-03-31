"""
LeetCode #1197: Minimum Knight Moves
Difficulty: Medium
Topics: Breadth-First Search, Graph
Companies: Amazon, Meta
URL: https://leetcode.com/problems/minimum-knight-moves/
"""


class Solution:
    def minKnightMoves_solution_1(self, x: int, y: int) -> int:
        """BFS, time: O(n), space: O(n), moves to 8 directions, target is as given"""
        directions = [(2, 1), (1, 2), (2, -1), (1, -2), (-2, 1), (-1, 2), (-2, -1), (-1, -2)]

        visited = set()
        steps = 0
        queue = [(0, 0)]

        while queue:
            for _ in range(len(queue)):
                cur_x, cur_y = queue.pop(0)
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