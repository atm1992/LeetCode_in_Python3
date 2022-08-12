# -*- coding: UTF-8 -*-
"""
title: 翻转单词顺序
输入一个英文句子，翻转句子中单词的顺序，但单词内字符的顺序不变。为简单起见，标点符号和普通字母一样处理。例如输入字符串"I am a student. "，则输出"student. a am I"。


示例 1：
输入: "the sky is blue"
输出: "blue is sky the"

示例 2：
输入: "  hello world!  "
输出: "world! hello"
解释: 输入字符串可以在前面或者后面包含多余的空格，但是反转后的字符不能包括。

示例 3：
输入: "a good   example"
输出: "example good a"
解释: 如果两个单词间有多余的空格，将反转后单词间的空格减少到只含一个。


说明：
无空格字符构成一个单词。
输入字符串可以在前面或者后面包含多余的空格，但是反转后的字符不能包括。
如果两个单词间有多余的空格，将反转后单词间的空格减少到只含一个。
"""


class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(s.split()[::-1])

    def reverseWords_2(self, s: str) -> str:
        res = []
        right = len(s) - 1
        while right >= 0:
            while right >= 0 and s[right] == ' ':
                right -= 1
            if right < 0:
                break
            left = right
            while left - 1 >= 0 and s[left - 1] != ' ':
                left -= 1
            res.append(s[left:right+1])
            right = left - 1
        return ' '.join(res)


if __name__ == '__main__':
    print(Solution().reverseWords_2("  hello  world!   "))
