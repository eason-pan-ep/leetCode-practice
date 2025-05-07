"""
LeetCode #424: Longest Repeating Character Replacement
Difficulty: Medium
Topics: Hash Table, String, Sliding Window
URL: https://leetcode.com/problems/longest-repeating-character-replacement/
"""

class Solution:
    def character_replacement_solution_2(self, s: str, k: int) -> int:
        """
        O(n) time complexity, O(m) space complexity, 
        where m is the number of unique characters in s and n is the length of s.
        """
        count = {}
        highest_freq = 0
        max_len = 0
        left = 0

        for right in range(len(s)):
            count[s[right]] = 1 + count.get(s[right], 0)
            highest_freq = max(highest_freq, count[s[right]])


            while (right - left + 1) - highest_freq > k:  # when characters need replacement are more than the limit
                count[s[left]] -= 1
                left += 1

            max_len = max(right - left + 1, max_len)
        
        return max_len
    
    
    def character_replacement_solution_1(self, s: str, k: int) -> int:
        """
        O(m*n) time complexity, O(n) space complexity, 
        where m is the number of unique characters in s and n is the length of s.
        """
        chars = set(s)
        max_len = 0

        for c in chars:
            count = left = 0
            for right in range(len(s)):
                if s[right] == c:
                    count += 1

                while (right - left + 1) - count > k:  # when characters need replacement are more than the limit
                    if s[left] == c:
                        count -= 1
                    left += 1

                max_len = max(right - left + 1, max_len)
        
        return max_len