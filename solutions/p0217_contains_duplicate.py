"""
LeetCode #217: Contains Duplicate
Difficulty: Easy
Topics: Array, Set
URL: https://leetcode.com/problems/contains-duplicate/
"""

from typing import List

def containsDuplicate(nums: List[int]) -> bool:
    check_set = set()
    for num in nums:
        if num in check_set:
            return True
        check_set.add(num)
    
    return False