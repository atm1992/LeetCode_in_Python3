# -*- coding: UTF-8 -*-
"""
title: 爬楼梯
You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?


Example 1:
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:
Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step


Constraints:
1 <= n <= 45
"""


class Solution:
    def climbStairs(self, n: int) -> int:
        """递归。f(n) = f(n-1) + f(n-2)，会运行超时，因为存在大量的重复计算"""
        if n == 1:
            return 1
        if n == 2:
            return 2
        return self.climbStairs(n - 1) + self.climbStairs(n - 2)

    def climbStairs_2(self, n: int) -> int:
        """动态规划。当前状态只和前两个状态有关，因此只需保留前两个状态即可"""
        # dp数组初始化时，包含了n为1和2时的结果。n为奇数时，结果取dp[0]；n为偶数时，结果取dp[1]。
        dp = [1, 2]
        for i in range(3, n + 1):
            dp[i % 2 == 0] = sum(dp)
        return dp[n % 2 == 0]


if __name__ == '__main__':
    print(Solution().climbStairs_2(4))
