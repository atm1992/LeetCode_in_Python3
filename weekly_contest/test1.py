# -*- coding: UTF-8 -*-
from functools import reduce
from typing import List


class Solution:
    def maxTrailingZeros(self, grid: List[List[int]]) -> int:
        """统计2、5的个数"""
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                val = grid[i][j]
                cnt_2, cnt_5 = 0, 0
                tmp = val
                while tmp % 2 == 0:
                    cnt_2 += 1
                    tmp //= 2
                tmp = val
                if tmp % 5 == 0:
                    cnt_5 += 1
                    tmp //= 5
                grid[i][j] = (cnt_2, cnt_5)

        def sum_(a: tuple, b: tuple) -> tuple:
            return a[0] + b[0], a[1] + b[1]

        res = 0
        for i in range(m):
            for j in range(n):
                val = grid[i][j]
                left = reduce(sum_, grid[i][:j]) if j > 0 else (0, 0)
                right = reduce(sum_, grid[i][j + 1:]) if j + 1 < m else (0, 0)
                top = reduce(sum_, [grid[k][j] for k in range(i)]) if i > 0 else (0, 0)
                bottom = reduce(sum_, [grid[k][j] for k in range(i + 1, m)]) if i + 1 < m else (0, 0)
                l2t = reduce(sum_, [left, val, top])
                r2t = reduce(sum_, [right, val, top])
                l2b = reduce(sum_, [left, val, bottom])
                r2b = reduce(sum_, [right, val, bottom])
                res = max(res, max(min(l2t), min(r2t), min(l2b), min(r2b)))
        return res


if __name__ == '__main__':
    print(Solution().maxTrailingZeros(grid=[[4, 3, 2], [7, 6, 1], [8, 8, 8]]))
