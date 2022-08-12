# -*- coding: UTF-8 -*-
"""
title: 字符串相加
Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.
You must solve the problem without using any built-in library for handling large integers (such as BigInteger). You must also not convert the inputs to integers directly.


Example 1:
Input: num1 = "11", num2 = "123"
Output: "134"

Example 2:
Input: num1 = "456", num2 = "77"
Output: "533"

Example 3:
Input: num1 = "0", num2 = "0"
Output: "0"


Constraints:
1 <= num1.length, num2.length <= 10^4
num1 and num2 consist of only digits.
num1 and num2 don't have any leading zeros except for the zero itself.
"""


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        """模拟竖式加法"""
        carry = 0
        idx1 = len(num1) - 1
        idx2 = len(num2) - 1
        res = []
        while idx1 >= 0 or idx2 >= 0 or carry > 0:
            n1 = ord(num1[idx1]) - ord('0') if idx1 >= 0 else 0
            n2 = ord(num2[idx2]) - ord('0') if idx2 >= 0 else 0
            _sum = n1 + n2 + carry
            res.append(str(_sum % 10))
            carry = _sum // 10
            idx1 -= 1
            idx2 -= 1
        return ''.join(res[::-1])


if __name__ == '__main__':
    print(Solution().addStrings(num1="456", num2="77"))
