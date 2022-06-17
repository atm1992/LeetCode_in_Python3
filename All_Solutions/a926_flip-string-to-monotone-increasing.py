# -*- coding: UTF-8 -*-
"""
title: 将字符串翻转到单调递增
A binary string is monotone increasing if it consists of some number of 0's (possibly none), followed by some number of 1's (also possibly none).
You are given a binary string s. You can flip s[i] changing it from 0 to 1 or from 1 to 0.
Return the minimum number of flips to make s monotone increasing.


Example 1:
Input: s = "00110"
Output: 1
Explanation: We flip the last digit to get 00111.

Example 2:
Input: s = "010110"
Output: 2
Explanation: We flip to get 011111, or alternatively 000111.

Example 3:
Input: s = "00011000"
Output: 2
Explanation: We flip to get 00000000.


Constraints:
1 <= s.length <= 10^5
s[i] is either '0' or '1'.
"""


class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        """
        动态规划
        dp[i] 表示使字符串s中前i个字符单调递增的最小翻转次数。
        dp[i][0] 表示将字符i翻转为0的情况下，前i个字符单调递增的最小翻转次数
        dp[i][1] 表示将字符i翻转为1的情况下，前i个字符单调递增的最小翻转次数
        将字符i翻转为0，若需保持单调递增，则字符i-1只能是0，即 dp[i][0]只能从dp[i-1][0]转移而来，dp[i][0] = dp[i-1][0] + int(s[i]=='1')；
        将字符i翻转为1，若需保持单调递增，则字符i-1既可以是0、也可以是1，即 dp[i][1]可以从dp[i-1][0] 或 dp[i-1][1]转移而来，
        dp[i][1] = min(dp[i-1][0], dp[i-1][1]) + int(s[i]=='0')
        """
        # 1 <= s.length
        dp_0, dp_1 = int(s[0] == '1'), int(s[0] == '0')
        for ch in s[1:]:
            dp_0, dp_1 = dp_0 + int(ch == '1'), min(dp_0, dp_1) + int(ch == '0')
        return min(dp_0, dp_1)


if __name__ == '__main__':
    print(Solution().minFlipsMonoIncr("010110"))
