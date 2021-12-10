# -*- coding: UTF-8 -*-
"""
title：不同的子序列
Given two strings s and t, return the number of distinct subsequences of s which equals t.
A string's subsequence is a new string formed from the original string by deleting some (can be none) of the characters without disturbing the remaining characters' relative positions. (i.e., "ACE" is a subsequence of "ABCDE" while "AEC" is not).
It is guaranteed the answer fits on a 32-bit signed integer.


Example 1:
Input: s = "rabbbit", t = "rabbit"
Output: 3
Explanation:
As shown below, there are 3 ways you can generate "rabbit" from S.
rabbbit
rabbbit
rabbbit

Example 2:
Input: s = "babgbag", t = "bag"
Output: 5
Explanation:
As shown below, there are 5 ways you can generate "bag" from S.
babgbag
babgbag
babgbag
babgbag
babgbag


Constraints:
1 <= s.length, t.length <= 1000
s and t consist of English letters.
"""


class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        """动态规划。dp[i][j] 表示在 s[:i] 的子序列中 t[:j] 出现的个数，因此，dp[i+1][j+1] 表示在 s[:i+1] 的子序列中 t[:j+1] 出现的个数，
        此时分为两种情况讨论：
        一、s[i] == t[j]，可以选择将s[i]和t[j]匹配，此时 dp[i+1][j+1] = dp[i][j]；也可以选择不将s[i]和t[j]匹配，
        此时意味着需要在 s[:i] 的子序列中计算 t[:j+1] 出现的个数，即 dp[i+1][j+1] = dp[i][j+1]。最终，dp[i+1][j+1] = dp[i][j] + dp[i][j+1]
        二、s[i] != t[j]，此时的s[i]和t[j]不能匹配，因此只有 dp[i+1][j+1] = dp[i][j+1]。
        根据上述状态转移方程，可将dp二维数组从 (m+1) * (n+1) 压缩为 2 * (n+1)。
        考虑特殊情况：dp[x][0] 表示在任意长度的序列中查找空字符串出现的个数，即 dp[x][0] = 1；
        dp[0][x]（x 除0以外）表示在空字符串中查找非空字符串出现的个数，即 dp[0][x] = 0，其中 x > 0"""
        m, n = len(s), len(t)
        if m < n:
            return 0
        # 初始化一个2 * (n+1)的二维dp数组，始终只计算dp[1][1:]
        dp = [[1] + [0] * n, [1] + [0] * n]
        for i in range(m):
            for j in range(n):
                if s[i] == t[j]:
                    dp[1][j + 1] += dp[0][j]
            dp[0][:] = dp[1][:]
        return dp[-1][-1]


if __name__ == '__main__':
    print(Solution().numDistinct(s="rabbbit", t="rabbit"))
