# -*- coding: UTF-8 -*-
"""
title: 24 点游戏
You are given an integer array cards of length 4. You have four cards, each containing a number in the range [1, 9]. You should arrange the numbers on these cards in a mathematical expression using the operators ['+', '-', '*', '/'] and the parentheses '(' and ')' to get the value 24.
You are restricted with the following rules:
    The division operator '/' represents real division, not integer division.
        For example, 4 / (1 - 2 / 3) = 4 / (1 / 3) = 12.
    Every operation done is between two numbers. In particular, we cannot use '-' as a unary operator.
        For example, if cards = [1, 1, 1, 1], the expression "-1 - 1 - 1 - 1" is not allowed.
    You cannot concatenate numbers together
        For example, if cards = [1, 2, 1, 2], the expression "12 + 12" is not valid.
Return true if you can get such expression that evaluates to 24, and false otherwise.


Example 1:
Input: cards = [4,1,8,7]
Output: true
Explanation: (8-4) * (7-1) = 24

Example 2:
Input: cards = [1,2,1,2]
Output: false


Constraints:
cards.length == 4
1 <= cards[i] <= 9
"""
from typing import List


class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        """
        回溯
        1、首先从给定的4个数中有序地选出2个，有 4 * 3 = 12 种选法，之所以需要是有序，因为 a - b != b - a。
        再从['+', '-', '*', '/']中选出1种运算符，有 4 种选法。使用运算结果代替刚选出的那2个数，此时剩余3个数
        2、从剩余的3个数中有序地选出2个，有 4 * 3 = 12 种选法。之所以不是直接将上面的运算结果固定为第一个数，再从另外两个数中选出一个，
        是因为()可以改变运算优先级，例如：c / (a - b) * d，若将上面的运算结果(a - b)固定为第一个数，则永远无法实现示例中的运算顺序。
        再从['+', '-', '*', '/']中选出1种运算符，有 4 种选法。使用运算结果代替刚选出的那2个数，此时剩余2个数
        3、从剩余的2个数中有序地选出2个，有 2 种选法。再从['+', '-', '*', '/']中选出1种运算符，有 4 种选法。
        此时的运算结果就是最终结果，判断是否等于24，因为运算中可能存在实数除法，所以最终结果可能是个浮点数，因此需考虑精度误差，误差需小于 10 ^ -6
        优化剪枝：
        1、若选出的运算符为'/'，则除数不能为0
        2、'+', '*' 满足交换律，此时无需考虑参与运算的两个数字间的顺序
        """
        target, precision = 24, 10 ** -6

        def calculate(nums: List[int]) -> bool:
            if len(nums) == 1:
                return abs(nums[0] - target) < precision
            for i, a in enumerate(nums):
                for j, b in enumerate(nums):
                    if i != j:
                        new_nums = []
                        # 先将剩余的数字放入new_nums中
                        for k, c in enumerate(nums):
                            if k not in [i, j]:
                                new_nums.append(c)
                        # 再将a与b的运算结果放入new_nums中，最后将new_nums传入calculate方法中，进行递归回溯
                        for op in ['+', '-', '*', '/']:
                            if op in ['+', '*'] and i > j:
                                continue
                            if op == '+':
                                new_nums.append(a + b)
                            elif op == '-':
                                new_nums.append(a - b)
                            elif op == '*':
                                new_nums.append(a * b)
                            else:
                                # 若除数b等于0
                                if abs(b) < precision:
                                    continue
                                new_nums.append(a / b)
                            if calculate(new_nums):
                                return True
                            # 回溯。将之前append进去的 a与b的运算结果 pop出来，再对a与b进行下一种运算
                            new_nums.pop()
            return False

        return calculate(cards)


if __name__ == '__main__':
    print(Solution().judgePoint24(cards=[1, 2, 1, 2]))
