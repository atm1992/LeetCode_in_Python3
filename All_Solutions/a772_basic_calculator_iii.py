# -*- coding: UTF-8 -*-
"""
title: 基本计算器 III
Implement a basic calculator to evaluate a simple expression string.
The expression string contains only non-negative integers, '+', '-', '*', '/' operators, and open '(' and closing parentheses ')'. The integer division should truncate toward zero.
You may assume that the given expression is always valid. All intermediate results will be in the range of [-2^31, 2^31 - 1].
Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().


Example 1:
Input: s = "1+1"
Output: 2

Example 2:
Input: s = "6-4/2"
Output: 4

Example 3:
Input: s = "2*(5+5*2)/3+(6/2+8)"
Output: 21


Constraints:
1 <= s <= 10^4
s consists of digits, '+', '-', '*', '/', '(', and ')'.
s is a valid expression.
"""


class Solution:
    def calculate(self, s: str) -> int:
        """
        栈。将人们日常的中缀表达式转换为计算器的逆波兰表达式(后缀表达式)。
        注意：本方法默认所有运算符均为二元操作符，因此无法处理'-'为一元操作符的情况，不过本题将这些情况认为是无效的表达式
        """

        def helper(num1: int, num2: int, opt: str) -> int:
            if opt == '+':
                return num1 + num2
            elif opt == '-':
                return num1 - num2
            elif opt == '*':
                return num1 * num2
            else:
                # Python中的负数整除与常规情况不太一样，例如："(0-3)/4"
                return int(num1 / num2)

        stack_opt, stack_num = [], []
        i, n = 0, len(s)
        # ')' 不会入栈stack_opt
        priority = {'(': 0, '+': 1, '-': 1, '*': 2, '/': 2}
        while i < n:
            ch = s[i]
            if ch.isdigit():
                j = i
                while i + 1 < n and s[i + 1].isdigit():
                    i += 1
                # 因为本题无需考虑空格的情况
                stack_num.append(int(s[j:i + 1]))
            elif ch == '(':
                stack_opt.append(ch)
            elif ch == ')':
                while stack_opt[-1] != '(':
                    opt = stack_opt.pop()
                    num2 = stack_num.pop()
                    num1 = stack_num.pop()
                    stack_num.append(helper(num1, num2, opt))
                # 退出上述while循环时，stack_opt[-1] == '('
                stack_opt.pop()
            else:
                while stack_opt and priority[stack_opt[-1]] >= priority[ch]:
                    opt = stack_opt.pop()
                    num2 = stack_num.pop()
                    num1 = stack_num.pop()
                    stack_num.append(helper(num1, num2, opt))
                stack_opt.append(ch)
            i += 1

        while stack_opt:
            opt = stack_opt.pop()
            num2 = stack_num.pop()
            num1 = stack_num.pop()
            stack_num.append(helper(num1, num2, opt))
        return stack_num[0]


if __name__ == '__main__':
    print(Solution().calculate("(0-3)/4"))
