# -*- coding: UTF-8 -*-
"""
title: 计数质数
Given an integer n, return the number of prime numbers that are strictly less than n.


Example 1:
Input: n = 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.

Example 2:
Input: n = 0
Output: 0

Example 3:
Input: n = 1
Output: 0


Constraints:
0 <= n <= 5 * 10^6
"""


class Solution:
    def countPrimes(self, n: int) -> int:
        """
        埃氏筛(厄拉多塞筛法)。如果 x 是质数，那么大于 x 的 x 的倍数 2x,3x,… 一定不是质数
        """
        is_prime = [1] * n
        res = 0
        for i in range(2, n):
            if is_prime[i] == 1:
                res += 1
                tmp = i * 2
                while tmp < n:
                    is_prime[tmp] = 0
                    tmp += i
        return res


if __name__ == '__main__':
    print(Solution().countPrimes(10))
