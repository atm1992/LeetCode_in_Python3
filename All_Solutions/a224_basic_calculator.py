# -*- coding: UTF-8 -*-
"""
title: 基本计算器
Given a string s representing a valid expression, implement a basic calculator to evaluate it, and return the result of the evaluation.
Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().


Example 1:
Input: s = "1 + 1"
Output: 2

Example 2:
Input: s = " 2-1 + 2 "
Output: 3

Example 3:
Input: s = "(1+(4+5+2)-3)+(6+8)"
Output: 23


Constraints:
1 <= s.length <= 3 * 10^5
s consists of digits, '+', '-', '(', ')', and ' '.
s represents a valid expression.
'+' is not used as a unary operation (i.e., "+1" and "+(2 + 3)" is invalid).
'-' could be used as a unary operation (i.e., "-1" and "-(2 + 3)" is valid).
There will be no two consecutive operators in the input.
Every number and running calculation will fit in a signed 32-bit integer.
"""


class Solution:
    def calculate(self, s: str) -> int:
        """栈"""
        stack = []
        n = len(s)
        idx = 0
        while idx < n:
            ch = s[idx]
            if ch in ['(', '-']:
                stack.append(ch)
            elif ch == ')':
                tmp_sum = 0
                while stack[-1] != '(':
                    tmp = stack.pop()
                    if stack[-1] == '-':
                        tmp = 0 - tmp
                        # pop '-'
                        stack.pop()
                    tmp_sum += tmp
                # pop '('
                stack.pop()
                stack.append(tmp_sum)
            elif ch not in ['+', '-', '(', ')', ' ']:
                tmp = 0
                # 避免数字内部存在 ' '
                while idx + 1 < n and s[idx + 1] not in ['+', '-', '(', ')']:
                    if s[idx] != ' ':
                        tmp = tmp * 10 + int(s[idx])
                    idx += 1
                if s[idx] != ' ':
                    tmp = tmp * 10 + int(s[idx])
                stack.append(tmp)
            idx += 1
        res = 0
        while stack:
            tmp = stack.pop()
            if stack and stack[-1] == '-':
                tmp = 0 - tmp
                # pop '-'
                stack.pop()
            res += tmp
        return res

    def calculate_2(self, s: str) -> int:
        """
        栈。使用一个栈ops来记录当前最新的符号，遇到 + ，sign直接取栈顶符号；符号 - ，sign为栈顶符号取反。
        例如：-(32 -5) == -32 + 5
        从左到右扫描 -(3-5-(4-7))：
        1、遇到 - ，sign变为-1，ops 依旧为 [1]
        2、遇到 ( ，sign依旧为-1，ops变为 [1, -1]
        3、遇到 32 ，取出32，再乘以sign(-1)，变为-32，加到res中，res = -32
        4、遇到 - ，- ops[-1] == 1，因此sign变为1，ops变为 [1, -1]
        5、遇到 5 ，取出5，再乘以sign(1)，变为5，加到res中，res = -32 + 5 = -27
        6、遇到 ) ，sign依旧为1，ops变为 [1]
        """
        ops = [1]
        sign = 1
        res = 0
        n = len(s)
        idx = 0
        while idx < n:
            ch = s[idx]
            if ch == '+':
                sign = ops[-1]
            elif ch == '-':
                sign = - ops[-1]
            elif ch == '(':
                ops.append(sign)
            elif ch == ')':
                ops.pop()
            elif ch not in ['+', '-', '(', ')', ' ']:
                tmp = 0
                # 避免数字内部存在 ' '
                while idx + 1 < n and s[idx + 1] not in ['+', '-', '(', ')']:
                    if s[idx] != ' ':
                        tmp = tmp * 10 + int(s[idx])
                    idx += 1
                if s[idx] != ' ':
                    tmp = tmp * 10 + int(s[idx])
                res += tmp * sign
            idx += 1
        return res


if __name__ == '__main__':
    print(Solution().calculate_2("(1+(4+5 3 4  3+2)-3)+(6+8)"))
