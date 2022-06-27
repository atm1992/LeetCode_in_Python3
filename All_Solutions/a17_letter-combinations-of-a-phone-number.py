# -*- coding: UTF-8 -*-
"""
title: 电话号码的字母组合
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.
A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.


Example 1:
Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Example 2:
Input: digits = ""
Output: []

Example 3:
Input: digits = "2"
Output: ["a","b","c"]


Constraints:
0 <= digits.length <= 4
digits[i] is a digit in the range ['2', '9'].
"""
from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        """递归"""
        mappings = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }

        def recursion(digits: str) -> List[str]:
            n = len(digits)
            if n == 0:
                return []
            if n == 1:
                return mappings[digits]
            tmp = recursion(digits[1:])
            res = []
            for a in mappings[digits[0]]:
                for b in tmp:
                    res.append(a + b)
            return res

        return recursion(digits)


if __name__ == '__main__':
    s = '337'
    print(Solution().letterCombinations(s))
