# -*- coding: UTF-8 -*-
"""
title: 最长回文子序列
Given a string s, find the longest palindromic subsequence's length in s.
A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.


Example 1:
Input: s = "bbbab"
Output: 4
Explanation: One possible longest palindromic subsequence is "bbbb".

Example 2:
Input: s = "cbbd"
Output: 2
Explanation: One possible longest palindromic subsequence is "bb".


Constraints:
1 <= s.length <= 1000
s consists only of lowercase English letters.
"""


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        """
        动态规划
        dp[i][j] 表示字符串s的下标范围[i, j]内的最长回文子序列的长度。0 <= i <= j < n
        当 i > j 时，字符串为空，因此 dp[i][j] = 0
        当 i == j 时，字符串长度为1，长度为1的字符串都是回文，因此 dp[i][j] = 1
        当 i < j 时，
            1、若 s[i] == s[j]，则 dp[i][j] = dp[i+1][j-1] + 2
            2、若 s[i] != s[j]，则 dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        """
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            dp[i][i] = 1
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
        return dp[0][n - 1]


if __name__ == '__main__':
    print(Solution().longestPalindromeSubseq("bbbab"))
