# -*- coding: UTF-8 -*-
"""
title: 基本计算器 II
Given a string s which represents an expression, evaluate this expression and return its value. 
The integer division should truncate toward zero.
You may assume that the given expression is always valid. All intermediate results will be in the range of [-2^31, 2^31 - 1].
Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().


Example 1:
Input: s = "3+2*2"
Output: 7

Example 2:
Input: s = " 3/2 "
Output: 1

Example 3:
Input: s = " 3+5 / 2 "
Output: 5


Constraints:
1 <= s.length <= 3 * 10^5
s consists of integers and operators ('+', '-', '*', '/') separated by some number of spaces.
s represents a valid expression.
All the integers in the expression are non-negative integers in the range [0, 2^31 - 1].
The answer is guaranteed to fit in a 32-bit integer.
"""


class Solution:
    def calculate(self, s: str) -> int:
        """栈"""
        stack = []
        n = len(s)
        idx = 0
        sign = 1
        while idx < n:
            ch = s[idx]
            if ch == '+':
                sign = 1
            elif ch == '-':
                sign = -1
            elif ch in ['*', '/']:
                left_num = stack.pop()
                idx += 1
                right_num = 0
                # 避免数字内部存在空格。官方答案没有考虑数字内部存在空格的情况
                while idx + 1 < n and s[idx + 1] not in ['+', '-', '*', '/']:
                    if s[idx] != ' ':
                        right_num = right_num * 10 + int(s[idx])
                    idx += 1
                if s[idx] != ' ':
                    right_num = right_num * 10 + int(s[idx])
                # left_num 前面可能是 - 号，从而导致left_num为负数，所以不能写成 left_num // right_num
                num = left_num * right_num if ch == '*' else int(left_num / right_num)
                stack.append(num)
            elif ch.isdigit():
                num = 0
                # 避免数字内部存在空格
                while idx + 1 < n and s[idx + 1] not in ['+', '-', '*', '/']:
                    if s[idx] != ' ':
                        num = num * 10 + int(s[idx])
                    idx += 1
                if s[idx] != ' ':
                    num = num * 10 + int(s[idx])
                stack.append(num * sign)
            idx += 1
        return sum(stack)


if __name__ == '__main__':
    print(Solution().calculate(" 3+5 / 2 "))
