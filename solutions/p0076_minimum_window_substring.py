"""
LeetCode #76: Minimum Window Substring
Difficulty: Hard
Topics: Hash Table, String, Sliding Window
URL: https://leetcode.com/problems/minimum-window-substring/
"""

class Solution:
    def min_window_solution_2(self, s: str, t: str) -> str:
        """Sliding Window Solution, time: O(n), space: O(n)"""
        if not s or not t or len(s) < len(t):
            return ""

        count_t = {}
        for c in t:
            count_t[c] = count_t.get(c, 0) + 1
        
        min_len = len(s) + 1
        res = [-1, -1]
        left = 0
        count_s = {}
        have, need = 0, len(count_t)

        for right in range(len(s)):
            cur_char = s[right]
            count_s[cur_char] = count_s.get(cur_char, 0) + 1
            if cur_char in count_t and count_t[cur_char] == count_s[cur_char]:
                have += 1

                while have == need:
                    cur_len = right - left + 1
                    if cur_len < min_len:
                        res = [left, right]
                        min_len = cur_len
                    
                    l_char = s[left]
                    count_s[l_char] -= 1
                    if l_char in count_t and count_s[l_char] < count_t[l_char]:
                        have -= 1
                    left += 1
        
        left, right = res
        return s[left:right+1] if min_len != len(s) + 1 else ""
    
    
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
        