# -*- coding: UTF-8 -*-
"""
title: 无重复字符的最长子串
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
        """哈希表"""
        res = 0
        left = 0
        ch2idx = {}
        for idx, ch in enumerate(s):
            # 若该字符之前的下标小于left，则认为该字符在之前已被逻辑删除了。说明该字符在[left, idx-1]范围内没有出现过
            if ch2idx.get(ch, -1) >= left:
                res = max(res, idx - left)
                left = ch2idx[ch] + 1
            ch2idx[ch] = idx
        return max(res, len(s) - left)
