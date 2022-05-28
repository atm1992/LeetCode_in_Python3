# -*- coding: UTF-8 -*-
"""
title: 矩阵中最大的矩形
给定一个由 0 和 1 组成的矩阵 matrix ，找出只包含 1 的最大矩形，并返回其面积。
注意：此题 matrix 输入格式为一维 01 字符串数组。


示例 1：
输入：matrix = ["10100","10111","11111","10010"]
输出：6
解释：最大矩形如上图所示。

示例 2：
输入：matrix = []
输出：0

示例 3：
输入：matrix = ["0"]
输出：0

示例 4：
输入：matrix = ["1"]
输出：1

示例 5：
输入：matrix = ["00"]
输出：0


提示：
rows == matrix.length
cols == matrix[0].length
0 <= row, cols <= 200
matrix[i][j] 为 '0' 或 '1'
"""
from typing import List


class Solution:
    def maximalRectangle(self, matrix: List[str]) -> int:
        """暴力"""
        if not matrix or not matrix[0]:
            return 0
        m, n = len(matrix), len(matrix[0])
        res = 0
        # 统计每个元素左侧有多少个连续的'1'
        new_matrix = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '0':
                    continue
                width = new_matrix[i][j - 1] + 1 if j > 0 else 1
                new_matrix[i][j] = width
                # 计算以(i,j)为右下角的矩形的最大面积
                area = width * 1
                for k in range(i - 1, -1, -1):
                    if new_matrix[k][j] == 0:
                        break
                    width = min(width, new_matrix[k][j])
                    area = max(area, width * (i - k + 1))
                res = max(res, area)
        return res

    def maximalRectangle_2(self, matrix: List[str]) -> int:
        """单调栈"""
        if not matrix or not matrix[0]:
            return 0
        m, n = len(matrix), len(matrix[0])
        # 统计每个元素左侧有多少个连续的'1'
        new_matrix = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    new_matrix[i][j] = new_matrix[i][j - 1] + 1 if j > 0 else 1
        res = 0
        # 对每一列，都使用一次单调栈
        for j in range(n):
            stack = []
            # up[i] 表示new_matrix[i]上侧最后一个小于其width值的元素下标j；down[i] 表示new_matrix[i]下侧第一个小于其width值的元素下标j。
            up, down = [-1] * m, [m] * m
            for i in range(m):
                width = new_matrix[i][j]
                # 参考offer2题39中的方法二，一次遍历同时更新上下边界下标
                while stack and stack[-1][0] >= width:
                    _, idx = stack.pop()
                    down[idx] = i
                if stack:
                    up[i] = stack[-1][1]
                stack.append((width, i))
            area = max(new_matrix[k][j] * (down[k] - up[k] - 1) for k in range(m))
            res = max(res, area)
        return res


if __name__ == '__main__':
    print(Solution().maximalRectangle(["10100", "10111", "11111", "10010"]))
