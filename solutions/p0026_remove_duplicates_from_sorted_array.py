"""
LeetCode #26: Remove Duplicates from Sorted Array
Difficulty: Easy
Topics: Array, Two Pointers
URL: https://leetcode.com/problems/remove-duplicates-from-sorted-array/
"""

from typing import List

class Solution:
    def remove_duplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return 1
        
        check, edit = 0, 0
        k = 1
        while check < len(nums):
            if nums[check] != nums[edit]:
                edit += 1
                nums[edit] = nums[check]
                k += 1
            check += 1
        
        return k