"""
LeetCode #242: Valid Anagram
Difficulty: Easy
Topics: Hash Table, String, Sorting
Companies: Google, Bloomberg, Meta, Microsoft, Amazon, Oracle, Affirm, Capgemini, Apple, Infosys, EPAM Systems, Cognizant
URL: https://leetcode.com/problems/valid-anagram/
"""
def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    
    checks = {}

    for i in range(len(s)):
        check_current_s = checks.get(s[i], 0)
        checks[s[i]] = check_current_s + 1

        check_current_t = checks.get(t[i], 0)
        checks[t[i]] = check_current_t - 1

    
    for key, value in checks.items():
        if value != 0:
            return False
    
    return True