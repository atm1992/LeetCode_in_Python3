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
        if len(a) < len(b):
            return self.addBinary(b, a)
        res = list(a)
        a_idx, b_idx = len(a) - 1, len(b) - 1
        carry = '0'
        while b_idx >= 0:
            if res[a_idx] == b[b_idx]:
                res[a_idx] = carry
                carry = b[b_idx]
            else:
                res[a_idx] = '1' if carry == '0' else '0'
            a_idx -= 1
            b_idx -= 1
        while a_idx >= 0:
            if res[a_idx] == carry:
                res[a_idx] = '0'
            else:
                res[a_idx] = '1'
                carry = '0'
            if carry == '0':
                break
            a_idx -= 1
        if carry == '1':
            res.insert(0, '1')
        return ''.join(res)

    def addBinary_2(self, a: str, b: str) -> str:
        x, y = int(a, 2), int(b, 2)
        while y:
            res = x ^ y
            carry = (x & y) << 1
            x, y = res, carry
        return bin(x)[2:]


if __name__ == '__main__':
    print(Solution().addBinary(a="1010", b="1011"))
