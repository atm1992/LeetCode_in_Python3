# -*- coding: UTF-8 -*-
"""
title: 逆波兰表达式求值
Evaluate the value of an arithmetic expression in Reverse Polish Notation.
Valid operators are +, -, *, and /. Each operand may be an integer or another expression.
Note that division between two integers should truncate toward zero.
It is guaranteed that the given RPN expression is always valid. That means the expression would always evaluate to a result, and there will not be any division by zero operation.


Example 1:
Input: tokens = ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9

Example 2:
Input: tokens = ["4","13","5","/","+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6

Example 3:
Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
Output: 22
Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22


Constraints:
1 <= tokens.length <= 10^4
tokens[i] is either an operator: "+", "-", "*", or "/", or an integer in the range [-200, 200].
"""
from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """使用栈，若遇到"+", "-", "*", or "/"，则将前两个数出栈，然后再将计算结果入栈"""
        stack = []
        for ch in tokens:
            if ch in ['+', '-', '*', '/']:
                b = stack.pop()
                a = stack.pop()
                if ch == '+':
                    stack.append(a + b)
                elif ch == '-':
                    stack.append(a - b)
                elif ch == '*':
                    stack.append(a * b)
                else:
                    # 注意：对Python而言，这里不能直接用 a//b，因为Python中的负数除法结果与日常情况不太一样，6 // -13 == -6 // 13 == -1，正常情况下，结果应该为0
                    stack.append(int(a / b))
            else:
                stack.append(int(ch))
        return stack.pop()


if __name__ == '__main__':
    print(Solution().evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))
