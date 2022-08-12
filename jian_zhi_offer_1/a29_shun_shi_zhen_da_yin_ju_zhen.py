# -*- coding: UTF-8 -*-
"""
title: 顺时针打印矩阵
输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字。


示例 1：
输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
输出：[1,2,3,6,9,8,7,4,5]

示例 2：
输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
输出：[1,2,3,4,8,12,11,10,9,5,6,7]


限制：
0 <= matrix.length <= 100
0 <= matrix[i].length <= 100
"""
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """削顶 + 逆时针旋转90度"""
        res = []
        while matrix:
            res.extend(matrix.pop(0))
            matrix = list(zip(*matrix))[::-1]
        return res

    def spiralOrder_2(self, matrix: List[List[int]]) -> List[int]:
        """
        按层模拟
        从左到右：(top, left) ——> (top, right)
        若top + 1 <= bottom，则继续，否则遍历结束
        从上到下：(top + 1, right) ——> (bottom, right)
        若right - 1 >= left，则继续，否则遍历结束
        从右到左：(bottom, right - 1) ——> (bottom, left)
        若bottom - 1 >= top + 1，则继续，否则遍历结束
        从下到上：(bottom - 1, left) ——> (top + 1, left)
        之后，top += 1, left += 1, right -= 1, bottom -= 1，进入下一层继续遍历
        """
        res = []
        if not matrix or not matrix[0]:
            return res
        left, right, top, bottom = 0, len(matrix[0]) - 1, 0, len(matrix) - 1
        while left <= right:
            res.extend(matrix[top][left:right + 1])
            if not top + 1 <= bottom:
                break
            for row in range(top + 1, bottom + 1):
                res.append(matrix[row][right])
            if not right - 1 >= left:
                break
            res.extend(matrix[bottom][left:right][::-1])
            if not bottom - 1 >= top + 1:
                break
            for row in range(bottom - 1, top, -1):
                res.append(matrix[row][left])
            left, right, top, bottom = left + 1, right - 1, top + 1, bottom - 1
        return res


if __name__ == '__main__':
    print(Solution().spiralOrder_2([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))
