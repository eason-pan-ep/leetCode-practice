"""
LeetCode #11: Container With Most Water
Difficulty: Medium
Topics: Array, Two Pointers, Greedy
Companies: Google, Amazon, Meta, Microsoft, Bloomberg, Goldman Sachs
URL: https://leetcode.com/problems/container-with-most-water/
"""

from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        if not height:
            return 0
        
        max_water = 0
        left, right = 0, len(height) - 1

        while left < right:
            left_height, right_height = height[left], height[right]
            width = right - left
            cur_water = min(left_height, right_height) * width
            max_water = max(max_water, cur_water)
            if left_height < right_height:
                left += 1
            else:
                right -= 1
        
        return max_water