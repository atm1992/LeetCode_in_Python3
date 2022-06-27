# -*- coding: UTF-8 -*-
"""
title: 4的幂
Given an integer n, return true if it is a power of four. Otherwise, return false.
An integer n is a power of four, if there exists an integer x such that n == 4x.


Example 1:
Input: n = 16
Output: true

Example 2:
Input: n = 5
Output: false

Example 3:
Input: n = 1
Output: true


Constraints:
-2^31 <= n <= 2^31 - 1

Follow up: Could you solve it without loops/recursion?
"""


class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        """二进制表示中 1 的位置。如果 n 是 4 的幂，那么 n 的二进制表示中有且只有一个 1，并且这个 1 的下标为偶数(下标从0开始)"""
        # ​10101010101010101010101010101010，n <= 2^31 - 1
        mask = 0xaaaaaaaa
        # 4 的幂一定是正数
        return n > 0 and n & (n - 1) == 0 and n & mask == 0

    def isPowerOfFour_2(self, n: int) -> bool:
        """
        取模
        以4^a为例，4^a = (3 + 1)^a，使用二项式定理展开后，除了最后一项 1^a == 1以外的其余所有项都是3的倍数，所以 4^a % 3 == 1
        如果n是2的幂(这个幂必须是奇数，如果是偶数，则此时的n也是4的幂)，n = 2^a = 2 * 4 ^ (a//2) = 2 * (3 + 1)^b，由上分析可知，这个数对3取余的结果为2
        """
        return n > 0 and n & (n - 1) == 0 and n % 3 == 1


if __name__ == '__main__':
    print(Solution().isPowerOfFour_2(256))
