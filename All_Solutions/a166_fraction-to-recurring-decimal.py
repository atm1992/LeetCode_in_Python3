# -*- coding: UTF-8 -*-
"""
title: 分数到小数
Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.
If the fractional part is repeating, enclose the repeating part in parentheses.
If multiple answers are possible, return any of them.
It is guaranteed that the length of the answer string is less than 10^4 for all the given inputs.


Example 1:
Input: numerator = 1, denominator = 2
Output: "0.5"

Example 2:
Input: numerator = 2, denominator = 1
Output: "2"

Example 3:
Input: numerator = 4, denominator = 333
Output: "0.(012)"


Constraints:
-2^31 <= numerator, denominator <= 2^31 - 1
denominator != 0
"""


class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        """长除法"""
        # 排除可以直接整除 以及 分子为0 的情况
        if numerator % denominator == 0:
            return str(numerator // denominator)
        # 初始值使用空数组，而不是直接使用空字符串，是为了方便后面insert '('
        res = []
        # 使用异或计算，获取结果的正负性
        if (numerator < 0) ^ (denominator < 0):
            res.append('-')

        numerator, denominator = abs(numerator), abs(denominator)
        # 获取整数部分
        res.append(str(numerator // denominator))
        res.append('.')

        # 获取小数部分
        idx_map = {}
        remainder = numerator % denominator
        # 退出循环时，若remainder不为0，则表示最终结果为无限循环小数；若remainder为0，则表示最终结果为有限小数
        while remainder and remainder not in idx_map:
            # 记录当前小数处于最终结果中的位置。例如：12.345345，第一位小数3位于结果中的第4个位置，索引下标为3
            idx_map[remainder] = len(res)
            remainder *= 10
            res.append(str(remainder // denominator))
            remainder %= denominator
        if remainder:
            idx = idx_map[remainder]
            res.insert(idx, '(')
            res.append(')')
        return ''.join(res)


if __name__ == '__main__':
    print(Solution().fractionToDecimal(numerator=4, denominator=333))
