# -*- coding: UTF-8 -*-
"""
title: 最长的斐波那契子序列的长度
A sequence x1, x2, ..., xn is Fibonacci-like if:
    n >= 3
    xi + xi+1 == xi+2 for all i + 2 <= n
Given a strictly increasing array arr of positive integers forming a sequence, return the length of the longest Fibonacci-like subsequence of arr. If one does not exist, return 0.
A subsequence is derived from another sequence arr by deleting any number of elements (including none) from arr, without changing the order of the remaining elements. For example, [3, 5, 8] is a subsequence of [3, 4, 5, 6, 7, 8].


Example 1:
Input: arr = [1,2,3,4,5,6,7,8]
Output: 5
Explanation: The longest subsequence that is fibonacci-like: [1,2,3,5,8].

Example 2:
Input: arr = [1,3,7,11,12,14,18]
Output: 3
Explanation: The longest subsequence that is fibonacci-like: [1,11,12], [3,11,14] or [7,11,18].


Constraints:
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
