# -*- coding: utf-8 -*-
# @date: 2023/4/6
# @author: liuquan
"""
title: 二进制转换
Given an integer n, return a binary string representing its representation in base -2.
Note that the returned string should not have leading zeros unless the string is "0".


Example 1:
Input: n = 2
Output: "110"
Explantion: (-2)^2 + (-2)^1 = 2

Example 2:
Input: n = 3
Output: "111"
Explantion: (-2)^2 + (-2)^1 + (-2)^0 = 3

Example 3:
Input: n = 4
Output: "100"
Explantion: (-2)^2 = 4


Constraints:
0 <= n <= 10^9
"""


class Solution:
    def baseNeg2(self, n: int) -> str:
        """
        模拟
        假设n的二进制表示为：11011 ——> 2^4 + 2^3 + 2^1 + 2^0
        转换为-2进制后：(-2)^4 + (-2)^3 + (-2)^1 + (-2)^0 = 2^4 - 2^3 - 2^1 + 2^0
        即 从低位到高位遍历时，当下标i为奇数时，减去了 2^i
        以处理下标1为例，此时res = [1, 1] 表示(-2)^0 + (-2)^1，因为减去了 2^1，所以要给n加回 2^1，即 11011 + 00010 = 11101
        可见，对于已处理完的低位(下标0)没有影响，加回 2^1 之后，下标0的值依旧还是1，影响的只是还未开始处理的高位
        此时n的下标2从最初的0变为了1，因此 res = [1, 1, 1] 表示(-2)^0 + (-2)^1 + (-2)^2
        """
        if n == 0:
            return '0'
        res = []
        i = 0
        while n > 0:
            if n & 1:
                res.append('1')
                # 这里的下标i只是用来判断奇偶，因此也可换成bool值
                if i & 1:
                    n += 1
            else:
                res.append('0')
            n >>= 1
            i += 1
        return ''.join(res[::-1])


if __name__ == '__main__':
    print(Solution().baseNeg2(3))
