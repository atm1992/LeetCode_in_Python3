# -*- coding: UTF-8 -*-
"""
title: 二进制求和
Given two binary strings a and b, return their sum as a binary string.


Example 1:
Input: a = "11", b = "1"
Output: "100"

Example 2:
Input: a = "1010", b = "1011"
Output: "10101"


Constraints:
1 <= a.length, b.length <= 10^4
a and b consist only of '0' or '1' characters.
Each string does not contain leading zeros except for the zero itself.
"""


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        """模拟"""
        if len(a) < len(b):
            return self.addBinary(b, a)
        m, n = len(a), len(b)
        res = []
        carry = 0
        for i in range(m):
            carry += int(a[m - 1 - i])
            carry += int(b[n - 1 - i]) if i < n else 0
            res.append(str(carry & 1))
            carry >>= 1
        if carry > 0:
            res.append('1')
        return ''.join(res[::-1])

    def addBinary_2(self, a: str, b: str) -> str:
        x, y = int(a, 2), int(b, 2)
        while y:
            x, y = x ^ y, (x & y) << 1
        return bin(x)[2:]


if __name__ == '__main__':
    print(Solution().addBinary(a="1010", b="1011"))
