# -*- coding: UTF-8 -*-
"""
title: 最小因式分解
Given a positive integer num, return the smallest positive integer x whose multiplication of each digit equals num. If there is no answer or the answer is not fit in 32-bit signed integer, return 0.


Example 1:
Input: num = 48
Output: 68

Example 2:
Input: num = 15
Output: 35


Constraints:
1 <= num <= 2^31 - 1
"""


class Solution:
    def smallestFactorization(self, num: int) -> int:
        """
        贪心 + 因式分解。
        从因数9到因数2逐步分解num，注意：并不是质因数分解。
        根据测试结果发现，若num只有一位数，则直接返回num本身，而不是返回 10 + num
        """
        if num < 10:
            return num
        res, weight = 0, 1
        for f in range(9, 1, -1):
            while num % f == 0:
                num //= f
                # 因为是倒序从9分解到2，所以越往后的因数在res中应该越靠左，这样才能使res最小
                res += weight * f
                weight *= 10
                if res > 2 ** 31 - 1:
                    return 0
            if num == 1:
                return res
        # num无法完全被9到2分解
        return 0


if __name__ == '__main__':
    print(Solution().smallestFactorization(13))
