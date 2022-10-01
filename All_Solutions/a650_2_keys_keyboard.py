# -*- coding: UTF-8 -*-
"""
title: 只有两个键的键盘
There is only one character 'A' on the screen of a notepad. You can perform one of two operations on this notepad for each step:
    Copy All: You can copy all the characters present on the screen (a partial copy is not allowed).
    Paste: You can paste the characters which are copied last time.
Given an integer n, return the minimum number of operations to get the character 'A' exactly n times on the screen.


Example 1:
Input: n = 3
Output: 3
Explanation: Initially, we have one character 'A'.
In step 1, we use Copy All operation.
In step 2, we use Paste operation to get 'AA'.
In step 3, we use Paste operation to get 'AAA'.

Example 2:
Input: n = 1
Output: 0


Constraints:
1 <= n <= 1000
"""
import math


class Solution:
    def minSteps(self, n: int) -> int:
        """
        动态规划
        假设 dp[i] 表示在记事本上输出恰好 i 个字符'A'的最少操作次数
        要恰好输出i个字符，并且操作次数要最少，则每次复制的字符应尽可能多，每次复制的字符个数最少为1，最多为 i//2
        所以要恰好得到i个字符，最多就是Copy 1次，Paste i-1次，即 dp[i]的最大为i
        假设每次复制的字符个数为j，则j需要能被i整除，即 i % j == 0，才能恰好得到i个字符
        dp[j]表示从1个字符变为j个字符的最少操作次数；而dp[i//j] 表示从1个字符变为i//j个字符的最少操作次数，等价于 从j个字符变为i个字符的最少操作次数
        即 状态转移方程为 dp[i] = min(dp[j] + dp[i//j]) ，其中 i % j == 0 且 1 < j * j <= i
        其实可以验证，若 i = j * i/j = k * i/k 其中(j != k)，则 dp[i] = dp[j] + dp[i//j] = dp[k] + dp[i//k]
        dp[24] = dp[4] + dp[6] = dp[4] + (dp[2] + dp[3]) = (dp[4] + dp[2]) + dp[3] = dp[8] + dp[3]
        """
        dp = [0, 0]
        for i in range(2, n + 1):
            # 最多只需操作 i 次
            tmp = i
            for j in range(2, int(math.sqrt(i)) + 1):
                if i % j == 0:
                    tmp = dp[j] + dp[i // j]
                    break
            dp.append(tmp)
        return dp[-1]

    def minSteps_2(self, n: int) -> int:
        """
        数学。质因数分解
        当i为质数时，每次复制的字符个数只能为1，此时 dp[i] = i，已经是最少操作次数了
        当i为合数时，每次复制的字符个数可以大于1，使操作次数尽可能少
        dp[24] = dp[4] + dp[6] = (dp[2] + dp[2]) + (dp[2] + dp[3]) = 3 * d[2] + dp[3] = 3 * 2 + 3 = 9
        """
        res = 0
        for i in range(2, int(math.sqrt(n)) + 1):
            while n % i == 0:
                res += i
                n //= i
        return res + n if n > 1 else res


if __name__ == '__main__':
    print(Solution().minSteps_2(24))
