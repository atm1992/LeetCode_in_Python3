# -*- coding: UTF-8 -*-
"""
title: 二维区域和检索 - 可变
Given a 2D matrix matrix, handle multiple queries of the following types:
    Update the value of a cell in matrix.
    Calculate the sum of the elements of matrix inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).
Implement the NumMatrix class:
    NumMatrix(int[][] matrix) Initializes the object with the integer matrix matrix.
    void update(int row, int col, int val) Updates the value of matrix[row][col] to be val.
    int sumRegion(int row1, int col1, int row2, int col2) Returns the sum of the elements of matrix inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).


Example 1:
Input
["NumMatrix", "sumRegion", "update", "sumRegion"]
[[[[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]], [2, 1, 4, 3], [3, 2, 2], [2, 1, 4, 3]]
Output
[null, 8, null, 10]
Explanation
NumMatrix numMatrix = new NumMatrix([[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]);
numMatrix.sumRegion(2, 1, 4, 3); // return 8 (i.e. sum of the left red rectangle)
numMatrix.update(3, 2, 2);       // matrix changes from left image to right image
numMatrix.sumRegion(2, 1, 4, 3); // return 10 (i.e. sum of the right red rectangle)


Constraints:
m == matrix.length
n == matrix[i].length
1 <= m, n <= 200
-10^5 <= matrix[i][j] <= 10^5
0 <= row < m
0 <= col < n
-10^5 <= val <= 10^5
0 <= row1 <= row2 < m
0 <= col1 <= col2 < n
At most 10^4 calls will be made to sumRegion and update.

解题思路：
对矩阵matrix中的每一行均构建一个 树状数组(Binary Indexed Tree) 或 线段树(Segment Tree)，从而将 二维区域和检索 问题转变为 一维区域和检索 问题。
一维区域和检索中 树状数组(Binary Indexed Tree) 和 线段树(Segment Tree) 的构建和检索可参见题307
"""
from typing import List


class BIT:
    """树状数组"""

    def low_bit(self, idx: int) -> int:
        return idx & -idx

    def __init__(self, nums: List[int]):
        bit = [0] + nums
        size = len(bit)
        # 树状数组的下标从1开始
        for i in range(1, size):
            # 因为每个节点都只有一个父节点，所以对于每个节点而言，只需执行一次将值累加到父节点上
            j = i + self.low_bit(i)
            if j < size:
                bit[j] += bit[i]
        self.nums = nums
        self.bit = bit
        self.bit_size = size

    def update(self, idx: int, val: int) -> None:
        delta = val - self.nums[idx]
        self.nums[idx] = val
        # 将原数组的下标转换为树状数组BIT的下标
        idx += 1
        # 从子节点向上更新
        while idx < self.bit_size:
            self.bit[idx] += delta
            idx += self.low_bit(idx)

    def preSum(self, idx: int) -> int:
        """基于BIT数组获取从0到idx(含)的前缀和"""
        res = 0
        while idx > 0:
            res += self.bit[idx]
            idx -= self.low_bit(idx)
        return res

    def sumRegion(self, start: int, end: int) -> int:
        """返回 [start, end] 闭区间的累加和"""
        # 将原数组的下标转换为树状数组BIT的下标
        start, end = start + 1, end + 1
        return self.preSum(end) - self.preSum(start - 1)


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        # 对原二维矩阵matrix中的每一行都构建一个树状数组
        bit_matrix = []
        for row in matrix:
            bit_matrix.append(BIT(row))
        self.bit_matrix = bit_matrix

    def update(self, row: int, col: int, val: int) -> None:
        self.bit_matrix[row].update(col, val)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        res = 0
        for row in range(row1, row2 + 1):
            res += self.bit_matrix[row].sumRegion(col1, col2)
        return res


class ST:
    def __init__(self, nums: List[int]):
        n = len(nums)
        st = [0] * n + nums
        # 线段树的下标也是从1开始
        for i in range(n - 1, 0, -1):
            st[i] = st[2 * i] + st[2 * i + 1]
        self.st = st
        self.n = n

    def update(self, idx: int, val: int) -> None:
        # 将原数组的下标转换为线段树ST的下标
        idx += self.n
        delta = val - self.st[idx]
        # 从叶节点向上更新到根节点st[1]
        while idx > 0:
            self.st[idx] += delta
            idx >>= 1

    def sumRegion(self, start: int, end: int) -> int:
        res = 0
        # 将原数组的下标转换为线段树ST的下标
        start, end = start + self.n, end + self.n
        while start <= end:
            # 若左边界为右子节点，则先向右走一步，否则直接向上走一步
            if start & 1:
                res += self.st[start]
                start += 1
            # 若右边界为左子节点，则先向左走一步，否则直接向上走一步
            if not end & 1:
                res += self.st[end]
                end -= 1
            # start, end 都向上走一步
            start, end = start >> 1, end >> 1
        return res


class NumMatrix2:

    def __init__(self, matrix: List[List[int]]):
        # 对原二维矩阵matrix中的每一行都构建一个线段树
        st_matrix = []
        for row in matrix:
            st_matrix.append(ST(row))
        self.st_matrix = st_matrix

    def update(self, row: int, col: int, val: int) -> None:
        self.st_matrix[row].update(col, val)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        res = 0
        for row in range(row1, row2 + 1):
            res += self.st_matrix[row].sumRegion(col1, col2)
        return res


if __name__ == '__main__':
    obj = NumMatrix2([[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]])
    print(obj.sumRegion(2, 1, 4, 3))
    print(obj.update(3, 2, 2))
    print(obj.sumRegion(2, 1, 4, 3))
