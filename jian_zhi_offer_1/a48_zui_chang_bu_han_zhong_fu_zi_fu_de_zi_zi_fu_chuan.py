# -*- coding: UTF-8 -*-
"""
title: 最长不含重复字符的子字符串
请从字符串中找出一个最长的不包含重复字符的子字符串，计算该最长子字符串的长度。


示例 1:
输入: "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。

示例 2:
输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。

示例 3:
输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。


提示：
s.length <= 40000
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        ch2idx = {}
        left = 0
        for idx, ch in enumerate(s):
            # 如果该字符之前的下标小于left，就可认为该字符在之前已被逻辑删除了。说明该字符在[left, idx-1]范围内没有出现过
            if ch in ch2idx and ch2idx[ch] >= left:
                res = max(res, idx - left)
                left = ch2idx[ch] + 1
            ch2idx[ch] = idx
        res = max(res, len(s) - left)
        return res


if __name__ == '__main__':
    print(Solution().lengthOfLongestSubstring('cdd'))
