# -*- coding: UTF-8 -*-
"""
title: 字符串的左右移
You are given a string s containing lowercase English letters, and a matrix shift, where shift[i] = [directioni, amounti]:
    directioni can be 0 (for left shift) or 1 (for right shift).
    amounti is the amount by which string s is to be shifted.
    A left shift by 1 means remove the first character of s and append it to the end.
    Similarly, a right shift by 1 means remove the last character of s and add it to the beginning.
Return the final string after all operations.


Example 1:
Input: s = "abc", shift = [[0,1],[1,2]]
Output: "cab"
Explanation: 
[0,1] means shift to left by 1. "abc" -> "bca"
[1,2] means shift to right by 2. "bca" -> "cab"

Example 2:
Input: s = "abcdefg", shift = [[1,1],[1,1],[0,2],[1,3]]
Output: "efgabcd"
Explanation: 
[1,1] means shift to right by 1. "abcdefg" -> "gabcdef"
[1,1] means shift to right by 1. "gabcdef" -> "fgabcde"
[0,2] means shift to left by 2. "fgabcde" -> "abcdefg"
[1,3] means shift to right by 3. "abcdefg" -> "efgabcd"


Constraints:
1 <= s.length <= 100
s only contains lower case English letters.
1 <= shift.length <= 100
shift[i].length == 2
directioni is either 0 or 1.
0 <= amounti <= 100
"""
from typing import List


class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        """模拟"""
        n = len(s)
        direction, amount = 0, 0
        for d, a in shift:
            a %= n
            if d == direction:
                amount = (amount + a) % n
            elif a > amount:
                direction = 1 - direction
                amount = a - amount
            else:
                amount = amount - a
        return s[-amount:] + s[:-amount] if direction else s[amount:] + s[:amount]

    def stringShift_2(self, s: str, shift: List[List[int]]) -> str:
        """模拟"""
        amount = 0
        for d, a in shift:
            # 右移为正，左移为负
            amount += (2 * d - 1) * a
        # Python取模与常规不同，若amount为负数，则取模结果为len(s) - (abs(amount) % len(s))；若amount为正数，则取模结果为amount % len(s)
        amount %= len(s)
        # 这里统一转换为右移
        return s[-amount:] + s[:-amount]


if __name__ == '__main__':
    print(Solution().stringShift(s="abcdefg", shift=[[1, 1], [1, 1], [0, 2], [1, 3]]))
