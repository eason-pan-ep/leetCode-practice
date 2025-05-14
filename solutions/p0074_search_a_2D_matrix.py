"""
LeetCode #74: Search a 2D Matrix
Difficulty: Medium
Topics: Array, Binary Search, Matrix
URL: https://leetcode.com/problems/search-a-2d-matrix/
"""

from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        total_row, total_col = len(matrix), len(matrix[0])
        left, right, cur_row = 0, total_col - 1, 0

        while left <= right and cur_row < total_row:
            cur_left = matrix[cur_row][left]
            cur_right = matrix[cur_row][right]

            # cases need to go to next row
            if cur_right < target and right == total_col - 1: # at the end of a row
                cur_row += 1
                left, right = 0, total_col - 1
                continue
            
            # cases need to find the value in the row
            mid = (left + right) // 2
            cur_mid = matrix[cur_row][mid]
            if target > cur_mid:
                left = mid + 1
            elif target < cur_mid:
                right = mid - 1
            else:
                return True
        
        return False
