# -*- coding: UTF-8 -*-
"""
title: 两个字符串的删除操作
Given two strings word1 and word2, return the minimum number of steps required to make word1 and word2 the same.
In one step, you can delete exactly one character in either string.


Example 1:
Input: word1 = "sea", word2 = "eat"
Output: 2
Explanation: You need one step to make "sea" to "ea" and another step to make "eat" to "ea".

Example 2:
Input: word1 = "leetcode", word2 = "etco"
Output: 4


Constraints:
1 <= word1.length, word2.length <= 500
word1 and word2 consist of only lowercase English letters.
"""


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """
        查找word1与word2之间的最长公共子序列common，最终结果为：len(word1) + len(word2) - 2 * len(common)
        查找最长公共子序列可使用二维动态规划，参考LeetCode题1143
        dp[i][j] 表示word1前i个字符(下标i-1)与word2前j个字符(下标j-1)之间最长公共子序列的长度。
        边界情况：空字符串与任意字符串之间最长公共子序列的长度均为0，所以 dp[0][*] = dp[*][0] = 0
        状态转移方程：若word1[i-1] == word2[j-1]，则 dp[i][j] = dp[i-1][j-1] + 1；
        若word1[i-1] != word2[j-1]，则 dp[i][j] = max(dp[i-1][j], dp[i][j-1])。
        相当于 用word1前i-1个字符与word2前j个字符去匹配 以及 用word1前i个字符与word2前j-1个字符去匹配
        """
        m, n = len(word1), len(word2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return m + n - 2 * dp[-1][-1]

    def minDistance_2(self, word1: str, word2: str) -> int:
        """
        直接使用动态规划计算最少删除次数
        dp[i][j] 表示使word1[:i]和word2[:j]相同的最少删除次数。其中 word1[:0] 表示空字符串
        状态转移方程：
        1、若word1[i-1] == word2[j-1]，则word1[i-1]、word2[j-1]都可以保留，即 dp[i][j] = dp[i-1][j-1]
        2、若word1[i-1] != word2[j-1]，则word1[i-1]、word2[j-1]至少需要删除其中一个
        2.1、若删除word1[i-1]，则 dp[i][j] = dp[i-1][j] + 1，后面的 +1 是指删除word1[i-1]需要一次操作
        2.2、若删除word2[j-1]，则 dp[i][j] = dp[i][j-1] + 1，后面的 +1 是指删除word2[j-1]需要一次操作
        所以若word1[i-1] != word2[j-1]，则 dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + 1
        边界条件：要使空字符串与任意字符串相同，则需删除该字符串中的所有字符，即 dp[0][j] = j、dp[i][0] = i
        """
        m, n = len(word1), len(word2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            dp[i][0] = i
        for j in range(1, n + 1):
            dp[0][j] = j
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + 1
        return dp[-1][-1]
