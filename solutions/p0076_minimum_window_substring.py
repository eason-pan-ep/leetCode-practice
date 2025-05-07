"""
LeetCode #76: Minimum Window Substring
Difficulty: Hard
Topics: Hash Table, String, Sliding Window
Companies: Meta, Snowflake, Amazon, LinkedIn, TickTok, Lyft, Google, Microsoft, Adobe, Uber
URL: https://leetcode.com/problems/minimum-window-substring/
"""

class Solution:
    def min_window_solution_1(self, s: str, t: str) -> str:
        """Brute Force Solution, time: O(n^2), space: O(n)"""
        if not s or not t or len(s) < len(t):
            return ""

        count_t = {}
        for c in t:
            count_t[c] = count_t.get(c, 0) + 1
        
        min_len = len(s) + 1
        res = [-1, -1]
        
        for left in range(len(s)):
            count_s = {}
            for right in range(left, len(s)):
                count_s[s[right]] = count_s.get(s[right], 0) + 1

                found_all = True
                for c in count_t:
                    if count_t[c] > count_s.get(c, 0):
                        found_all = False
                        break
                
                cur_len = right - left + 1
                if found_all and cur_len < min_len:
                    res = [left, right]
                    min_len = cur_len
        
        left, right = res
        if min_len != len(s) + 1:
            return s[left:right+1]
        
        return ""
        