# -*- coding: UTF-8 -*-
"""
title: 有效的变位词
给定两个字符串 s 和 t ，编写一个函数来判断它们是不是一组变位词（字母异位词）。
注意：若 s 和 t 中每个字符出现的次数都相同且字符顺序不完全相同，则称 s 和 t 互为变位词（字母异位词）。


示例 1:
输入: s = "anagram", t = "nagaram"
输出: true

示例 2:
输入: s = "rat", t = "car"
输出: false

示例 3:
输入: s = "a", t = "a"
输出: false


提示:
1 <= s.length, t.length <= 5 * 10^4
s and t 仅包含小写字母

进阶: 如果输入字符串包含 unicode 字符怎么办？你能否调整你的解法来应对这种情况？
"""
from collections import defaultdict, Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t) or s == t:
            return False
        return Counter(s) == Counter(t)

    def isAnagram_2(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        is_same = True
        ch2cnt = defaultdict(int)
        for s_ch, t_ch in zip(s, t):
            ch2cnt[s_ch] += 1
            ch2cnt[t_ch] -= 1
            if is_same and s_ch != t_ch:
                is_same = False
            if ch2cnt[s_ch] == 0:
                ch2cnt.pop(s_ch)
            if t_ch in ch2cnt and ch2cnt[t_ch] == 0:
                ch2cnt.pop(t_ch)
        return not is_same and not ch2cnt


if __name__ == '__main__':
    print(Solution().isAnagram(s="rat", t="car"))
