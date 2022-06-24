# -*- coding: UTF-8 -*-
"""
title: 形成三的最大倍数
Given an array of digits digits, return the largest multiple of three that can be formed by concatenating some of the given digits in any order. If there is no answer return an empty string.
Since the answer may not fit in an integer data type, return the answer as a string. Note that the returning answer must not contain unnecessary leading zeros.


Example 1:
Input: digits = [8,1,9]
Output: "981"

Example 2:
Input: digits = [8,6,7,1,0]
Output: "8760"

Example 3:
Input: digits = [1]
Output: ""

Example 4:
Input: digits = [0,0,0,0,0,0]
Output: "0"


Constraints:
1 <= digits.length <= 10^4
0 <= digits[i] <= 9
"""
from typing import List


class Solution:
    def largestMultipleOfThree(self, digits: List[int]) -> str:
        """
        数学。
        假设digits数组的累加和为total，则可分为3种情况：
        1、total % 3 == 0，直接降序拼接返回
        2、total % 3 == 1，删除digits中一个最小的余1的元素，若不存在，则删除两个最小的余2的元素
        3、total % 3 == 2，删除digits中一个最小的余2的元素，若不存在，则删除两个最小的余1的元素
        """
        total, digit2cnt, mod2cnt = 0, [0] * 10, [0] * 3
        for digit in digits:
            total += digit
            digit2cnt[digit] += 1
            mod2cnt[digit % 3] += 1
        remove_mod, remove_cnt = 0, 0
        if total % 3 == 1:
            remove_mod, remove_cnt = (1, 1) if mod2cnt[1] >= 1 else (2, 2)
        elif total % 3 == 2:
            remove_mod, remove_cnt = (2, 1) if mod2cnt[2] >= 1 else (1, 2)
        res = []
        for i in range(10):
            for j in range(digit2cnt[i]):
                if remove_cnt > 0 and i % 3 == remove_mod:
                    remove_cnt -= 1
                else:
                    res.append(str(i))
        res = ''.join(res[::-1])
        return '0' if res.startswith('0') else res
