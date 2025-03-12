"""
LeetCode #125: Valid Palindrome
Difficulty: Easy
Topics: Two Pointers, String
Companies: Meta, BCG, Apple, Amazon, Microsoft, Bloomberg, Google
URL: https://leetcode.com/problems/valid-palindrome/
"""

class Solution:
    def is_palindrome_solution_1(self, s: str) -> bool:
        """Solution using two pointers and string cleanup"""
        # Clean up string (remove non-letter characters and convert to all lowercase)
        cleanup_string = ''.join(char for char in s.lower() if char.isalpha() or char.isdigit())
        print(cleanup_string)

        # 2 pointers check head and tail and move towards the centre
        left, right = 0, len(cleanup_string) - 1

        while left < right:
            if cleanup_string[left] != cleanup_string[right]:
                return False
            left += 1
            right -= 1
        
        return True
