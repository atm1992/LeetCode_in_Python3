# -*- coding: UTF-8 -*-
"""
title: 3 的幂
Given an integer n, return true if it is a power of three. Otherwise, return false.
An integer n is a power of three, if there exists an integer x such that n == 3^x.


Example 1:
Input: n = 27
Output: true

Example 2:
Input: n = 0
Output: false

Example 3:
Input: n = 9
Output: true


Constraints:
-2^31 <= n <= 2^31 - 1

Follow up: Could you solve it without loops/recursion?
"""


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        """因为n是整数，所以无需考虑3的负数次幂，因为所有的3的负数次幂都是介于0~1之间的小数"""
        if n < 1:
            return False
        while n % 3 == 0:
            n //= 3
        return n == 1

    def isPowerOfThree_2(self, n: int) -> bool:
        """因为n的最大值为 2^31 - 1，在这个范围内，最大的 3 的幂为 3^19 = 1162261467，因此只需判断输入的n是否为1162261467的约数即可"""
        if n < 1:
            return False
        return 1162261467 % n == 0


if __name__ == '__main__':
    print(Solution().isPowerOfThree(1))
