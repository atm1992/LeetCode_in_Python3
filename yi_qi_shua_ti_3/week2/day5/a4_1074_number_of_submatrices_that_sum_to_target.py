# -*- coding: UTF-8 -*-
"""
title: 元素和为目标值的子矩阵数量
Given a matrix and a target, return the number of non-empty submatrices that sum to target.
A submatrix x1, y1, x2, y2 is the set of all cells matrix[x][y] with x1 <= x <= x2 and y1 <= y <= y2.
Two submatrices (x1, y1, x2, y2) and (x1', y1', x2', y2') are different if they have some coordinate that is different: for example, if x1 != x1'.


Example 1:
Input: matrix = [[0,1,0],[1,1,1],[0,1,0]], target = 0
Output: 4
Explanation: The four 1x1 submatrices that only contain 0.

Example 2:
Input: matrix = [[1,-1],[-1,1]], target = 0
Output: 5
Explanation: The two 1x2 submatrices, plus the two 2x1 submatrices, plus the 2x2 submatrix.

Example 3:
Input: matrix = [[904]], target = 0
Output: 0


Constraints:
1 <= matrix.length <= 100
1 <= matrix[0].length <= 100
-1000 <= matrix[i] <= 1000
-10^8 <= target <= 10^8
"""
from collections import defaultdict
from typing import List


class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        """前缀和 + 哈希表。参考 题560、题363
        枚举子矩阵的上下边界，并计算出该边界内每列的元素和，则将原问题转换成了如下的一维问题：
        给定一个整数数组和一个整数 target，计算出该数组中子数组和等于 target 的子数组个数。
        若行数大于列数，则可枚举矩阵的左右边界。总之，根据 m 和 n 的大小来细化枚举策略，从而将时间复杂度控制在 O(min(m,n)^2 * max(m,n) * 2)
        """
        res = 0
        m, n = len(matrix), len(matrix[0])
        # i 表示子矩阵的上边界为原矩阵的第几行，j 表示子矩阵的下边界为原矩阵的第几行。
        # i == j时，表示该子矩阵只有一行。i 不变的情况下，j下移时，可以复用之前的total计算结果，只需把新的第j行各个单元格数据加到对应列即可。
        for i in range(m):
            total = [0] * n
            for j in range(i, m):
                for col in range(n):
                    total[col] += matrix[j][col]
                pre_sum = 0
                pre2cnt = defaultdict(int)
                # 初始时，pre_sum为0的情况有一个，即 表示从0~col的前缀和恰好等于target
                pre2cnt[0] = 1
                for col in range(n):
                    pre_sum += total[col]
                    # 从前缀和等于pre_sum - target的那一列的下一列开始到当前列col，和正好为target
                    res += pre2cnt[pre_sum - target]
                    # 一定要先计算res，再把当前的pre_sum加到pre2cnt中，避免影响到pre_sum - target == pre_sum时候的结果，此时target == 0
                    pre2cnt[pre_sum] += 1
        return res


if __name__ == '__main__':
    print(Solution().numSubmatrixSumTarget(matrix=[[0, 1, 0], [1, 1, 1], [0, 1, 0]], target=0))
