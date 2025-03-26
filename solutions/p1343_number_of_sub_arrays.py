"""
LeetCode #1343: Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold
Difficulty: Medium
Topics: Array, Sliding Window
Companies: Amazon
URL: https://leetcode.com/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/
"""

from typing import List

class Solution:
    def num_of_sub_arrays_solution_1(self, arr: List[int], k: int, threshold: int) -> int:
        """Sliding window, time: O(n), space: O(1), using right end to move the window"""
        total, cur_sum = 0, 0
        check_threshold = threshold * k  # avoiding divison calculation later

        for right in range(len(arr)):
            cur_sum += arr[right]  # add the element at the right end
            if right >= k - 1:  # keep going until reaching the given window size
                if cur_sum >= check_threshold:
                    total += 1
                # move window forward
                left = right - k + 1
                cur_sum -= arr[left]
        
        return total
