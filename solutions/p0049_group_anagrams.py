"""
LeetCode #49: Group Anagrams
Difficulty: Medium
Topics: Array, Hash Table, String
Companies: Amazon, Google, Meta, Microsoft, Oracle, Apple, Goldman Sachs, Nvidia, Zoho, Affirm
URL: https://leetcode.com/problems/group-anagrams/
"""
from typing import List

def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    checks = {}

    for cur_str in strs:
        count = [0] * 26

        for c in cur_str:
            count[ord(c) - ord('a')] += 1
        
        cur_count_str = str(count)
        if cur_count_str in checks:
            checks[cur_count_str].append(cur_str)
        else:
            checks[cur_count_str] = [cur_str]
    
    res = []
    for _, value in checks.items():
        res.append(value)
    
    return res