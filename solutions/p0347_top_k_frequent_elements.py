"""
LeetCode #347: Top K Frequent Elements
Difficulty: Medium
Topics: Array, Hash Table, Heap, Bucket Sort, Counting, Quickselect
URL: https://leetcode.com/problems/top-k-frequent-elements/
"""

from typing import List
from collections import Counter, defaultdict

class Solution:
    def topKFrequent_1(self, nums: List[int], k: int) -> List[int]:
        """Time complexity: O(nlogn)"""
        checks = {}
        for num in nums:
            current_num_check = checks.get(num, 0)
            checks[num] = current_num_check + 1

        sorted_dict = dict(sorted(checks.items(), key=lambda item: item[1], reverse=True))

        res = []
        count = 0

        for key, _ in sorted_dict.items():
            if count < k:
                res.append(key)
                count += 1
            else:
                break

        return res
    
    
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """Time complexity: O(n)"""
        # count freq of each num
        num_freq = Counter(nums)

        # convert to freq: [nums]
        freq_num_dict = defaultdict(list)
        for num, freq in num_freq.items():
            freq_num_dict[freq].append(num)
        
        max_freq = len(nums)
        res = []
        for freq_check in range(max_freq, 0, -1):
            if freq_check in freq_num_dict:
                res += freq_num_dict[freq_check]
                if len(res) >= k:
                    break
        
        return res
