# -*- coding: UTF-8 -*-
"""
title: 分割回文串 II
Given a string s, partition s such that every substring of the partition is a palindrome.
Return the minimum cuts needed for a palindrome partitioning of s.


Example 1:
Input: s = "aab"
Output: 1
Explanation: The palindrome partitioning ["aa","b"] could be produced using 1 cut.

Example 2:
Input: s = "a"
Output: 0

Example 3:
Input: s = "ab"
Output: 1


Constraints:
1 <= s.length <= 2000
s consists of lowercase English letters only.
"""


class Solution:
    def minCut(self, s: str) -> int:
        """
        使用题131的方法进行动态规划预处理，从而可在O(1)的时间判断出任意 s[i..j] 是否为回文串。
        然后再使用动态规划计算最少分割次数，假设 f[i] 表示字符串前缀 s[0..i] 的最少分割次数，可以考虑枚举 s[0..i] 分割出的最后一个回文串，
        假设枚举最后一个回文串的起始位置为j+1，即s[j+1..i] 是一个回文串，则 f[i] = f[j] + 1，因此，状态转移方程为：f[i] = min(f[j]) + 1，其中，0<=j<i
        特殊情况：s[0..i]本身就是一个回文串，则f[i]=0，表示无需进行任何分割。
        """
        n = len(s)
        dp = [[True] * n for _ in range(n)]

        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                dp[i][j] = dp[i + 1][j - 1] and (s[i] == s[j])

        f = [float('inf')] * n
        for i in range(n):
            if dp[0][i]:
                f[i] = 0
            else:
                for j in range(i):
                    if dp[j + 1][i]:
                        f[i] = min(f[j] + 1, f[i])
        return int(f[-1])
