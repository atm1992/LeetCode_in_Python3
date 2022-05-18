# -*- coding: UTF-8 -*-
"""
title: 二进制加法
给定两个 01 字符串 a 和 b ，请计算它们的和，并以二进制字符串的形式输出。
输入为 非空 字符串且只包含数字 1 和 0。


示例 1:
输入: a = "11", b = "10"
输出: "101"

示例 2:
输入: a = "1010", b = "1011"
输出: "10101"


提示：
每个字符串仅由字符 '0' 或 '1' 组成。
1 <= a.length, b.length <= 10^4
字符串如果不是 "0" ，就都不含前导零。
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


if __name__ == '__main__':
    print(Solution().addBinary(a="1010", b="10111"))
