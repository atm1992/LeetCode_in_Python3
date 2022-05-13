# -*- coding: UTF-8 -*-
"""
title: 数字 1 的个数
Given an integer n, count the total number of digit 1 appearing in all non-negative integers less than or equal to n.


Example 1:
Input: n = 13
Output: 6

Example 2:
Input: n = 0
Output: 0


Constraints:
0 <= n <= 10^9
"""


class Solution:
    def countDigitOne(self, n: int) -> int:
        """
        枚举每个数位上1的出现次数。最终结果 = 个位上1的出现次数 + 十位上1的出现次数 + 百位上1的出现次数 + ……
        下面以 n = 23456 ，统计百位上1的出现次数为例进行讲解：
        1、百位上的1，只可能是 100 ~ 199 ，总共100次
        2、23456 // 1000 = 23，100 ~ 199 循环了23次，总共 23 * 100 次
        3、23456 % 1000 = 456，由于 456 > 199，所以1完整的出现了100次
        3.1、若 余数 < 100，则百位上的1出现0次
        3.2、若 100 <= 余数 <= 199，则百位上的1出现 余数 - 100 + 1 次
        3.3、若 余数 > 199，则百位上的1完整出现100次
        公式总结：百位上1的出现次数 = (n // 1000) * 100 + min(max(n % 1000 - 100 + 1, 0), 100)
        公式推广：百位的索引下标为k = 2，所以上式中的1000可写成 10 ^ (k+1)，100可写成 10 ^ k
        """
        res = 0
        # 1 ——> 10 ——> 100 ——> ……
        mul_k = 1
        while n >= mul_k:
            res += (n // (mul_k * 10)) * mul_k + min(max(n % (mul_k * 10) - mul_k + 1, 0), mul_k)
            mul_k *= 10
        return res


if __name__ == '__main__':
    print(Solution().countDigitOne(13))
