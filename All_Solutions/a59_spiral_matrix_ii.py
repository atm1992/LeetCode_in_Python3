# -*- coding: UTF-8 -*-
"""
title: 螺旋矩阵 II
Given a positive integer n, generate an n x n matrix filled with elements from 1 to n^2 in spiral order.


Example 1:
Input: n = 3
Output: [[1,2,3],[8,9,4],[7,6,5]]

Example 2:
Input: n = 1
Output: [[1]]


Constraints:
1 <= n <= 20
"""
from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        """模拟螺旋矩阵的路径。当路径的长度达到矩阵中的元素总数时，路径结束。"""
        res = [[0] * n for _ in range(n)]
        # 分别代表4个方向：向右(只加col)、向下(只加row)、向左(只减col)、向上(只减row)
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        direction_idx = 0
        row = col = 0
        for i in range(1, n * n + 1):
            res[row][col] = i
            next_row, next_col = row + directions[direction_idx][0], col + directions[direction_idx][1]
            if not (0 <= next_row < n) or not (0 <= next_col < n) or res[next_row][next_col]:
                direction_idx = (direction_idx + 1) % 4
            row, col = row + directions[direction_idx][0], col + directions[direction_idx][1]
        return res

    def generateMatrix_2(self, n: int) -> List[List[int]]:
        """按层模拟螺旋矩阵的路径。将螺旋矩阵看做若干层，首先填入最外层的元素，其次填入次外层的元素，……，最后填入最内层的元素。
        [[1, 1, 1, 1, 1, 1],
         [1, 2, 2, 2, 2, 1],
         [1, 2, 3, 3, 2, 1],
         [1, 2, 3, 3, 2, 1],
         [1, 2, 2, 2, 2, 1],
         [1, 1, 1, 1, 1, 1]]
         对于每层，从左上方开始顺时针填入当前层的所有元素。左上角(top,left)、右上角(top,right)、右下角(bottom,right)、左下角(bottom,left)。
         一、(top,left) ——> (top,right)
         二、若top + 1 <= bottom，则(top + 1,right) ——> (bottom,right)
         三、若right - 1 >= left，则(bottom,right - 1) ——> (bottom,left)
         四、若bottom - 1 >= top + 1，则(bottom - 1,left) ——> (top + 1,left)
         填完当前层所有元素后，将 left 和 top 分别加 1，将 right 和 bottom 分别减 1，进入下一层继续填入元素，直到top > bottom or left > right。
        """
        res = [[0] * n for _ in range(n)]
        num = 1
        top, bottom, left, right = 0, n - 1, 0, n - 1
        while top <= bottom and left <= right:
            for i in range(left, right + 1):
                res[top][i] = num
                num += 1
            if top + 1 > bottom:
                break
            for i in range(top + 1, bottom + 1):
                res[i][right] = num
                num += 1
            if right - 1 < left:
                break
            for i in range(right - 1, left - 1, -1):
                res[bottom][i] = num
                num += 1
            if bottom - 1 < top + 1:
                break
            for i in range(bottom - 1, top, -1):
                res[i][left] = num
                num += 1
            top, bottom, left, right = top + 1, bottom - 1, left + 1, right - 1
        return res


if __name__ == '__main__':
    print(Solution().generateMatrix(3))
