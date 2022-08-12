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
        动态规划预处理 + 动态规划
        先使用动态规划预处理出所有的子字符串中哪些是回文，使用一个二维dp数组存储
        然后再使用动态规划计算最少分割次数，f[i] 表示字符串s中前i个字符s[0..i]的最少分割次数，枚举 s[0..i] 分割出的最后一个回文串，
        然后枚举所有以字符i结尾的回文串，假设其中一个回文串的起始位置为j+1，即 dp[j + 1][i] = True，则 f[i] = f[j] + 1，
        状态转移方程为：f[i] = min(f[j]) + 1，其中，0<=j<i
        边界条件：f[0] = 0，一个字符是回文，不需要分割
        特殊情况：s[0..i]本身就是一个回文串，则 f[i] = 0，表示无需进行任何分割。
        """
        n = len(s)
        dp = [[True] * n for _ in range(n)]
        # dp[i][j] = dp[i+1][j-1] and s[i] == s[j]
        # dp[i+1][j-1] 在 dp[i][j]的左下方，所以i需要从下往上计算，因为在计算dp[i]的时候，dp[i+1]已经全部计算出来了，所以j从左往右、从右往左计算都可以
        # i >= j时，s[i:j+1]为单个字符或空字符串，单个字符或空字符串是回文，所以i >= j时，dp[i][j] = True
        # 所以只需计算i<j时的情况，即 只需计算(0, 0) ——> (n-1, n-1)对角线以上的部分
        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                dp[i][j] = dp[i + 1][j - 1] and s[i] == s[j]
        f = [0] * n
        for i in range(1, n):
            if dp[0][i]:
                continue
            tmp = n
            for j in range(i):
                if dp[j + 1][i]:
                    tmp = min(tmp, f[j] + 1)
                    if tmp == 1:
                        break
            f[i] = tmp
        return f[-1]


if __name__ == '__main__':
    print(Solution().minCut("aab"))
