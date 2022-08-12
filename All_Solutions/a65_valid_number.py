# -*- coding: UTF-8 -*-
"""
title: 有效数字
A valid number can be split up into these components (in order):
A decimal number or an integer.
(Optional) An 'e' or 'E', followed by an integer.

A decimal number can be split up into these components (in order):
(Optional) A sign character (either '+' or '-').
One of the following formats:
    One or more digits, followed by a dot '.'.
    One or more digits, followed by a dot '.', followed by one or more digits.
    A dot '.', followed by one or more digits.

An integer can be split up into these components (in order):
(Optional) A sign character (either '+' or '-').
One or more digits.

For example, all the following are valid numbers: ["2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789"], while the following are not valid numbers: ["abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53"].
Given a string s, return true if s is a valid number.


Example 1:
Input: s = "0"
Output: true

Example 2:
Input: s = "e"
Output: false

Example 3:
Input: s = "."
Output: false

Example 4:
Input: s = ".1"
Output: true


Constraints:
1 <= s.length <= 20
s consists of only English letters (both uppercase and lowercase), digits (0-9), plus '+', minus '-', or dot '.'.
"""


class Solution:
    def isNumber(self, s: str) -> bool:
        """模拟，分类讨论。本题主要考察确定有限状态自动机(DFA)"""
        n = len(s)
        dot_flag = e_flag = num_flag = False
        for i in range(n):
            ch = s[i]
            if ch in ['e', 'E']:
                if i == 0 or i == n - 1 or e_flag or not num_flag:
                    return False
                e_flag = True
            elif ch in ['+', '-']:
                if (i > 0 and s[i - 1] not in ['e', 'E']) or i == n - 1:
                    return False
            elif ch == '.':
                if dot_flag or e_flag or n == 1:
                    return False
                dot_flag = True
            elif '0' <= ch <= '9':
                num_flag = True
            else:
                return False
        return num_flag

    def isNumber_2(self, s: str) -> bool:
        """本题主要考察确定有限状态自动机(DFA)。但执行效率比不上前一个方法"""
        from enum import Enum
        # 状态集合。此题其实并没用到 STATE_END
        State = Enum('State', [
            'STATE_INITIAL',
            'STATE_INT_SIGN',
            'STATE_INTEGER',
            'STATE_POINT',
            'STATE_POINT_WITHOUT_INT',
            'STATE_FRACTION',
            'STATE_EXP',
            'STATE_EXP_SIGN',
            'STATE_EXP_NUMBER',
            'STATE_END'
        ])
        CharType = Enum('CharType', [
            'CHAR_NUMBER',
            'CHAR_EXP',
            'CHAR_POINT',
            'CHAR_SIGN',
            'CHAR_ILLEGAL'
        ])
        # 转移规则
        transfer = {
            State.STATE_INITIAL: {
                CharType.CHAR_NUMBER: State.STATE_INTEGER,
                CharType.CHAR_POINT: State.STATE_POINT_WITHOUT_INT,
                CharType.CHAR_SIGN: State.STATE_INT_SIGN
            },
            State.STATE_INT_SIGN: {
                CharType.CHAR_NUMBER: State.STATE_INTEGER,
                CharType.CHAR_POINT: State.STATE_POINT_WITHOUT_INT
            },
            State.STATE_INTEGER: {
                CharType.CHAR_NUMBER: State.STATE_INTEGER,
                CharType.CHAR_POINT: State.STATE_POINT,
                CharType.CHAR_EXP: State.STATE_EXP
            },
            State.STATE_POINT: {
                CharType.CHAR_NUMBER: State.STATE_FRACTION,
                CharType.CHAR_EXP: State.STATE_EXP
            },
            State.STATE_POINT_WITHOUT_INT: {
                CharType.CHAR_NUMBER: State.STATE_FRACTION
            },
            State.STATE_FRACTION: {
                CharType.CHAR_NUMBER: State.STATE_FRACTION,
                CharType.CHAR_EXP: State.STATE_EXP
            },
            State.STATE_EXP: {
                CharType.CHAR_NUMBER: State.STATE_EXP_NUMBER,
                CharType.CHAR_SIGN: State.STATE_EXP_SIGN
            },
            State.STATE_EXP_SIGN: {
                CharType.CHAR_NUMBER: State.STATE_EXP_NUMBER
            },
            State.STATE_EXP_NUMBER: {
                CharType.CHAR_NUMBER: State.STATE_EXP_NUMBER
            }
        }

        def to_char_type(ch: str) -> CharType:
            if ch.isdigit():
                return CharType.CHAR_NUMBER
            elif ch.lower() == 'e':
                return CharType.CHAR_EXP
            elif ch == '.':
                return CharType.CHAR_POINT
            elif ch in ['+', '-']:
                return CharType.CHAR_SIGN
            else:
                return CharType.CHAR_ILLEGAL

        # 初始状态
        cur_state = State.STATE_INITIAL
        for ch in s:
            char_type = to_char_type(ch)
            if char_type not in transfer[cur_state]:
                return False
            cur_state = transfer[cur_state][char_type]
        # 允许的最终状态
        return cur_state in [State.STATE_INTEGER, State.STATE_POINT, State.STATE_FRACTION, State.STATE_EXP_NUMBER,
                             State.STATE_END]


if __name__ == '__main__':
    print(Solution().isNumber_2("+."))
