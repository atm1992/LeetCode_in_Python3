# -*- coding: UTF-8 -*-
"""
title: 表示数值的字符串
请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。
数值（按顺序）可以分成以下几个部分：
    若干空格
    一个 小数 或者 整数
    （可选）一个 'e' 或 'E' ，后面跟着一个 整数
    若干空格
小数（按顺序）可以分成以下几个部分：
    （可选）一个符号字符（'+' 或 '-'）
    下述格式之一：
        至少一位数字，后面跟着一个点 '.'
        至少一位数字，后面跟着一个点 '.' ，后面再跟着至少一位数字
        一个点 '.' ，后面跟着至少一位数字
整数（按顺序）可以分成以下几个部分：
    （可选）一个符号字符（'+' 或 '-'）
    至少一位数字
部分数值列举如下：
    ["+100", "5e2", "-123", "3.1416", "-1E-16", "0123"]
部分非数值列举如下：
    ["12e", "1a3.14", "1.2.3", "+-5", "12e+5.4"]


示例 1：
输入：s = "0"
输出：true

示例 2：
输入：s = "e"
输出：false

示例 3：
输入：s = "."
输出：false

示例 4：
输入：s = "    .1  "
输出：true


提示：
1 <= s.length <= 20
s 仅含英文字母（大写和小写），数字（0-9），加号 '+' ，减号 '-' ，空格 ' ' 或者点 '.' 。

参考LeetCode题65，此题比题65多一个空格 ' '
"""


class Solution:
    def isNumber(self, s: str) -> bool:
        """
        本题主要考察确定有限状态自动机(DFA)
        所有可能的状态：
            1、起始的空格
            2、符号位
            3、整数部分
            4、左侧有整数的小数点
            5、左侧无整数的小数点
            6、小数部分
            7、字符'e' 或 'E'
            8、指数部分的符号位
            9、指数部分的整数部分
            10、末尾的空格
        初始状态：
            1、起始的空格
        接受状态：
            3、整数部分
            4、左侧有整数的小数点
            6、小数部分
            9、指数部分的整数部分
            10、末尾的空格
        当字符串全部读取完毕后，如果自动机处于某个接受状态，则判定该字符串被接受；否则，判定该字符串被拒绝。
        """
        from enum import Enum
        # 状态集合
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
            'CHAR_SPACE',
            'CHAR_ILLEGAL'
        ])
        # 转移规则
        transfer = {
            State.STATE_INITIAL: {
                CharType.CHAR_SPACE: State.STATE_INITIAL,
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
                CharType.CHAR_EXP: State.STATE_EXP,
                CharType.CHAR_SPACE: State.STATE_END
            },
            State.STATE_POINT: {
                CharType.CHAR_NUMBER: State.STATE_FRACTION,
                CharType.CHAR_EXP: State.STATE_EXP,
                CharType.CHAR_SPACE: State.STATE_END
            },
            State.STATE_POINT_WITHOUT_INT: {
                CharType.CHAR_NUMBER: State.STATE_FRACTION
            },
            State.STATE_FRACTION: {
                CharType.CHAR_NUMBER: State.STATE_FRACTION,
                CharType.CHAR_EXP: State.STATE_EXP,
                CharType.CHAR_SPACE: State.STATE_END
            },
            State.STATE_EXP: {
                CharType.CHAR_NUMBER: State.STATE_EXP_NUMBER,
                CharType.CHAR_SIGN: State.STATE_EXP_SIGN
            },
            State.STATE_EXP_SIGN: {
                CharType.CHAR_NUMBER: State.STATE_EXP_NUMBER
            },
            State.STATE_EXP_NUMBER: {
                CharType.CHAR_NUMBER: State.STATE_EXP_NUMBER,
                CharType.CHAR_SPACE: State.STATE_END
            },
            State.STATE_END: {
                CharType.CHAR_SPACE: State.STATE_END
            }
        }

        def to_char_type(ch: str) -> CharType:
            if ch.isdigit():
                return CharType.CHAR_NUMBER
            elif ch in ['e', 'E']:
                return CharType.CHAR_EXP
            elif ch == '.':
                return CharType.CHAR_POINT
            elif ch in ['+', '-']:
                return CharType.CHAR_SIGN
            elif ch == ' ':
                return CharType.CHAR_SPACE
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

    def isNumber_2(self, s: str) -> bool:
        """模拟，分类讨论。本题主要考察确定有限状态自动机(DFA)，单论执行速度，此方法快得多"""
        s = s.strip()
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
            elif ch.isdigit():
                num_flag = True
            else:
                return False
        return num_flag


if __name__ == '__main__':
    print(Solution().isNumber_2("   .1  "))
