# -*- coding: UTF-8 -*-
"""
title: 为运算表达式设计优先级
Given a string expression of numbers and operators, return all possible results from computing all the different possible ways to group numbers and operators. You may return the answer in any order.


Example 1:
Input: expression = "2-1-1"
Output: [0,2]
Explanation:
((2-1)-1) = 0
(2-(1-1)) = 2

Example 2:
Input: expression = "2*3-4*5"
Output: [-34,-14,-10,-10,10]
Explanation:
(2*(3-(4*5))) = -34
((2*3)-(4*5)) = -14
((2*(3-4))*5) = -10
(2*((3-4)*5)) = -10
(((2*3)-4)*5) = 10


Constraints:
1 <= expression.length <= 20
expression consists of digits and the operator '+', '-', and '*'.
All the integer values in the input expression are in the range [0, 99].
"""
from typing import List


class Solution:
    def __init__(self):
        # key 为子表达式字符串，value 为计算结果列表
        self.memo = {}

    def diffWaysToCompute(self, expression: str) -> List[int]:
        """记忆化递归(记忆化搜索)"""
        if expression.isdigit():
            return [int(expression)]
        if expression in self.memo:
            return self.memo[expression]
        res = []
        for idx, ch in enumerate(expression):
            if ch in '+-*':
                left_res = self.diffWaysToCompute(expression[:idx])
                right_res = self.diffWaysToCompute(expression[idx + 1:])
                for left in left_res:
                    for right in right_res:
                        if ch == '+':
                            res.append(left + right)
                        elif ch == '-':
                            res.append(left - right)
                        else:
                            res.append(left * right)
        self.memo[expression] = res
        return res


if __name__ == '__main__':
    print(Solution().diffWaysToCompute("2*3-4*5"))
