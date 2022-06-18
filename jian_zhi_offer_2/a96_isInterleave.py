# -*- coding: UTF-8 -*-
"""
title: 字符串交织
给定三个字符串 s1、s2、s3，请判断 s3 能不能由 s1 和 s2 交织（交错） 组成。
两个字符串 s 和 t 交织 的定义与过程如下，其中每个字符串都会被分割成若干 非空 子字符串：
    s = s1 + s2 + ... + sn
    t = t1 + t2 + ... + tm
    |n - m| <= 1
    交织 是 s1 + t1 + s2 + t2 + s3 + t3 + ... 或者 t1 + s1 + t2 + s2 + t3 + s3 + ...
提示：a + b 意味着字符串 a 和 b 连接。


示例 1：
输入：s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
输出：true

示例 2：
输入：s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
输出：false

示例 3：
输入：s1 = "", s2 = "", s3 = ""
输出：true


提示：
0 <= s1.length, s2.length <= 100
0 <= s3.length <= 200
s1、s2、和 s3 都由小写英文字母组成
"""


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        """
        动态规划。
        s = s1 + s2 + ... + sn
        t = t1 + t2 + ... + tm
        |n - m| <= 1
        注意：不要误解题意，题目并没有要求len(s1) == len(s2) == len(sn)，也没有要求len(s1) == len(t1)，
        因此，|n - m| <= 1 是一个必然能满足的条件。如果s3从下标i到下标j的字符都是来自s1，那么完全可将s1中下标i到下标j的字符作为一个整体(子字符串)，
        而下标i之前以及下标j之后的字符串必然来自s2，因为如果下标j后面的字符依旧来自s1，那么完全可将这些字符跟前面的下标i到下标j合并为一个子字符串，
        直到某个下标之后的字符是来自s2。
        题解：假设 dp[i][j] 表示s3中的前i+j个字符能否由s1中的前i个字符 和 s2中的前j个字符交错而来。字符串的下标从0开始，前0个字符表示空字符串。
        若s3[i+j-1]==s1[i-1] 且 dp[i-1][j] 为True，则dp[i][j]为True；若s3[i+j-1]==s2[j-1] 且 dp[i][j-1] 为True，则dp[i][j]也为True。
        所以，状态转移方程为：dp[i][j] = (dp[i-1][j] and s3[i+j-1]==s1[i-1]) or (dp[i][j-1] and s3[i+j-1]==s2[j-1])
        边界条件：由Example 3可知，dp[0][0] = True
        由上面的状态转移方程可知，dp[i][j]只与dp[i-1][j]、dp[i][j-1]有关，因此可用滚动数组来优化空间复杂度
        """
        # 这里是为了进一步减小一维dp数组的空间复杂度。其实可以不写
        if len(s1) < len(s2):
            return self.isInterleave(s2, s1, s3)
        n1, n2, n3 = len(s1), len(s2), len(s3)
        if n1 + n2 != n3:
            return False
        # 一维dp数组
        dp = [True] + [False] * n2
        for i in range(n1 + 1):
            for j in range(n2 + 1):
                k = i + j - 1
                if i > 0:
                    # and前面的dp[j]，指的是dp[i-1][j]
                    dp[j] = dp[j] and s3[k] == s1[i - 1]
                if j > 0 and not dp[j]:
                    # and前面的dp[j-1]，指的是dp[i][j-1]
                    dp[j] = dp[j - 1] and s3[k] == s2[j - 1]
        return dp[-1]
