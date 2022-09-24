# -*- coding: UTF-8 -*-
"""
title: 两个字符串的最小ASCII删除和
Given two strings s1 and s2, return the lowest ASCII sum of deleted characters to make two strings equal.


Example 1:
Input: s1 = "sea", s2 = "eat"
Output: 231
Explanation: Deleting "s" from "sea" adds the ASCII value of "s" (115) to the sum.
Deleting "t" from "eat" adds 116 to the sum.
At the end, both strings are equal, and 115 + 116 = 231 is the minimum sum possible to achieve this.

Example 2:
Input: s1 = "delete", s2 = "leet"
Output: 403
Explanation: Deleting "dee" from "delete" to turn the string into "let",
adds 100[d] + 101[e] + 101[e] to the sum.
Deleting "e" from "leet" adds 101[e] to the sum.
At the end, both strings are equal to "let", and the answer is 100+101+101+101 = 403.
If instead we turned both strings into "lee" or "eet", we would get answers of 433 or 417, which are higher.


Constraints:
1 <= s1.length, s2.length <= 1000
s1 and s2 consist of lowercase English letters.
"""


class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        """
        动态规划
        假设 dp[i][j] 表示使s1[:i]和s2[:j]相同的最小ASCII删除和
        状态转移方程：
        当i>0且j>0时，
            若s1[i-1] == s2[j-1]，则 dp[i][j] = dp[i-1][j-1]
            若s1[i-1] != s2[j-1]，则 dp[i][j] = min(dp[i-1][j] + ord(s1[i-1]), dp[i][j-1] + ord(s2[j-1]))
        边界条件：
        当i==0且j==0时，两个都是空字符串，已经相同，无需删除任何字符，所以 dp[0][0] = 0
        当i==0且j>0时，一个是空字符串，一个是非空字符串，要使相同，则需删除非空字符串的所有字符，所以 dp[0][j>0] = dp[0][j-1] + ord(s2[j-1])
        当i>0且j==0时，和上面同理，此时 dp[i>0][0] = dp[i-1][0] + ord(s1[i-1])
        """
        n = len(s2)
        dp = [0]
        for ch2 in s2:
            dp.append(dp[-1] + ord(ch2))
        for ch1 in s1:
            pre = dp[0]
            dp[0] += ord(ch1)
            for j in range(1, n + 1):
                cur = dp[j]
                ch2 = s2[j - 1]
                if ch1 == ch2:
                    dp[j] = pre
                else:
                    dp[j] = min(dp[j] + ord(ch1), dp[j - 1] + ord(ch2))
                pre = cur
        return dp[-1]


if __name__ == '__main__':
    print(Solution().minimumDeleteSum(s1="delete", s2="leet"))
