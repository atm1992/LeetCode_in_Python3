# -*- coding: UTF-8 -*-
"""
title: 不同骰子序列的数目
You are given an integer n. You roll a fair 6-sided dice n times. Determine the total number of distinct sequences of rolls possible such that the following conditions are satisfied:
    The greatest common divisor of any adjacent values in the sequence is equal to 1.
    There is at least a gap of 2 rolls between equal valued rolls. More formally, if the value of the ith roll is equal to the value of the jth roll, then abs(i - j) > 2.
Return the total number of distinct sequences possible. Since the answer may be very large, return it modulo 10^9 + 7.
Two sequences are considered distinct if at least one element is different.


Example 1:
Input: n = 4
Output: 184
Explanation: Some of the possible sequences are (1, 2, 3, 4), (6, 1, 2, 3), (1, 2, 3, 1), etc.
Some invalid sequences are (1, 2, 1, 3), (1, 2, 3, 6).
(1, 2, 1, 3) is invalid since the first and third roll have an equal value and abs(1 - 3) = 2 (i and j are 1-indexed).
(1, 2, 3, 6) is invalid since the greatest common divisor of 3 and 6 = 3.
There are a total of 184 distinct sequences possible, so we return 184.

Example 2:
Input: n = 2
Output: 22
Explanation: Some of the possible sequences are (1, 2), (2, 1), (3, 2).
Some invalid sequences are (3, 6), (2, 4) since the greatest common divisor is not equal to 1.
There are a total of 22 distinct sequences possible, so we return 22.


Constraints:
1 <= n <= 10^4
"""


class Solution:
    def distinctSequences(self, n: int) -> int:
        """
        三维DP
        dp[i][last][last2] 表示序列长度为 i，最后一个元素为last，倒数第二个元素为last2的序列数目。
        通过枚举last、last2，可以计算出dp[i+1][j][last]
        需满足三个条件：
        1、gcd(j, last) == 1
        2、j != last
        3、j != last2
        累加满足上述三个条件的dp[i][last][last2]，即可得到 dp[i+1][j][last]
        累加dp[-1]二维数组中的所有值，即为最终结果
        """
        if n == 1:
            return 6

        def gcd(a: int, b: int) -> int:
            """辗转相除法，求最大公约数"""
            while b:
                # 若初始时a < b，则第一次while循环时，会将a和b的值进行交换
                a, b = b, a % b
            return a

        mod = 10 ** 9 + 7
        # 骰子值的取值范围为: [1, 6]，避免下标值与骰子值之间的加减1转换，所以range(7)，而不是range(6)
        # 同理，骰子个数的取值范围为: [1, n]，所以range(n+1)，而不是range(n)
        dp = [[[0] * 7 for _ in range(7)] for _ in range(n + 1)]
        for i in range(2, n + 1):
            for j in range(1, 7):
                for last in range(1, 7):
                    if j != last and gcd(j, last) == 1:
                        if i == 2:
                            dp[i][j][last] = 1
                        else:
                            for last2 in range(1, 7):
                                if j != last2:
                                    dp[i][j][last] = (dp[i][j][last] + dp[i - 1][last][last2]) % mod
        res = 0
        for i in range(1, 7):
            for j in range(1, 7):
                res = (res + dp[-1][i][j]) % mod
        return res

    def distinctSequences_2(self, n: int) -> int:
        """动态规划。滚动数组降低空间复杂度"""
        if n == 1:
            return 6

        def gcd(a: int, b: int) -> int:
            """辗转相除法，求最大公约数"""
            while b:
                # 若初始时a < b，则第一次while循环时，会将a和b的值进行交换
                a, b = b, a % b
            return a

        mod = 10 ** 9 + 7
        all_gcd = [[False] * 7 for _ in range(7)]
        # 预处理出所有的最大公约数是否为1
        for i in range(1, 7):
            for j in range(1, 7):
                all_gcd[i][j] = gcd(i, j) == 1

        dp = [[0] * 7 for _ in range(7)]
        for i in range(2, n + 1):
            tmp = [[0] * 7 for _ in range(7)]
            for j in range(1, 7):
                for last in range(1, 7):
                    if j != last and all_gcd[j][last]:
                        if i == 2:
                            tmp[j][last] = 1
                        else:
                            for last2 in range(1, 7):
                                if j != last2:
                                    tmp[j][last] = (tmp[j][last] + dp[last][last2]) % mod
            # 滚动数组
            dp = tmp
        res = 0
        for i in range(1, 7):
            for j in range(1, 7):
                res = (res + dp[i][j]) % mod
        return res


if __name__ == '__main__':
    print(Solution().distinctSequences_2(4))
