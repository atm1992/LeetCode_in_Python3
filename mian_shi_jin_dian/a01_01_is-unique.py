# -*- coding: UTF-8 -*-
"""
title: 判定字符是否唯一
Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures?


Example 1:
Input: s = "leetcode"
Output: false

Example 2:
Input: s = "abc"
Output: true


Note:
0 <= len(s) <= 100
"""


class Solution:
    def isUnique(self, astr: str) -> bool:
        return len(set(astr)) == len(astr)

    def isUnique_2(self, astr: str) -> bool:
        """位运算"""
        mark = 0
        for ch in astr:
            idx = ord(ch) - ord('a')
            if mark & (1 << idx):
                return False
            mark |= 1 << idx
        return True
