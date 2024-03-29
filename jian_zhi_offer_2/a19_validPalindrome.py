# -*- coding: UTF-8 -*-
"""
title: 最多删除一个字符得到回文
给定一个非空字符串 s，请判断如果 最多 从字符串中删除一个字符能否得到一个回文字符串。


示例 1:
输入: s = "aba"
输出: true

示例 2:
输入: s = "abca"
输出: true
解释: 可以删除 "c" 字符 或者 "b" 字符

示例 3:
输入: s = "abc"
输出: false


提示:
1 <= s.length <= 10^5
s 由小写英文字母组成
"""


class Solution:
    def validPalindrome(self, s: str) -> bool:
        """贪心 + 双指针"""

        def check(left: int, right: int) -> bool:
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        left, right = 0, len(s) - 1
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return check(left + 1, right) or check(left, right - 1)
        return True
