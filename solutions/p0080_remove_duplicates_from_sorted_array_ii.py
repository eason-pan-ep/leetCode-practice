"""
LeetCode #80: Remove Duplicates from Sorted Array II
Difficulty: Medium
Topics: Array, Two Pointers
Companies: Google, Amazon, Meta
URL: https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/
"""

from typing import List
from collections import Counter

class Solution:
    def remove_duplicates_solution_1(self, nums: List[int]) -> int:
        """Solution to use hash map, O(n) time and O(n) space"""
        n = len(nums)
        if n <= 2:
            return n
        
        count = Counter(nums)
        i = 0
        for num in count:
            nums[i] = num
            i += 1
            count[num] -= 1
            if count[num] >= 1:
                nums[i] = num
                i += 1
        
        return i