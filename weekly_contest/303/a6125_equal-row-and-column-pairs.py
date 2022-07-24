# -*- coding: UTF-8 -*-
"""
title: 相等行列对
Given a 0-indexed n x n integer matrix grid, return the number of pairs (Ri, Cj) such that row Ri and column Cj are equal.
A row and column pair is considered equal if they contain the same elements in the same order (i.e. an equal array).


Example 1:
Input: grid = [[3,2,1],[1,7,6],[2,7,7]]
Output: 1
Explanation: There is 1 equal row and column pair:
- (Row 2, Column 1): [2,7,7]

Example 2:
Input: grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
Output: 3
Explanation: There are 3 equal row and column pairs:
- (Row 0, Column 0): [3,1,2,2]
- (Row 2, Column 2): [2,4,2,2]
- (Row 3, Column 2): [2,4,2,2]


Constraints:
n == grid.length == grid[i].length
1 <= n <= 200
1 <= grid[i][j] <= 10^5
"""
from collections import defaultdict
from typing import List


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        """哈希表"""
        n = len(grid)
        row2cnt = defaultdict(int)
        for row in grid:
            row2cnt[','.join(map(str, row))] += 1
        res = 0
        for j in range(n):
            tmp = []
            for i in range(n):
                tmp.append(str(grid[i][j]))
            res += row2cnt[','.join(tmp)]
        return res


if __name__ == '__main__':
    print(Solution().equalPairs(grid=[[11, 1], [1, 11]]))
