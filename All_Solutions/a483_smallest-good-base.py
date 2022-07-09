# -*- coding: UTF-8 -*-
"""
title: 最小好进制
Given an integer n represented as a string, return the smallest good base of n.
We call k >= 2 a good base of n, if all digits of n base k are 1's.


Example 1:
Input: n = "13"
Output: "3"
Explanation: 13 base 3 is 111.

Example 2:
Input: n = "4681"
Output: "8"
Explanation: 4681 base 8 is 11111.

Example 3:
Input: n = "1000000000000000000"
Output: "999999999999999999"
Explanation: 1000000000000000000 base 999999999999999999 is 11.


Constraints:
n is an integer in the range [3, 10^18].
n does not contain any leading zeros.
"""
import math


class Solution:
    def smallestGoodBase(self, n: str) -> str:
        """
        数学
        假设n由m+1位k进制的1组成，即 n = k^0 + k^1 + …… + k^m
        因为 n >= 3，所以 m至少为1，k至少为2
        k^0 + k^1 + …… + k^m 可用等比数列求和公式算得：n = (k^(m+1) - 1) / (k - 1)
        公式变换后：k^(m+1) = kn - n + 1 < kn，因为 n >= 3
        移项并化简后：m < logk(n)，k为底数
        由于 k >= 2，且 n <= 10^18 = 1000^6 < 1024^6 = 2^60，所以 m < 60。最终得到m的取值范围：[1, 60)
        当m为1时，n = k^0 + k^1 = 1 + k，即 k = n - 1，此时的k为最大取值，这也确保了k一定存在，k的取值范围：[2, n-1]

        根据二项式定理，(k+1)^m = Cm0 * k^0 + Cm1 * k^1 + …… + Cmm * k^m = k^0 + Cm1 * k^1 + …… + k^m > k^0 + k^1 + …… + k^m > k^m
        即 (k+1)^m > n > k^m， ==> k+1 > n ** (1/m) > k
        可知，n ** (1/m) 是一个介于k和k+1之间的小数，这个小数的整数部分就是所求的k
        可以通过逐步增大k的方式来验证是否存在可行的m，若存在可行的m，则当前的k就是最小好进制。
        但由于k的取值范围为[2, n-1]，而m的取值范围为[1, 60)，所以选择枚举m，对于一个确定的n，k越大，m越小；反之，m越大，k越小。
        所以选择从m的最大取值int(log2(n))开始逐步减小m，直到m为2，来验证是否存在可行的k，找到的第一个可行k，就是最小好进制。
        m为1时，k一定存在，此时的k为n-1
        """
        n = int(n)
        max_m = int(math.log2(n))
        for m in range(max_m, 1, -1):
            k = int(n ** (1 / m))
            # 使用等比数列求和公式：k^0 + k^1 + …… + k^m = (k^(m+1) - 1) / (k - 1)
            # 注意：max_m 不能直接取59，那样有可能会使k==1，导致k-1 == 0
            # max_m = int(math.log2(n)) 保证了 k >= 2
            if (k ** (m + 1) - 1) // (k - 1) == n:
                return str(k)
        return str(n - 1)


if __name__ == '__main__':
    print(Solution().smallestGoodBase(n="4681"))
