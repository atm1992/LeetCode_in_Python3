# -*- coding: UTF-8 -*-
"""
title: 子序列的数目
给定一个字符串 s 和一个字符串 t ，计算在 s 的子序列中 t 出现的个数。
字符串的一个 子序列 是指，通过删除一些（也可以不删除）字符且不干扰剩余字符相对位置所组成的新字符串。（例如，"ACE" 是 "ABCDE" 的一个子序列，而 "AEC" 不是）
题目数据保证答案符合 32 位带符号整数范围。


示例 1：
输入：s = "rabbbit", t = "rabbit"
输出：3
解释：
如下图所示, 有 3 种可以从 s 中得到 "rabbit" 的方案。
rabbbit
rabbbit
rabbbit

示例 2：
输入：s = "babgbag", t = "bag"
输出：5
解释：
如下图所示, 有 5 种可以从 s 中得到 "bag" 的方案。
babgbag
babgbag
babgbag
babgbag
babgbag


提示：
0 <= s.length, t.length <= 1000
s 和 t 由英文字母组成
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
    print(Solution().numDistinct(s="babgbag", t="bag"))
