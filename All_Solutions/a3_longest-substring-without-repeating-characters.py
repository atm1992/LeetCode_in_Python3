# -*- coding: UTF-8 -*-
"""
title: 无重复字符的最长子串。
Given a string s, find the length of the longest substring without repeating characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

Example 4:
Input: s = ""
Output: 0
 

Constraints:
0 <= s.length <= 5 * 10^4
s consists of English letters, digits, symbols and spaces.
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        tmp = []
        for char in s:
            if char not in tmp:
                tmp.append(char)
            else:
                if max_len < len(tmp):
                    max_len = len(tmp)
                tmp = tmp[tmp.index(char) + 1:]
                tmp.append(char)
        # 以防出现给定s完全不存在重复字符的情况，此时max_len始终为0
        return max(max_len, len(tmp))
