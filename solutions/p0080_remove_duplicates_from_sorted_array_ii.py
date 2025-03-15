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
    def remove_duplicates_solution_3(self, nums: List[int]) -> int:
        """solution to use two pointers, O(n) time and O(1) space"""
        left, right = 0, 0

        while right < len(nums):
            if left < 2 or nums[right] != nums[left - 2]:
                nums[left] = nums[right]
                left += 1
            right += 1
        return left
    
    
    def remove_duplicates_solution_2(self, nums: List[int]) -> int:
        """solution to use two pointers, O(n) time and O(1) space"""
        n = len(nums)
        if n <= 2:
            return n
        
        left, right = 0, 0
        while right < len(nums):
            count = 1
            while (right + 1 < n) and (nums[right] == nums[right+1]):
                right += 1
                count += 1
            for i in range(min(2, count)):
                nums[left] = nums[right]
                left += 1
            right += 1
        return left


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