# -*- coding: UTF-8 -*-
"""
title: 统计理想数组的数目
You are given two integers n and maxValue, which are used to describe an ideal array.
A 0-indexed integer array arr of length n is considered ideal if the following conditions hold:
    Every arr[i] is a value from 1 to maxValue, for 0 <= i < n.
    Every arr[i] is divisible by arr[i - 1], for 0 < i < n.
Return the number of distinct ideal arrays of length n. Since the answer may be very large, return it modulo 10^9 + 7.


Example 1:
Input: n = 2, maxValue = 5
Output: 10
Explanation: The following are the possible ideal arrays:
- Arrays starting with the value 1 (5 arrays): [1,1], [1,2], [1,3], [1,4], [1,5]
- Arrays starting with the value 2 (2 arrays): [2,2], [2,4]
- Arrays starting with the value 3 (1 array): [3,3]
- Arrays starting with the value 4 (1 array): [4,4]
- Arrays starting with the value 5 (1 array): [5,5]
There are a total of 5 + 2 + 1 + 1 + 1 = 10 distinct ideal arrays.

Example 2:
Input: n = 5, maxValue = 3
Output: 11
Explanation: The following are the possible ideal arrays:
- Arrays starting with the value 1 (9 arrays):
   - With no other distinct values (1 array): [1,1,1,1,1]
   - With 2nd distinct value 2 (4 arrays): [1,1,1,1,2], [1,1,1,2,2], [1,1,2,2,2], [1,2,2,2,2]
   - With 2nd distinct value 3 (4 arrays): [1,1,1,1,3], [1,1,1,3,3], [1,1,3,3,3], [1,3,3,3,3]
- Arrays starting with the value 2 (1 array): [2,2,2,2,2]
- Arrays starting with the value 3 (1 array): [3,3,3,3,3]
There are a total of 9 + 1 + 1 = 11 distinct ideal arrays.


Constraints:
2 <= n <= 10^4
1 <= maxValue <= 10^4
"""


