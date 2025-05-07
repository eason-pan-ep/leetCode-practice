"""
LeetCode #23: Merge k Sorted Lists
Difficulty: Hard
Topics: Linked List, Divide and Conquer, Heap (Priority Queue), Merge Sort
URL: https://leetcode.com/problems/merge-k-sorted-lists/
"""

from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        n = len(lists)
        if n < 2:
            return lists[0]
        list_1 = lists[0]
        for i in range(1, n):
            list_2 = lists[i]
            list_1 = self.merge_two(list_1, list_2)
        return list_1


    def merge_two(self, list_1: ListNode, list_2: ListNode) -> Optional[ListNode]:
        res_head = ListNode()
        p_res = res_head
        p1, p2 = list_1, list_2
        
        while p1 and p2:
            if p1.val < p2.val:
                p_res.next = p1
                p1 = p1.next
            else:
                p_res.next = p2
                p2 = p2.next
            p_res = p_res.next
        
        if p1:
            p_res.next = p1
        if p2:
            p_res.next = p2
        
        return res_head.next
        