"""
LeetCode #15: 3Sum
Difficulty: Medium
Topics: Array, Two Pointers, Sorting
Companies: Amazon, Facebook, Google, Microsoft, Bloomberg, Adobe, Apple, Cisco, Oracle, Uber, Yahoo, Yelp
URL: https://leetcode.com/problems/3sum/
"""

from typing import List

class Solution:
    def three_sum_solution_2(self, nums: List[int]) -> List[List[int]]:
        """Two pointers, time: O(n^2), space: O(n)"""
        n = len(nums)
        if n < 3:
            return []

        res = []
        nums.sort()
        for index, num in enumerate(nums):
            # if the smallest is already greater than 0, there is no chance to sum up equals to 0
            if num > 0:
                break
            
            # the same num as the previous one, ans will be the same
            if index > 0 and num == nums[index-1]:
                continue
            
            left, right = index + 1, n - 1
            while left < right:
                cur_sum = num + nums[left] + nums[right]
                if cur_sum == 0:
                    res.append([num, nums[left], nums[right]])
                    left += 1
                    right -= 1
                    # skip the same left, meaning the same right will also be skipped
                    while nums[left] == nums[left-1] and left < right:
                        left += 1
                elif cur_sum > 0:
                    right -= 1
                else:
                    left += 1
            
        return res


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