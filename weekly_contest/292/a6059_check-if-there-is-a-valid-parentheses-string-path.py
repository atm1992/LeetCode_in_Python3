# -*- coding: UTF-8 -*-
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
