"""
LeetCode #219: Contains Duplicate II
Difficulty: Easy
Topics: Array, Hash Table, Sliding Window
Companies: Meta, Google, Amazon, Microsoft, Bloomberg, tcs
URL: https://leetcode.com/problems/contains-duplicate-ii/
"""

from typing import List

class Solution:
    def contains_nearby_duplicate_solution_2(self, nums: List[int], k: int) -> bool:
        """Sliding window, time: O(n), space: O(k)"""
        window = set()
        left = 0

        for right in range(len(nums)):
            if right - left > k:  # now at the window size
                window.remove(nums[left])
                left += 1
            if nums[right] in window:
                return True
            window.add(nums[right])

        return False
    
    
    def contains_nearby_duplicate_solution_1(self, nums: List[int], k: int) -> bool:
        """Brute force, time: O(n^2), space: O(1)"""
        n = len(nums)
        for left in range(n):
            for right in range(left + 1, min(n, left + k + 1)):
                if nums[left] == nums[right]:
                    return True
        return False