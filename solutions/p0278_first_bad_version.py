"""
LeetCode #278: First Bad Version
Difficulty: Easy
Topics: Binary Search, Interactive
URL: https://leetcode.com/problems/first-bad-version/
"""


# The isBadVersion API is already defined for you.
def isBadVersion(version: int) -> bool:
    pass  # This is a placeholder for the actual implementation.

##################################################################

class Solution:
    def firstBadVersion(self, n: int) -> int:
        if isBadVersion(1):
            return 1

        head, tail, bad = 1, n, -1

        while head <= tail:
            mid = (head + tail) // 2

            if isBadVersion(mid):
                bad = mid
                tail = mid - 1
            else:
                head = mid + 1
        return bad
        