"""
LeetCode #1: Two Sum
Difficulty: Easy
Topics: Array, Hash Table
URL: https://leetcode.com/problems/two-sum/
"""

from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    checked = {} # diff num, index

    for i in range(len(nums)):
        diff = target - nums[i]
        if diff in checked:
            return [i, checked[diff]]
        checked[nums[i]] = i