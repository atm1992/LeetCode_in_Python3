# -*- coding: UTF-8 -*-
"""
title: 各位相加
Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.


Example 1:
Input: num = 38
Output: 2
Explanation: The process is
38 --> 3 + 8 --> 11
11 --> 1 + 1 --> 2
Since 2 has only one digit, return it.

Example 2:
Input: num = 0
Output: 0


Constraints:
0 <= num <= 2^31 - 1

Follow up: Could you do it without any loop/recursion in O(1) runtime?
"""


class Solution:
    def addDigits(self, num: int) -> int:
        while num > 9:
            tmp = 0
            while num:
                tmp += num % 10
                num //= 10
            num = tmp
        return num

    def addDigits_2(self, num: int) -> int:
        """
        数学。只有num为0时，结果才为0。其余情况下，结果在[1, 9]之间。
        假设num的十进制表示由n位数字(a0/a1/……/an-1)组成，则num = a0 * 10^0 + a1 * 10^1 + …… + an-1 * 10^n-1 = Eai * 10^i （E 表示累加符号, 0 <= i <= n-1）
        num = Eai * 10^i = Eai * (10^i - 1 + 1) = Eai * (10^i - 1) + Eai
        其中，Eai 就是我们所需的系数累加，设为res，则 num = res * (10^i - 1) + res
        10^i - 1 分别为 0、9、99、999、……，可以看出这些数都是9的倍数，因此num对9取余，可以消去res * (10^i - 1)，最后剩下res
        但是直接对9取余，结果范围为[0, 8]，而我们知道除了0以外，结果范围为[1, 9]，因此可以先将num-1，然后对9取余，最后再加上1
        """
        # Python中，-1 % 9 == 8，而不是 -1，所以需要对num为0的情况额外处理
        return (num - 1) % 9 + 1 if num > 0 else 0


if __name__ == '__main__':
    print(Solution().addDigits(38))
