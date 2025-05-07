"""
LeetCode #42: Trapping Rain Water
Difficulty: Hard
Topics: Array, Two Pointers, Stack, Dynamic Programming, Monotonic Stack
URL: https://leetcode.com/problems/trapping-rain-water/
"""

from typing import List

class Solution:
    def trap_solution_2(self, height: List[int]) -> int:
        """two pointers, time: O(n), space: O(1)"""
        n = len(height)
        if n == 0:
            return 0

        left, right = 0, n-1
        total, max_left, max_right = 0, height[left], height[right]

        while left < right:
            if max_left > max_right:
                right -= 1
                current = height[right]
                total += max(0, max_right - current)
                max_right = max(max_right, current)
            else:
                left += 1
                current = height[left]
                total += max(0, max_left - current)
                max_left = max(max_left, current)
        
        return total


    def trap_solution_1(self, height: List[int]) -> int:
        "time: O(n), space: O(n)"
        n = len(height)
        if n == 0:
            return 0

        max_left = [0] * n
        for i in range(1, n):
            max_left[i] = max(max_left[i-1], height[i-1])
        
        max_right = [0] * n
        for i in range(n-2, -1, -1):
            max_right[i] = max(max_right[i+1], height[i+1])
        
        min_height = []
        for i in range(n):
            min_height.append(min(max_left[i], max_right[i]))
        
        total = 0
        for i in range(n):
            cur_water = min_height[i] - height[i]
            total += max(0, cur_water)
        
        return total