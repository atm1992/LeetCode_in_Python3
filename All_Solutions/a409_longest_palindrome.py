# -*- coding: UTF-8 -*-
"""
title: 最长回文串
Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.
Letters are case sensitive, for example, "Aa" is not considered a palindrome here.


Example 1:
Input: s = "abccccdd"
Output: 7
Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.

Example 2:
Input: s = "a"
Output: 1
Explanation: The longest palindrome that can be built is "a", whose length is 1.


Constraints:
1 <= s.length <= 2000
s consists of lowercase and/or uppercase English letters only.
"""
from collections import Counter


class Solution:
    def longestPalindrome(self, s: str) -> int:
        """贪心"""
        res = 0
        for cnt in Counter(s).values():
            res += cnt // 2 * 2
        # 若在计算res的过程中，有抛弃过字符，则可从这些被抛弃的字符中选一个作为回文中心
        return res + 1 if res < len(s) else res
