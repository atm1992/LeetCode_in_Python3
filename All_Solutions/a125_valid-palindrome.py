# -*- coding: UTF-8 -*-
"""
title：验证回文串。
给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。
说明：本题中，我们将空字符串定义为有效的回文串。
示例 1:
输入: "A man, a plan, a canal: Panama"
输出: true

示例 2:
输入: "race a car"
输出: false

解题思路：首先，得到只保留大小写字母、数字的字符串；然后将大写字母转换为小写字母；最后判断字符串的逆序与原字符串是否相等。
只考虑大小写字母和数字，其余字符不考虑
"""


class Solution:
    # 使用正则表达式
    def isPalindrome(self, s: str) -> bool:
        import re
        tmp = "".join(re.findall(r"[a-zA-Z0-9]+", s))
        tmp = tmp.lower()
        return tmp[::-1] == tmp

    def isPalindrome_2(self, s: str) -> bool:
        tmp = ""
        s = s.lower()
        for i in s:
            if 'a' <= i <= 'z' or '0' <= i <= '9':
                tmp += i
        return tmp[::-1] == tmp
