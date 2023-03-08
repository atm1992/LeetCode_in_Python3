# -*- coding: UTF-8 -*-
"""
title: 切披萨的方案数
Given a rectangular pizza represented as a rows x cols matrix containing the following characters: 'A' (an apple) and '.' (empty cell) and given the integer k. You have to cut the pizza into k pieces using k-1 cuts. 
For each cut you choose the direction: vertical or horizontal, then you choose a cut position at the cell boundary and cut the pizza into two pieces. If you cut the pizza vertically, give the left part of the pizza to a person. If you cut the pizza horizontally, give the upper part of the pizza to a person. Give the last piece of pizza to the last person.
Return the number of ways of cutting the pizza such that each piece contains at least one apple. Since the answer can be a huge number, return this modulo 10^9 + 7.


Example 1:
Input: pizza = ["A..","AAA","..."], k = 3
Output: 3
Explanation: The figure above shows the three ways to cut the pizza. Note that pieces must contain at least one apple.

Example 2:
Input: pizza = ["A..","AA.","..."], k = 3
Output: 1

Example 3:
Input: pizza = ["A..","A..","..."], k = 1
Output: 1


Constraints:
1 <= rows, cols <= 50
rows == pizza.length
cols == pizza[i].length
1 <= k <= 10
pizza consists of characters 'A' and '.' only.
"""
from functools import lru_cache
from typing import List


class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        """动态规划计算后缀和，DFS + 记忆化 + 剪枝"""
        mod = 10 ** 9 + 7
        m, n = len(pizza), len(pizza[0])
        A_cnt = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                A_cnt[i][j] = A_cnt[i + 1][j] + A_cnt[i][j + 1] - A_cnt[i + 1][j + 1] + (1 if pizza[i][j] == 'A' else 0)

        @lru_cache(maxsize=None)
        def dfs(i: int, j: int, cuts: int) -> int:
            if cuts == 0:
                return 1
            res = 0
            # 统一先尝试横着切，无法再横着切了之后，再去竖着切。避免一会横着切、一会竖着切，造成方案重复
            # 因为每次执行都会先尝试横着切，所以为了避免重复计算，因此加上记忆化
            for x in range(i + 1, m):
                # 剪枝
                if A_cnt[i][j] > A_cnt[x][j] >= cuts:
                    res += dfs(x, j, cuts - 1)
            for y in range(j + 1, n):
                if A_cnt[i][j] > A_cnt[i][y] >= cuts:
                    res += dfs(i, y, cuts - 1)
            return res % mod

        return dfs(0, 0, k - 1)


if __name__ == '__main__':
    print(Solution().ways(pizza=["A..", "AAA", "..."], k=3))
