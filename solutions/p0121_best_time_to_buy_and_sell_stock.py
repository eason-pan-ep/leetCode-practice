"""
LeetCode #121: Best Time to Buy and Sell Stock
Difficulty: Easy
Topics: Array, Dynamic Programming, Sliding Window
Companies: Meta, Amazon, Google, Microsoft, Uber, Bloomberg, Apple, Visa, Zoox, Oracle
URL: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
"""

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """solution to use two pointers, O(n) time and O(1) space"""
        if not prices:
            return 0
        if len(prices) == 1:
            return 0
        if len(prices) == 2:
            return max(0, prices[1] - prices[0])
        
        max_profit = 0
        buy = 0

        for sell in range(len(prices)):
            profit = prices[sell] - prices[buy]
            max_profit = max(max_profit, profit)
            
            while buy <= sell and prices[sell] < prices[buy]:
                buy += 1
        
        return max_profit