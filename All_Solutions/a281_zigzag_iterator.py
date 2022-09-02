# -*- coding: UTF-8 -*-
"""
title: 锯齿迭代器
Given two vectors of integers v1 and v2, implement an iterator to return their elements alternately.
Implement the ZigzagIterator class:
    ZigzagIterator(List<int> v1, List<int> v2) initializes the object with the two vectors v1 and v2.
    boolean hasNext() returns true if the iterator still has elements, and false otherwise.
    int next() returns the current element of the iterator and moves the iterator to the next element.


Example 1:
Input: v1 = [1,2], v2 = [3,4,5,6]
Output: [1,3,2,4,5,6]
Explanation: By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,3,2,4,5,6].

Example 2:
Input: v1 = [1], v2 = []
Output: [1]

Example 3:
Input: v1 = [], v2 = [1]
Output: [1]


Constraints:
0 <= v1.length, v2.length <= 1000
1 <= v1.length + v2.length <= 2000
-2^31 <= v1[i], v2[i] <= 2^31 - 1

Follow up: What if you are given k vectors? How well can your code be extended to such cases?
Clarification for the follow-up question:
The "Zigzag" order is not clearly defined and is ambiguous for k > 2 cases. If "Zigzag" does not look right to you, replace "Zigzag" with "Cyclic".

Follow-up Example:
Input: v1 = [1,2,3], v2 = [4,5,6,7], v3 = [8,9]
Output: [1,4,8,2,5,9,3,6,7]
"""
from typing import List


class ZigzagIterator:
    """双指针"""

    def __init__(self, v1: List[int], v2: List[int]):
        # nums 是个二维数组
        self.nums = [v1, v2]
        self.max_col = max(len(v1), len(v2))
        self.col = 0
        # 因为 0 <= v1.length, v2.length，且 1 <= v1.length + v2.length，所以v1、v2至少有一个不为空
        # 若v1为空，则从第2行(row == 1)开始遍历
        self.row = 0 if v1 else 1

    def next(self) -> int:
        res = self.nums[self.row][self.col]
        while self.col < self.max_col:
            self.row += 1
            if self.row == len(self.nums):
                self.row = 0
                self.col += 1
            if self.col < len(self.nums[self.row]):
                break
        return res

    def hasNext(self) -> bool:
        return self.col < self.max_col


if __name__ == '__main__':
    obj = ZigzagIterator(v1=[1, 2], v2=[3, 4, 5, 6])
    while obj.hasNext():
        print(obj.next())
