"""
LeetCode #374: Guess Number Higher or Lower
Difficulty: Easy
Topics: Binary Search, Interactive
URL: https://leetcode.com/problems/guess-number-higher-or-lower/
"""


# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
PICKED_NUM = 5

def guess(num: int) -> int:
    if num > PICKED_NUM:
        return -1
    elif num < PICKED_NUM:
        return 1
    else:
        return 0
    
####################################################################

class Solution:
    def guessNumber(self, n: int) -> int:
        low, high = 1, n

        while low <= high:
            mid = (low + high) // 2

            guess_res = guess(mid)
            if guess_res < 0:
                high = mid - 1
            elif guess_res > 0:
                low = mid + 1
            else:
                return mid
        
        return -1