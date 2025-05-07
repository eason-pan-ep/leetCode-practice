"""
LeetCode #238: Product of Array Except Self
Difficulty: Medium
Topics: Array, Prefix Sum
URL: https://leetcode.com/problems/product-of-array-except-self/
"""

from typing import List
from collections import Counter

class Solution:
    def product_except_self_solution_1(self, nums: List[int]) -> List[int]:
        """Solution using division"""
        nums_count = Counter(nums)
        # if there is no zero, have a product of every element and each will be the all product / current num
        if 0 not in nums_count:
            total_product = nums[0]
            for i in range(1, len(nums)):
                total_product *= nums[i]
            res = []
            for i in range(len(nums)):
                res.append(total_product // nums[i])
            return res

        # if there are more than 1 zeros, all will be 0
        elif nums_count.get(0) > 1:
            return [0] * len(nums)

        # if there is only 1 zero, all zero, excpet the position with the 0
        else:
            res = [0] * len(nums)
            def calculate_non_zero_product(nums: List[int]) -> int:
                product = 1
                for num in nums:
                    if num != 0:
                        product *= num
                return product
            non_zero_product = calculate_non_zero_product(nums)
            for i in range(len(nums)):
                if nums[i] == 0:
                    res[i] = non_zero_product
                    break
            return res
    
    def product_except_self_solution_2(self, nums: List[int]) -> List[int]:
        """Solution using prefix and postfix product"""
        res = [1] * len(nums)
        # fill item-i with its prefix product
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        
        # multiply item-i with its postfix product
        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        
        return res