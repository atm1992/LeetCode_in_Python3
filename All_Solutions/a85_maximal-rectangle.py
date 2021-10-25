# -*- coding: UTF-8 -*-
"""
title: 最大矩形
Given a rows x cols binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.


Example 1:
Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 6
Explanation: The maximal rectangle is shown in the above picture.

Example 2:
Input: matrix = []
Output: 0

Example 3:
Input: matrix = [["0"]]
Output: 0

Example 4:
Input: matrix = [["1"]]
Output: 1

Example 5:
Input: matrix = [["0","0"]]
Output: 0


Constraints:
rows == matrix.length
cols == matrix[i].length
0 <= row, cols <= 200
matrix[i][j] is '0' or '1'.
"""
from typing import List


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        """暴力破解"""
        if not matrix:
            return 0
        m, n = len(matrix), len(matrix[0])

        res = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '0':
                    continue
                # 先统计每个元素左侧有多少个元素为'1'，直接在原矩阵中修改。
                # 之所以回填str，因为matrix的数据类型为List[List[str]]，避免一部分元素为int，一部分为str
                int_val = int(matrix[i][j - 1]) + 1 if j > 0 else 1
                matrix[i][j] = str(int_val)

                # 计算以坐标(i,j)为右下角的矩形面积
                min_width = int_val
                area = min_width * 1
                for k in range(i - 1, -1, -1):
                    if matrix[k][j] == '0':
                        break
                    min_width = min(min_width, int(matrix[k][j]))
                    area = max(area, min_width * (i - k + 1))
                res = max(res, area)
        return res

    def maximalRectangle_2(self, matrix: List[List[str]]) -> int:
        """单调栈。以每个单元格左侧1的个数(宽度)为基准，分别向上下延伸，找到能以该宽度覆盖的所有单元格(即 高度)"""
        if not matrix:
            return 0
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            for j in range(1, n):
                if matrix[i][j] == '1':
                    matrix[i][j] = str(int(matrix[i][j - 1]) + 1)
        res = 0
        # 对每一列，都使用一次单调栈
        for j in range(n):
            up, down = [-1] * m, [m] * m
            # 单调栈。每个元素均为一个二元组(width[i], i)
            mono_stack = []
            for i in range(m):
                cur_width = int(matrix[i][j])
                while mono_stack and mono_stack[-1][0] >= cur_width:
                    down[mono_stack[-1][1]] = i
                    mono_stack.pop()
                if mono_stack:
                    up[i] = mono_stack[-1][1]
                mono_stack.append((cur_width, i))

            for i in range(m):
                cur_width = int(matrix[i][j])
                if cur_width == 0:
                    continue
                res = max(res, (down[i] - up[i] - 1) * cur_width)
        return res


if __name__ == '__main__':
    print(Solution().maximalRectangle(
        matrix=[["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"], ["1", "1", "1", "1", "1"],
                ["1", "0", "0", "1", "0"]]))
