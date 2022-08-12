# -*- coding: UTF-8 -*-
"""
title: 阶乘后的零
Given an integer n, return the number of trailing zeroes in n!.
Note that n! = n * (n - 1) * (n - 2) * ... * 3 * 2 * 1.


Example 1:
Input: n = 3
Output: 0
Explanation: 3! = 6, no trailing zero.

Example 2:
Input: n = 5
Output: 1
Explanation: 5! = 120, one trailing zero.

Example 3:
Input: n = 0
Output: 0


Constraints:
0 <= n <= 10^4

Follow up: Could you write a solution that works in logarithmic time complexity?
"""


class Solution:
    def trailingZeroes(self, n: int) -> int:
        """统计2、5的个数，不过2的个数肯定会大于5的个数，所以直接统计5的个数就行"""
        res = 0
        for i in range(5, n + 1, 5):
            while i % 5 == 0:
                res += 1
                i //= 5
        return res

    def trailingZeroes_2(self, n: int) -> int:
        """优化计算。直接使用输入的n来统计5的个数，[1, n]中p的倍数有a1 = n//p个，这些数至少贡献出了a1个质因子p。
        同理，p^2的倍数有a2 = n//p^2个，由于这些数已经是 p 的倍数了，为了不重复统计 p 的个数，我们仅考虑额外贡献的质因子个数，
        即这些数额外贡献了至少a2个质因子 p。即 统计p^2的倍数时，由于前面统计p的倍数时已经将该数算入了一次，所以只需算入额外的一次就行；
        同理，统计p^3的倍数时，由于前面统计p的倍数以及p^2的倍数时已经将该数分别算入了一次，所以也只需再算入额外的一次就行"""
        res = 0
        while n:
            n //= 5
            res += n
        return res


if __name__ == '__main__':
    print(Solution().trailingZeroes(10))
