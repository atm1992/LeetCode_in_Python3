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
        """
        动态规划（正序遍历）
        dp[i][j] 表示在字符串s的前i个字符s[:i]中，字符串t的前j个字符t[:j]的出现个数。前0个字符表示空字符串
        可分为两种情况讨论：
        1、s[i-1] == t[j-1]，此时既可选择让s[i-1] 与 t[j-1]进行匹配，也可不让s[i-1] 与 t[j-1]匹配。若匹配，则 dp[i][j] = dp[i-1][j-1]；
        若不匹配，则相当于在s[:i-1]中查找t[:j]，即 dp[i][j] = dp[i-1][j]。最终 dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
        2、s[i-1] != t[j-1]，此时s[i-1] 与 t[j-1]不匹配，即 dp[i][j] = dp[i-1][j]
        边界条件：
        1、dp[x][0] 表示在任意长度的字符串s中查找空字符串t的出现个数，此时 dp[x][0] = 1；
        2、dp[0][x]（x > 0）表示在空字符串s中查找非空字符串t的出现个数，此时 dp[0][x] = 0。
        根据状态转移方程可知，dp[i] 只与 dp[i-1]有关，因此可用滚动数组的思想，降低空间复杂度
        """
        m, n = len(s), len(t)
        if m < n:
            return 0
        # i == 0时的结果
        dp = [[1] + [0] * n, [1] + [0] * n]
        for i in range(1, m + 1):
            # dp[x][0] = 1
            for j in range(1, n + 1):
                if s[i - 1] == t[j - 1]:
                    dp[1][j] += dp[0][j - 1]
            dp[0][:] = dp[1][:]
        return dp[-1][-1]

    def numDistinct_2(self, s: str, t: str) -> int:
        """
        动态规划（逆序遍历）
        dp[i][j] 表示在字符串s的前i个字符s[:i]中，字符串t的前j个字符t[:j]的出现个数。前0个字符表示空字符串
        可分为两种情况讨论：
        1、s[i-1] == t[j-1]，此时既可选择让s[i-1] 与 t[j-1]进行匹配，也可不让s[i-1] 与 t[j-1]匹配。若匹配，则 dp[i][j] = dp[i-1][j-1]；
        若不匹配，则相当于在s[:i-1]中查找t[:j]，即 dp[i][j] = dp[i-1][j]。最终 dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
        2、s[i-1] != t[j-1]，此时s[i-1] 与 t[j-1]不匹配，即 dp[i][j] = dp[i-1][j]
        边界条件：
        1、dp[x][0] 表示在任意长度的字符串s中查找空字符串t的出现个数，此时 dp[x][0] = 1；
        2、dp[0][x]（x > 0）表示在空字符串s中查找非空字符串t的出现个数，此时 dp[0][x] = 0。
        根据状态转移方程可知，dp[i] 只与 dp[i-1]有关，因此可用滚动数组的思想，降低空间复杂度
        """
        m, n = len(s), len(t)
        if m < n:
            return 0
        # i == 0时的结果
        dp = [1] + [0] * n
        for i in range(1, m + 1):
            # 1 <= j <= min(i, n)。j为0时，dp[i][j]=1；j>i时，dp[i][j]=0
            for j in range(min(i, n), 0, -1):
                if s[i - 1] == t[j - 1]:
                    dp[j] += dp[j - 1]
                if i == m:
                    return dp[-1]


if __name__ == '__main__':
    print(Solution().numDistinct("babgbag", t="bag"))
