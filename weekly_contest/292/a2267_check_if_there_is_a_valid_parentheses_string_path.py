# -*- coding: UTF-8 -*-
"""
title: 检查是否有合法括号字符串路径
A parentheses string is a non-empty string consisting only of '(' and ')'. It is valid if any of the following conditions is true:
    It is ().
    It can be written as AB (A concatenated with B), where A and B are valid parentheses strings.
    It can be written as (A), where A is a valid parentheses string.
You are given an m x n matrix of parentheses grid. A valid parentheses string path in the grid is a path satisfying all of the following conditions:
    The path starts from the upper left cell (0, 0).
    The path ends at the bottom-right cell (m - 1, n - 1).
    The path only ever moves down or right.
    The resulting parentheses string formed by the path is valid.
Return true if there exists a valid parentheses string path in the grid. Otherwise, return false.


Example 1:
Input: grid = [["(","(","("],[")","(",")"],["(","(",")"],["(","(",")"]]
Output: true
Explanation: The above diagram shows two possible paths that form valid parentheses strings.
The first path shown results in the valid parentheses string "()(())".
The second path shown results in the valid parentheses string "((()))".
Note that there may be other valid parentheses string paths.

Example 2:
Input: grid = [[")",")"],["(","("]]
Output: false
Explanation: The two possible paths form the parentheses strings "))(" and ")((". Since neither of them are valid parentheses strings, we return false.


Constraints:
m == grid.length
n == grid[i].length
1 <= m, n <= 100
grid[i][j] is either '(' or ')'.
"""
from functools import lru_cache
from typing import List


class Solution:
    def hasValidPath(self, grid: List[List[str]]) -> bool:
        """回溯 + 记忆化"""
        m, n = len(grid), len(grid[0])
        if grid[0][0] == ')' or grid[-1][-1] == '(':
            return False
        # 因为只能向下或向右走，所以从(0,0)到(m-1,n-1)的步数是固定的m+n-1。如果为奇数，那必然是不合法的
        if (m + n - 1) & 1:
            return False

        @lru_cache(maxsize=None)
        def dfs(i: int, j: int, cnt: int) -> bool:
            # 即使后面全部都是')'，也不可能合法
            if cnt > m - i + n - j - 1:
                return False
            ch = grid[i][j]
            cnt += 1 if ch == '(' else -1
            if cnt < 0:
                return False
            if i == m - 1 and j == n - 1:
                return cnt == 0
            res = False
            for x, y in [(i + 1, j), (i, j + 1)]:
                if x < m and y < n:
                    res |= dfs(x, y, cnt)
                    if res:
                        break
            cnt += -1 if ch == '(' else 1
            return res

        return dfs(0, 0, 0)


if __name__ == '__main__':
    print(Solution().hasValidPath(grid=[["(", "(", "("], [")", "(", ")"], ["(", "(", ")"], ["(", "(", ")"]]))
