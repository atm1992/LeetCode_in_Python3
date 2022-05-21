# -*- coding: UTF-8 -*-
"""
title: 有效的回文
给定一个字符串 s ，验证 s 是否是 回文串 ，只考虑字母和数字字符，可以忽略字母的大小写。
本题中，将空字符串定义为有效的 回文串 。


示例 1:
输入: s = "A man, a plan, a canal: Panama"
输出: true
解释："amanaplanacanalpanama" 是回文串

示例 2:
输入: s = "race a car"
输出: false
解释："raceacar" 不是回文串


提示：
1 <= s.length <= 2 * 10^5
字符串 s 由 ASCII 字符组成
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        """双指针"""
        left, right = 0, len(s) - 1
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True


if __name__ == '__main__':
    print(Solution().isPalindrome("race a car"))
