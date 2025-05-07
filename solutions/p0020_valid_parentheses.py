"""
LeetCode #20: Valid Parentheses
Difficulty: Easy
Topics: String, Stack
Companies: Amazon, Meta, LinkedIn, Google, Bloomberg, AT&T, Microsoft, Oracle, Walmart Labs, TikTok
URL: https://leetcode.com/problems/valid-parentheses/
"""

from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        if not s or (len(s) % 2 != 0):
            return False
        
        stack = deque()
        first_half = {'(', '[', '{'}
        second_half = {')': '(', ']': '[', '}': '{'}

        for char in s:
            if char in first_half:
                stack.append(char)
            elif char in second_half:
                try:
                    last_element = stack.pop()
                except IndexError:
                    return False
                
                if last_element != second_half[char]:
                    return False
        
        return len(stack) == 0