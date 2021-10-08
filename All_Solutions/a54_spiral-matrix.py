# -*- coding: UTF-8 -*-
"""
title: 螺旋矩阵
Given an m x n matrix, return all elements of the matrix in spiral order.


Example 1:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

Example 2:
Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]


Constraints:
m == matrix.length
n == matrix[i].length
1 <= m, n <= 10
-100 <= matrix[i][j] <= 100
"""
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """模拟螺旋矩阵的路径。当路径的长度达到矩阵中的元素总数时，路径结束。"""
        m, n = len(matrix), len(matrix[0])
        visited = [[False] * n for _ in range(m)]
        total = m * n
        res = []
        # 分别代表4个方向：向右(只加j)、向下(只加i)、向左(只减j)、向上(只减i)
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        direction_idx = 0
        i = j = 0
        for _ in range(total):
            # res append满total个元素，就可以退出for循环了
            res.append(matrix[i][j])
            visited[i][j] = True
            next_i, next_j = i + directions[direction_idx][0], j + directions[direction_idx][1]
            if next_i not in range(m) or next_j not in range(n) or visited[next_i][next_j]:
                direction_idx = (direction_idx + 1) % 4
            i += directions[direction_idx][0]
            j += directions[direction_idx][1]
        return res

    def spiralOrder_2(self, matrix: List[List[int]]) -> List[int]:
        """按层模拟螺旋矩阵的路径。将螺旋矩阵看做若干层，首先输出最外层的元素，其次输出次外层的元素，……，最后输出最内层的元素。
        [[1, 1, 1, 1, 1, 1, 1],
         [1, 2, 2, 2, 2, 2, 1],
         [1, 2, 3, 3, 3, 2, 1],
         [1, 2, 2, 2, 2, 2, 1],
         [1, 1, 1, 1, 1, 1, 1]]
         对于每层，从左上方开始顺时针遍历当前层的所有元素。左上角(top,left)、右上角(top,right)、右下角(bottom,right)、左下角(bottom,left)。
         一、(top,left) ——> (top,right)
         二、若top + 1 <= bottom，则(top + 1,right) ——> (bottom,right)
         三、若right - 1 >= left，则(bottom,right - 1) ——> (bottom,left)
         四、若bottom - 1 >= top + 1，则(bottom - 1,left) ——> (top + 1,left)
         遍历完当前层所有元素后，将 left 和 top 分别加 1，将 right 和 bottom 分别减 1，进入下一层继续遍历，直到top > bottom or left > right。
        """
        m, n = len(matrix), len(matrix[0])
        res = []
        top, bottom, left, right = 0, m - 1, 0, n - 1
        while top <= bottom and left <= right:
            for i in range(left, right + 1):
                res.append(matrix[top][i])
            if not top + 1 <= bottom:
                break
            for i in range(top + 1, bottom + 1):
                res.append(matrix[i][right])
            if not right - 1 >= left:
                break
            for i in range(right - 1, left - 1, -1):
                res.append(matrix[bottom][i])
            if not bottom - 1 >= top + 1:
                break
            for i in range(bottom - 1, top, -1):
                res.append(matrix[i][left])
            top, bottom, left, right = top + 1, bottom - 1, left + 1, right - 1
        return res

    def spiralOrder_3(self, matrix: List[List[int]]) -> List[int]:
        """削头 + 逆时针旋转90度"""
        res = []
        while matrix:
            # 削头（第一层）
            res += matrix.pop(0)
            # 将剩余部分逆时针旋转90度，等待下次削头
            matrix = list(zip(*matrix))[::-1]
        return res


if __name__ == '__main__':
    print(Solution().spiralOrder_3([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))
