"""
LeetCode #128: Longest Consecutive Sequence
Difficulty: Medium
Topics: Array, Hash Table, Union Find
Companies: Google, Amazon, Bloomberg, Meta, Microsoft, IBM, TikTok
URL: https://leetcode.com/problems/longest-consecutive-sequence/
"""

from typing import List
import copy

class Solution:
    def longest_consecutive_solution_1(self, nums: List[int]) -> int:
        """Solution using sorting, O(nlogn)"""
        if not nums:
            return 0
        sorted_nums = copy.deepcopy(nums)
        sorted_nums.sort()
        count = 1
        cur_count = 1
        for i in range(len(sorted_nums)-1):
            if sorted_nums[i] + 1 == sorted_nums[i+1]:
                cur_count += 1
            elif sorted_nums[i] == sorted_nums[i+1]:
                continue
            else:
                count = max(cur_count, count)
                cur_count = 1
        count = max(cur_count, count)
        return count