class Solution:
    def idealArrays(self, n: int, maxValue: int) -> int:
        """
        数论
        分别考虑以x结尾长度为n的理想数组有多少个，数组结尾可以是1 ~ maxValue，因此把这些情况累加，就是最终结果。
        以结尾为4、长度为5进行分析：
        4的前面可以是4、2、1， 2的前面可以是2、1， 1的前面只能是1。例如：
        [1, 2, 2, 4, 4]
        [1, 1, 1, 4, 4]
        [2, 2, 2, 4, 4]
        [4, 4, 4, 4, 4]
        以[1, 2, 2, 4, 4]为例，可以记为 [_, *2, _, *2, _]，只需记录在哪些位置的元素发生了改变(倍增)，
        从当前倍增的位置开始 ~ 下一次倍增的位置之前(或数组结尾)，将会一直维持这个值。
        可假设每个数组的开头前面有一个值1，若数组中的第一个元素为1，则没有发生倍增；若第一个元素不是1，则发生了倍增。
        例如：[2, 2, 2, 4, 4] 可表示为 [*2, _, _, *2, _]；
        在同一个位置可以发生多次倍增，例如：[1, 1, 1, 4, 4] 可表示为 [_, _, _, *2*2, _]；[4, 4, 4, 4, 4] 可表示为 [*2*2, _, _, _, _]。
        由于固定了结尾为4，而4的质因子为2、2，即 4 = (1) * 2 * 2
        所有结尾为4、长度为5的理想数组，问题可转化为 结尾数字(4)的质因子可以放在哪些位置，当前有5个不同的位置，2个质因子2，
        从5个位置中选择一个(将2个2放在一个位置)或两个(将2个2放在不同位置)，因为2个2是相同的，谁先谁后，结果都是一样的。所以这是个组合问题。
        问题进一步转化为：把k个相同的小球放进n个不同的盒子中，允许有些盒子为空，也允许一个盒子中放入多个小球，有多少种不同的放法？
        该问题可用隔板法来求解，把n个盒子当做n-1个隔板，然后加上k个小球，相当于总共有 n-1 + k 个位置，从中选出n-1个位置放隔板，
        即方案数为：C(n-1+k)(n-1)
        由于maxValue <= 10^4，质因子最小为2，2^13 = 8192 < 10^4 < 16384 = 2^14，质因子越大，质因子的个数将会越小，
        所以质因子为2时，质因子的个数k才能达到最大值13，即 k <= 13。所以上面的 C(n-1+k)(n-1) 可写为 C(n-1+k)(k) ，k 显然远小于n-1.
        若结尾数字由多个不同的质因子组成，例如：k1个2、k2个3、k3个5，则可将问题分解为：
        1、从n-1 + k1个位置中选出k1个位置放质因子2，得到 C(n-1+k1)(k1)
        2、从n-1 + k2个位置中选出k2个位置放质因子3，得到 C(n-1+k2)(k2)
        3、从n-1 + k3个位置中选出k3个位置放质因子5，得到 C(n-1+k3)(k3)
        这3种情况之间互不影响：放质因子5的时候，不用关心这个位置之前放没放过2、3，以及放了多少个2、多少个3。
        所以可采用乘法原理来计算最终结果：C(n-1+k1)(k1) * C(n-1+k2)(k2) * C(n-1+k3)(k3)

        综上，原问题最终转化为：质因数分解出所有的质因子及其个数(其实只关注个数k) + 计算组合数问题
        计算组合数问题 可用动态规划进行计算，假设dp[i][j] 表示从i个位置中选择j个，即 C(i)(j)。该问题可分为两种情况：
        1、选择了位置i，则只需再从i-1个位置中选择j-1个，即 C(i-1)(j-1)
        2、未选择位置i，则需要从i-1个位置中选择j个，即 C(i-1)(j)
        所以，dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
        """
        mod = 10 ** 9 + 7
        max_k = 13
        # n-1+13 +1
        max_n = n + max_k
        dp = [[0] * (max_k + 1) for _ in range(max_n)]
        # 初始值，从0个位置中选出0个，只有一种方案
        dp[0][0] = 1
        # 预处理出 1 ~ n-1+13 的所有组合数
        for i in range(1, max_n):
            # 从任意个位置中选出0个，都只有一种方案
            dp[i][0] = 1
            for j in range(1, min(i, max_k) + 1):
                dp[i][j] = (dp[i - 1][j - 1] + dp[i - 1][j]) % mod

        # 预处理 2 ~ maxValue 的所有数x，将这些数分解出所有的质因子，然后记录各个质因子的个数k。
        # 由于并不关心个数k具体对应哪个质因子，所以使用数组记录个数k即可，而无需使用字典记录 个数k ——> 质因子
        ks = [[] for _ in range(maxValue + 1)]
        for i in range(2, maxValue + 1):
            # 质因子p从2开始：2、3、5、7、……
            p, x = 2, i
            # 不用担心会记录质因子4的个数，质因子4的个数一定为0，因为能被4整除，就一定能被2整除，x先被2整除过若干次后，直到不能被2整除，
            # 质因子p才会加1变成3，等质因子p加1变成4时，x都已经无法被2整除了，那就更不可能被4整除了，可理解为被2榨干了
            while p * p <= x:
                if x % p == 0:
                    k = 0
                    while x % p == 0:
                        k += 1
                        x //= p
                    ks[i].append(k)
                p += 1
            if x > 1:
                # 若最后榨完的x还大于1，则说明最后剩余的x本身就是个质因子，该质因子的个数为1
                ks[i].append(1)

        res = 0
        # 理想数组的结尾数字x可以为 [1, maxValue] 中的任意值
        for x in range(1, maxValue + 1):
            mul = 1
            # x为1时，由于1不存在质因子，所以ks[1]为空数组。长度为n、结尾数字为1的理想数组只有1个，即 全1数组
            for k in ks[x]:
                mul = mul * dp[n - 1 + k][k] % mod
            res = (res + mul) % mod
        return res
