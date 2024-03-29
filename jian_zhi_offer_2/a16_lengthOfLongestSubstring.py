# -*- coding: UTF-8 -*-
"""
title: 不含重复字符的最长子字符串
给定一个字符串 s ，请你找出其中不含有重复字符的 最长连续子字符串 的长度。


示例 1:
输入: s = "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子字符串是 "abc"，所以其长度为 3。

示例 2:
输入: s = "bbbbb"
输出: 1
解释: 因为无重复字符的最长子字符串是 "b"，所以其长度为 1。

示例 3:
输入: s = "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。

示例 4:
输入: s = ""
输出: 0


提示：
0 <= s.length <= 5 * 10^4
s 由英文字母、数字、符号和空格组成
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """双指针"""
        res = 0
        ch2idx = {}
        left = 0
        for idx, ch in enumerate(s):
            # 如果该字符之前的下标小于left，就可认为该字符在之前已被逻辑删除了。说明该字符在[left, idx-1]范围内没有出现过
            if ch in ch2idx and ch2idx[ch] >= left:
                res = max(res, idx - left)
                left = ch2idx[ch] + 1
            ch2idx[ch] = idx
        return max(res, len(s) - left)


if __name__ == '__main__':
    print(Solution().lengthOfLongestSubstring(' '))
