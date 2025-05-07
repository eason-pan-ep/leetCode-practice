"""
LeetCode #155: Min Stack
Difficulty: Medium
Topics: Stack, Design
URL: https://leetcode.com/problems/min-stack/
"""

from collections import deque

class MinStack:

    def __init__(self):
        self.stack = deque()
        self.min_stack = deque()
        

    def push(self, val: int) -> None:
        # add to stack
        self.stack.append(val)

        # tracking the min value
        if (len(self.min_stack) == 0) or (self.min_stack[-1] > val):
            self.min_stack.append(val)
        else:
            self.min_stack.append(self.min_stack[-1])
        

    def pop(self) -> None:
        if len(self.stack) == 0:
            return
        
        self.stack.pop()
        self.min_stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min_stack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()