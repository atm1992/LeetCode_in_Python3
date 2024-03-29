# -*- coding: UTF-8 -*-
"""
title: 把数字翻译成字符串
给定一个数字，我们按照如下规则把它翻译为字符串：0 翻译成 “a” ，1 翻译成 “b”，……，11 翻译成 “l”，……，25 翻译成 “z”。一个数字可能有多个翻译。请编程实现一个函数，用来计算一个数字有多少种不同的翻译方法。


示例 1:
输入: 12258
输出: 5
解释: 12258有5种不同的翻译，分别是"bccfi", "bwfi", "bczi", "mcfi"和"mzi"


提示：
0 <= num < 2^31
"""


class Solution:
    def translateNum(self, num: int) -> int:
        """
        动态规划
        dp[i] 表示以下标i结尾的字符串的翻译方法数；dp[0] = 1 表示第1个字符(下标0)的翻译方法数。
        若当前字符i与前一位字符i-1组合起来的字符串num[i-1:i+1]不满足条件：'10' <= num[i-1:i+1] <= '25'，
        则当前字符i只能直接拼接到以下标i-1结尾的字符串的后面，此时 dp[i] = dp[i-1]；
        若当前字符i与前一位字符i-1组合起来的字符串num[i-1:i+1]符合：10 <= dp[i-1:i+1] <= 25，
        则 当前字符i既可以直接拼接到以下标i-1结尾的字符串的后面dp[i-1]，也可以先和字符i-1组合起来，再拼接到以下标i-2结尾的字符串的后面dp[i-2]，
        所以此时 dp[i] = dp[i-1] + dp[i-2]。
        若当前i=1，此时dp[i-1] = dp[0] = 1，而dp[i-2]不存在，可将dp[i-2]认为1，表示字符i与字符i-1组合起来可翻译成一种新的字符。
        """
        num = str(num)
        # dp[0] = 1 表示第1个字符(下标0)的翻译方法数
        dp = [1]
        # 从第2个字符(下标1)开始遍历
        for i in range(1, len(num)):
            tmp = dp[i-1]
            if '10' <= num[i - 1:i + 1] <= '25':
                tmp += dp[i-2] if i - 2 >= 0 else 1
            dp.append(tmp)
        return dp[-1]


if __name__ == '__main__':
    print(Solution().translateNum(18822))
