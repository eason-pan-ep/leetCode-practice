"""
LeetCode #209: Minimum Size Subarray Sum
Difficulty: Medium
Topics: Array, Binary Search, Sliding Window, Prefix Sum
Companies: Google, DoorDash, Microsoft, Meta
URL: https://leetcode.com/problems/minimum-size-subarray-sum/
"""

from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left, cur_sum = 0, 0
        n = len(nums)
        min_len = n + 1

        for right in range(n):
            cur_sum += nums[right]
            while cur_sum >= target:
                min_len = min(right - left + 1, min_len)
                cur_sum -= nums[left]
                left += 1
        
        return 0 if min_len == n + 1 else min_len