# -*- coding: UTF-8 -*-
"""
title: 最长斐波那契数列
如果序列 X_1, X_2, ..., X_n 满足下列条件，就说它是 斐波那契式 的：
    n >= 3
    对于所有 i + 2 <= n，都有 X_i + X_{i+1} = X_{i+2}
给定一个严格递增的正整数数组形成序列 arr ，找到 arr 中最长的斐波那契式的子序列的长度。如果一个不存在，返回  0 。
（回想一下，子序列是从原序列  arr 中派生出来的，它从 arr 中删掉任意数量的元素（也可以不删），而不改变其余元素的顺序。例如， [3, 5, 8] 是 [3, 4, 5, 6, 7, 8] 的一个子序列）


示例 1：
输入: arr = [1,2,3,4,5,6,7,8]
输出: 5
解释: 最长的斐波那契式子序列为 [1,2,3,5,8] 。

示例 2：
输入: arr = [1,3,7,11,12,14,18]
输出: 3
解释: 最长的斐波那契式子序列有 [1,11,12]、[3,11,14] 以及 [7,11,18] 。


提示：
3 <= arr.length <= 1000
1 <= arr[i] < arr[i + 1] <= 10^9
"""
from collections import defaultdict
from typing import List


class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        """哈希 + 暴力"""
        arr_set = set(arr)
        n = len(arr)
        res = 0
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                x, y = arr[i], arr[j]
                tmp = 2
                while x + y in arr_set:
                    x, y = y, x + y
                    tmp += 1
                res = max(res, tmp)
        return res if res >= 3 else 0

    def lenLongestFibSubseq_2(self, arr: List[int]) -> int:
        """
        哈希表 + 动态规划
        arr是严格递增的，就意味着每个元素值都是唯一的
        dp[i][j] 表示以元素i、元素j结尾的最长斐波那契子序列的长度，其中 i < j
        状态转移方程：dp[i][j] = dp[k][i] + 1，其中 k < i < j, arr[k] + arr[i] == arr[j]
        初始值：dp[i][j] = 2
        """
        num2idx = {num: idx for idx, num in enumerate(arr)}
        # defaultdict(lambda: 2) 表示默认值为2，defaultdict(int) 的默认值为0
        dp = defaultdict(lambda: 2)
        res = 0
        n = len(arr)
        # k < i < j
        for i in range(1, n - 1):
            for j in range(i + 1, n):
                k = num2idx.get(arr[j] - arr[i], n)
                if k < i:
                    dp[(i, j)] = dp[(k, i)] + 1
                    res = max(res, dp[(i, j)])
        return res if res >= 3 else 0


if __name__ == '__main__':
    print(Solution().lenLongestFibSubseq_2([1, 3, 7, 11, 12, 14, 18]))
