# -*- coding: UTF-8 -*-
"""
title: 剪绳子
给你一根长度为 n 的绳子，请把绳子剪成整数长度的 m 段（m、n都是整数，n>1并且m>1），每段绳子的长度记为 k[0],k[1]...k[m-1] 。请问 k[0]*k[1]*...*k[m-1] 可能的最大乘积是多少？例如，当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，此时得到的最大乘积是18。


示例 1：
输入: 2
输出: 1
解释: 2 = 1 + 1, 1 × 1 = 1

示例 2:
输入: 10
输出: 36
解释: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36


提示：
2 <= n <= 58
"""


class Solution:
    def cuttingRope(self, n: int) -> int:
        res = 0
        for m in range(2, n + 1):
            average_size, extra_size = divmod(n, m)
            tmp = [average_size] * m
            for i in range(extra_size):
                tmp[i] += 1
            tmp_res = 1
            for item in tmp:
                tmp_res *= item
            if tmp_res <= res:
                break
            res = tmp_res
        return res


if __name__ == '__main__':
    print(Solution().cuttingRope(10))
