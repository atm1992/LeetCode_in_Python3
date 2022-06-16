# -*- coding: UTF-8 -*-
"""
title: 含有 k 个元素的组合
给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。


示例 1:
输入: n = 4, k = 2
输出:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]

示例 2:
输入: n = 1, k = 1
输出: [[1]]


提示:
1 <= n <= 20
1 <= k <= n
"""
from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        """回溯 + 剪枝"""

        def dfs(i: int, path: List[int]) -> None:
            # 剪枝
            if len(path) + (n - i + 1) < k:
                return
            if len(path) == k:
                res.append(path[:])
                return
            # 选择当前元素
            path.append(i)
            dfs(i + 1, path)
            # 回溯
            path.pop()

            # 跳过当前元素
            dfs(i + 1, path)

        res = []
        dfs(1, [])
        return res

    def combine_2(self, n: int, k: int) -> List[List[int]]:
        """非递归（字典序法）实现组合型枚举"""
        res = []
        # tmp数组的长度始终为k+1，下标范围: [0, k]，并且tmp[k] == n+1，是一个哨兵。
        # tmp[k-1]可以从k取到n，tmp[0:k] 的变化范围：[1, ……, k] ——> [n-k+1, ……, n]
        tmp = [i for i in range(1, k + 1)]
        tmp.append(n + 1)
        j = 0
        while j < k:
            res.append(tmp[:k])
            j = 0
            # 值不连续的时候，跳出while循环
            # 以 n=5, k=3 为例：
            # 初始时，tmp[:k] 为 [1, 2, 3]
            # 变化情况为：[1, 2, 3] ——> [1, 2, 4] ——> [1, 3, 4] ——> [2, 3, 4] ——> [1, 2, 5] ——> [1, 3, 5] ——> [2, 3, 5] ——> [1, 4, 5] ——> [2, 4, 5] ——> [3, 4, 5]
            # 从下标0开始，一直向后查找，若存在连续的m个值(m -> m+1 不连续了)，则将低位的m-1个值修改为：1 ~ m-1，第m个值在原有的基础上加1
            while j < k and tmp[j] + 1 == tmp[j + 1]:
                # j 是下标(从0开始)，取值需要从1开始
                tmp[j] = j + 1
                j += 1
            if j < k:
                tmp[j] += 1
        return res


if __name__ == '__main__':
    print(Solution().combine_2(n=5, k=3))
