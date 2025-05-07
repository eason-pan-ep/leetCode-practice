"""
LeetCode #3: Longest Substring Without Repeating Characters
Difficulty: Medium
Topics: Hash Table, String, Sliding Window
URL: https://leetcode.com/problems/longest-substring-without-repeating-characters/
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, max_len = 0, 0
        cur_chars = set()
        n = len(s)

        for right in range(n):
            cur_char = s[right]
            while cur_char in cur_chars:
                cur_chars.remove(s[left])
                left += 1
            cur_chars.add(cur_char)
            max_len = max(right - left + 1, max_len)
        
        return max_len