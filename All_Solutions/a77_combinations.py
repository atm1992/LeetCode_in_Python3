# -*- coding: UTF-8 -*-
"""
title: 组合
Given two integers n and k, return all possible combinations of k numbers out of the range [1, n].
You may return the answer in any order.


Example 1:
Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]

Example 2:
Input: n = 1, k = 1
Output: [[1]]


Constraints:
1 <= n <= 20
1 <= k <= n
"""
from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        """回溯 + 剪枝"""

        def dfs(start_idx: int = 1, cnt: int = 0, path: list = []):
            if cnt == k:
                res.append(path[:])
                return
            # 要求 start_idx + (k - cnt) <= n + 1
            if start_idx + (k - cnt) > n + 1:
                return
            for i in range(start_idx, n + 1):
                path.append(i)
                dfs(i + 1, cnt + 1, path)
                path.pop()

        res = []
        dfs()
        return res


if __name__ == '__main__':
    print(Solution().combine(n=20, k=5))
