# -*- coding: UTF-8 -*-
"""
title: 解码方法
A message containing letters from A-Z can be encoded into numbers using the following mapping:
    'A' -> "1"
    'B' -> "2"
    ...
    'Z' -> "26"
To decode an encoded message, all the digits must be grouped then mapped back into letters using the reverse of the mapping above (there may be multiple ways). For example, "11106" can be mapped into:
    "AAJF" with the grouping (1 1 10 6)
    "KJF" with the grouping (11 10 6)
Note that the grouping (1 11 06) is invalid because "06" cannot be mapped into 'F' since "6" is different from "06".
Given a string s containing only digits, return the number of ways to decode it.
The answer is guaranteed to fit in a 32-bit integer.


Example 1:
Input: s = "12"
Output: 2
Explanation: "12" could be decoded as "AB" (1 2) or "L" (12).

Example 2:
Input: s = "226"
Output: 3
Explanation: "226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).

Example 3:
Input: s = "0"
Output: 0
Explanation: There is no character that is mapped to a number starting with 0.
The only valid mappings with 0 are 'J' -> "10" and 'T' -> "20", neither of which start with 0.
Hence, there are no valid ways to decode this since all digits need to be mapped.

Example 4:
Input: s = "06"
Output: 0
Explanation: "06" cannot be mapped to "F" because of the leading zero ("6" is different from "06").


Constraints:
1 <= s.length <= 100
s contains only digits and may contain leading zero(s).
"""


class Solution:
    def numDecodings(self, s: str) -> int:
        """动态规划。此题与青蛙跳台阶基本一致。
        设dp_i为字符串s中前i个字符组成的子串的解码方法数。
        解码分为两种情况：
        1、将第i个字符作为组合。只要第i个字符s[i-1]不为'0'，此时 dp_i 为 dp_i_1；
        2、将第i-1、i个字符作为组合。只要第i-1个字符s[i-2]不为'0'，并且int(s[i-2:i])<=26，此时 dp_i 为 dp_i_2。
        将以上两种情况的结果相加，便得到最终的dp_i，即 dp_i = dp_i_1 + dp_i_2
        """
        n = len(s)
        # 初始时，dp_i_1 表示字符串为空时的解码方法数。dp_i 从第1个字符开始求解
        dp_i_2, dp_i_1, dp_i = 0, 1, 0
        # 这里的i表示第i个字符。从第1个字符遍历到第n个字符
        for i in range(1, n + 1):
            dp_i = 0
            if s[i - 1] != '0':
                dp_i += dp_i_1
            if i > 1 and s[i - 2] != '0' and int(s[i - 2:i]) <= 26:
                dp_i += dp_i_2
            dp_i_2, dp_i_1 = dp_i_1, dp_i
        return dp_i


if __name__ == '__main__':
    print(Solution().numDecodings("1123"))
