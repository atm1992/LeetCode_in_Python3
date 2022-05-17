# -*- coding: UTF-8 -*-
"""
title: 整数拆分
Given an integer n, break it into the sum of k positive integers, where k >= 2, and maximize the product of those integers.
Return the maximum product you can get.


Example 1:
Input: n = 2
Output: 1
Explanation: 2 = 1 + 1, 1 × 1 = 1.

Example 2:
Input: n = 10
Output: 36
Explanation: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36.


Constraints:
2 <= n <= 58
"""


class Solution:
    def integerBreak(self, n: int) -> int:
        res = 0
        for k in range(2, n + 1):
            average_size, extra_size = divmod(n, k)
            tmp = [average_size] * k
            for i in range(extra_size):
                tmp[i] += 1
            tmp_res = 1
            for item in tmp:
                tmp_res *= item
            if tmp_res <= res:
                break
            res = tmp_res
        return res

    def integerBreak_2(self, n: int) -> int:
        """
        动态规划。dp[i] 表示将正整数 i 拆分成至少两个正整数的和之后，这些正整数的最大乘积。注意：0 和 1 都不能拆分，因此dp[0]=dp[1]=0
        当i>=2时，假设对正整数i拆分出的第一个正整数为j (1<=j<i)，则有以下两种情况：
        1、将i拆分为j、i-j后，不再对i-j继续拆分，此时的乘积为 j * (i-j)
        2、将i拆分为j、i-j后，继续拆分i-j，此时的乘积为 j * dp[i-j]
        所以状态转移方程为：dp[i] = max(j * (i - j), j * dp[i - j])
        由于j的取值范围为：[1, i-1]，所以需要遍历所有的j，从而获得最大的dp[i]
        """
        dp = [0] * (n + 1)
        for i in range(2, n + 1):
            for j in range(1, i):
                dp[i] = max(dp[i], j * (i - j), j * dp[i - j])
        return dp[n]

    def integerBreak_3(self, n: int) -> int:
        """
        贪心。分成尽可能多的长度为3的小段，这样的乘积最大。通过数学推导出每段的最佳长度为自然底数e = 2.71828
        n == 2时，1 * 1 = 1，返回 n - 1
        n == 3时，1 * 2 = 2，返回 n - 1
        n == 4时，2 * 2 = 4
        n > 4时，分成尽可能多的长度为3的小段，每次循环时，长度n减去3，乘积res乘以3。退出循环后，再乘以小于等于4的最后一小段(此时的n<=4)
        """
        if n < 4:
            return n - 1
        res = 1
        # 退出循环时，n的可能取值为：2、3、4
        while n > 4:
            res = res * 3
            n -= 3
        return res * n

    def integerBreak_4(self, n: int) -> int:
        """
        数学。分成尽可能多的长度为3的小段，这样的乘积最大。通过数学推导出每段的最佳长度为自然底数e = 2.71828
        """
        if n < 4:
            return n - 1
        div, mod = divmod(n, 3)
        if mod == 0:
            return 3 ** div
        elif mod == 1:
            return 3 ** (div - 1) * 4
        else:
            return 3 ** div * 2


if __name__ == '__main__':
    print(Solution().integerBreak_2(10))
