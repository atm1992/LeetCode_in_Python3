# -*- coding: UTF-8 -*-
"""
title: 不同路径
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
How many possible unique paths are there?


Example 1:
Input: m = 3, n = 7
Output: 28

Example 2:
Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down

Example 3:
Input: m = 7, n = 3
Output: 28

Example 4:
Input: m = 3, n = 3
Output: 6


Constraints:
1 <= m, n <= 100
It's guaranteed that the answer will be less than or equal to 2 * 10^9.
"""


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """递归。运行超时，因为存在大量重复计算"""
        if m < 1 or n < 1:
            return 0
        if m == 1 or n == 1:
            return 1
        return self.uniquePaths(m, n - 1) + self.uniquePaths(m - 1, n)

    def uniquePaths_2(self, m: int, n: int) -> int:
        """动态规划。假设 dp[i][j] 为(0,0)走到(i,j)的路径数量，因为只可能是从(i-1,j)向下走到(i,j) 或 从(i,j-1)向右走到(i,j)，
        所以状态转移方程为 dp[i][j] = dp[i-1][j] + dp[i][j-1]。又因为dp[i][j]只与第i-1行和第i行的状态有关，所以dp数组只需存储这两行的状态即可。
        因为从起点(0,0)走到第一行的任意点(0,j) 以及 第一列的任意点(i,0)都是只有一条路径，所以dp[0][j] = dp[i][0] = 1。"""
        if n > m:
            # 交换行列的值，并不影响此题的答案。这里是为了进一步降低空间复杂度，降为 O(min(m,n))。时间复杂度还是O(mn)
            return self.uniquePaths_2(n, m)

        # 初始化dp二维数组，dp数组始终只有两行。最终答案始终为 dp[-1][-1]
        dp = [[1] * n, [1] * n]
        # 始终只计算dp数组第二行的结果，第一行始终都是最新的已计算结果。并且因为到第一列任意点的路径都只有1，所以第二行第一列的值固定为1，
        # 第二行只需从第二列开始计算。总共有m行，所以要计算m-1次
        for _ in range(m - 1):
            for col in range(1, n):
                dp[1][col] = dp[0][col] + dp[1][col - 1]
            dp[0][:] = dp[1][:]
        return dp[-1][-1]

    def uniquePaths_3(self, m: int, n: int) -> int:
        """排列组合。从左上角走到右下角的过程中，需要向右走n-1步 以及 向下走m-1步，因此总共需要走m+n-2步。这其实就是个数学组合问题，
        从m+n-2步中选出m-1步向下走。
        排列(Arrangement、Permutation)，用A表示。组合(Combination)，用C表示。A 和 C 的本质区别在于：决策的顺序对结果有没有影响，顺序重不重要，打乱顺序是否影响最终结果。
        Arrangement：将3个奖牌(金牌/银牌/铜牌)颁发给8个人中的3个，有多少种不同的颁奖方式？很明显是一个排列的问题，因为先把金牌给a，再把银牌给b；跟先把金牌给b，再把银牌给a，
        这是两种不同的颁奖方式。第一步：颁发金牌，可以从8个人中任选一个，有8种选择；第二步：颁发银牌，可以从剩余的7个人中任选一个，有7种选择。
        第三步：颁发铜牌，从剩余的6个人中任选一个，有6种选择。因此总的颁奖方式有：8 * 7 * 6 = 8! / 5! = 8! / (8-3)!
        因此得到排列的计算公式：A(n,k) = n! / (n-k)!
        Combination：对上面的问题稍作修改，将3瓶同样的可乐颁发给8个人中的3个，此时变为一个组合问题，因为无论谁先得，谁后得，结果都是一样的。
        前面排列的结果已经把不同颁发顺序视作不同颁发方法了，而对组合而言，颁发顺序已经不重要了！因此可以在前面排列结果的基础上，除去不同颁发顺序的总数，便可得到组合的结果。
        不同颁发顺序的总数为：3! ，因此组合的结果为：8! / ((8-3)! * 3!)
        因此得到组合的计算公式：C(n,k) = n! / ((n-k)! * k!)
        """
        # 此问题要求解的是：C(m+n-2,m-1) = (m+n-2)! / ((n-1)! * (m-1)!)。因为n-1、m-1都小于等于m+n-2，
        # 所以先在数组factorial中存储从0~m+n-2的阶乘结果，总共有m+n-1个元素。0 和 1 的阶乘都为1
        factorial = [1, 1]
        for i in range(2, m + n - 1):
            factorial.append(factorial[i - 1] * i)
        return factorial[m + n - 2] // (factorial[n - 1] * factorial[m - 1])

    def uniquePaths_4(self, m: int, n: int) -> int:
        """对 C(m+n-2,m-1) = (m+n-2)! / ((n-1)! * (m-1)!) 进一步优化，因为n-1、m-1都小于等于m+n-2，
        所以 C(m+n-2,m-1) = (m+n−2) * (m+n−3) * …… * n / (m-1)!
        """
        # 交换行列的值，并不影响此题的答案。这里是为了进一步降低时间复杂度，降为 O(min(m,n))。空间复杂度为O(1)
        if n < m:
            return self.uniquePaths_4(n, m)
        # 分子(Numerator)，分母(Denominator)
        Numerator = Denominator = 1
        # n + 0 ——> n + m-2，1 ——> m-1，都需要走m-1步
        for i in range(m - 1):
            Numerator *= n + i
            Denominator *= i + 1
        return Numerator // Denominator


if __name__ == '__main__':
    print(Solution().uniquePaths_4(m=3, n=7))
