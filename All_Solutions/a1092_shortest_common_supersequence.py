# -*- coding: utf-8 -*-
# @date: 2023/3/28
# @author: liuquan
"""
title: 最短公共超序列
Given two strings str1 and str2, return the shortest string that has both str1 and str2 as subsequences. If there are multiple valid strings, return any of them.
A string s is a subsequence of string t if deleting some number of characters from t (possibly 0) results in the string s.


Example 1:
Input: str1 = "abac", str2 = "cab"
Output: "cabac"
Explanation:
str1 = "abac" is a subsequence of "cabac" because we can delete the first "c".
str2 = "cab" is a subsequence of "cabac" because we can delete the last "ac".
The answer provided is the shortest such string that satisfies these properties.

Example 2:
Input: str1 = "aaaaaaaa", str2 = "aaaaaaaa"
Output: "aaaaaaaa"


Constraints:
1 <= str1.length, str2.length <= 1000
str1 and str2 consist of lowercase English letters.
"""


class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        """
        动态规划 + 双指针
        dp[i][j] 表示str1[i:]与str2[j:]之间的最短公共超序列的长度。dp[0][0]即为最终答案的长度
        状态转移方程：
        1、若str1[i] == str2[j]，则直接使用str1[i]，此时的 dp[i][j] = dp[i+1][j+1] + 1
        2、若str1[i] != str2[j]，则可使用str1[i]或str2[j]，此时的 dp[i][j] = min(dp[i+1][j], dp[i][j+1]) + 1
        边界条件：
        m, n = len(str1), len(str2)
        dp[m][j] = n - j 直接使用 str2[j:] 作为最短公共超序列
        dp[i][n] = m - i 直接使用 str1[i:] 作为最短公共超序列

        求得dp[0][0]后，结合上面dp的结果，使用双指针从前往后构造出一个最短公共超序列
        初始时，i指向str1[0]，j指向str2[0]
        1、若str1[i] == str2[j]，则毫无疑问直接使用str1[i]
        2、若str1[i] != str2[j]，则根据dp[i+1][j]和dp[i][j+1]的大小关系来决定使用哪个
            2.1、若dp[i][j] = dp[i+1][j] + 1，则说明应该使用str1[i]，然后 i += 1
            2.2、若dp[i][j] = dp[i][j+1] + 1，则说明应该使用str2[j]，然后 j += 1
        当i或j其中一个到达终点后，则直接拼接另一个字符串的剩余部分
        """
        m, n = len(str1), len(str2)
        dp = [[m + n] * (n + 1) for _ in range(m + 1)]
        for i in range(m, -1, -1):
            for j in range(n, -1, -1):
                if i == m or j == n:
                    dp[i][j] = n - j if i == m else m - i
                    continue
                dp[i][j] = dp[i + 1][j + 1] + 1 if str1[i] == str2[j] else min(dp[i + 1][j], dp[i][j + 1]) + 1
        res = []
        i, j = 0, 0
        while i < m and j < n:
            if str1[i] == str2[j]:
                res.append(str1[i])
                i += 1
                j += 1
            elif dp[i][j] == dp[i + 1][j] + 1:
                res.append(str1[i])
                i += 1
            else:
                res.append(str2[j])
                j += 1
        if i < m:
            res.append(str1[i:])
        elif j < n:
            res.append(str2[j:])
        return ''.join(res)


if __name__ == '__main__':
    print(Solution().shortestCommonSupersequence(str1="abac", str2="cab"))
