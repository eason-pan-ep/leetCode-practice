"""
LeetCode #15: 3Sum
Difficulty: Medium
Topics: Array, Two Pointers, Sorting
Companies: Amazon, Facebook, Google, Microsoft, Bloomberg, Adobe, Apple, Cisco, Oracle, Uber, Yahoo, Yelp
URL: https://leetcode.com/problems/3sum/
"""

from typing import List

class Solution:
    def three_sum_solution_1(self, nums: List[int]) -> List[List[int]]:
        """Brute force, time: O(n^3), space: O(n)"""
        n = len(nums)
        if n < 3:
            return []

        res = set()
        nums.sort()

        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    if nums[i] + nums[j] + nums[k] == 0:
                        temp = [nums[i], nums[j], nums[k]]
                        res.add(tuple(temp))
        
        return [list(i) for i in res]