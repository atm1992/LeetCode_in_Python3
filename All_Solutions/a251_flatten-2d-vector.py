# -*- coding: UTF-8 -*-
"""
title: 展开二维向量
Design an iterator to flatten a 2D vector. It should support the next and hasNext operations.
Implement the Vector2D class:
    Vector2D(int[][] vec) initializes the object with the 2D vector vec.
    next() returns the next element from the 2D vector and moves the pointer one step forward. You may assume that all the calls to next are valid.
    hasNext() returns true if there are still some elements in the vector, and false otherwise.


Example 1:
Input
["Vector2D", "next", "next", "next", "hasNext", "hasNext", "next", "hasNext"]
[[[[1, 2], [3], [4]]], [], [], [], [], [], [], []]
Output
[null, 1, 2, 3, true, true, 4, false]
Explanation
Vector2D vector2D = new Vector2D([[1, 2], [3], [4]]);
vector2D.next();    // return 1
vector2D.next();    // return 2
vector2D.next();    // return 3
vector2D.hasNext(); // return True
vector2D.hasNext(); // return True
vector2D.next();    // return 4
vector2D.hasNext(); // return False


Constraints:
0 <= vec.length <= 200
0 <= vec[i].length <= 500
-500 <= vec[i][j] <= 500
At most 10^5 calls will be made to next and hasNext.

Follow up: As an added challenge, try to code it using only iterators in C++ or iterators in Java.
"""
from typing import List


class Vector2D:

    def __init__(self, vec: List[List[int]]):
        self.nums = []
        for item in vec:
            self.nums.extend(item)

    def next(self) -> int:
        return self.nums.pop(0)

    def hasNext(self) -> bool:
        return bool(self.nums)


class Vector2D_2:

    def __init__(self, vec: List[List[int]]):
        self.nums = []
        for item in vec:
            self.nums.extend(item)
        self.idx = -1
        self.size = len(self.nums)

    def next(self) -> int:
        self.idx += 1
        return self.nums[self.idx]

    def hasNext(self) -> bool:
        return self.idx < self.size - 1


class Vector2D_3:
    """上述两个方法不好，迭代器的主要目的之一就是最小化辅助空间的使用。我们应尽可能利用现有的数据结构。
    在某些情况下，如果要遍历的数据量太大，那么是无法直接放入内存的。
    并且不建议修改输入集合，迭代器只是用来遍历数据的，而不能去修改原始数据。另外，如果原始数据很大，但只需遍历前几个数，
    那么构造函数就会浪费大量时间和空间！
    双指针。使用两个变量outer、inner分别指向外层数组和内层数组，直接在输入数据上遍历
    """

    def __init__(self, vec: List[List[int]]):
        self.vector = vec
        self.outer = 0
        self.inner = 0
        self.size = len(self.vector)

    def go_to_next_outer(self):
        # 只有当inner走到头了，才会移动到下一个outer，并且下一个outer不是空数组。如果是空数组的话，outer会继续往后移
        # inner没有走到当前所在子数组的头时，go_to_next_outer不会执行任何操作
        while self.outer < self.size and self.inner == len(self.vector[self.outer]):
            self.outer += 1
            self.inner = 0

    def next(self) -> int:
        self.go_to_next_outer()
        res = self.vector[self.outer][self.inner]
        self.inner += 1
        return res

    def hasNext(self) -> bool:
        self.go_to_next_outer()
        return self.outer < self.size

# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(vec)
# param_1 = obj.next()
# param_2 = obj.hasNext()
