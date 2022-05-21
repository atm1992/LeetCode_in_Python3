# -*- coding: UTF-8 -*-
"""
title: 字符串中的所有变位词
给定两个字符串 s 和 p，找到 s 中所有 p 的 变位词 的子串，返回这些子串的起始索引。不考虑答案输出的顺序。
变位词 指字母相同，但排列不同的字符串。


示例 1：
输入: s = "cbaebabacd", p = "abc"
输出: [0,6]
解释:
起始索引等于 0 的子串是 "cba", 它是 "abc" 的变位词。
起始索引等于 6 的子串是 "bac", 它是 "abc" 的变位词。

示例 2：
输入: s = "abab", p = "ab"
输出: [0,1,2]
解释:
起始索引等于 0 的子串是 "ab", 它是 "ab" 的变位词。
起始索引等于 1 的子串是 "ba", 它是 "ab" 的变位词。
起始索引等于 2 的子串是 "ab", 它是 "ab" 的变位词。


提示:
1 <= s.length, p.length <= 3 * 10^4
s 和 p 仅包含小写字母
"""
from collections import defaultdict
from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        """滑动窗口"""
        m, n = len(s), len(p)
        res = []
        if m < n:
            return res
        ch2cnt = defaultdict(int)
        diff_cnt = 0
        # 先加再减。顺序不能错，先加s的字符，再减p的字符
        for i in range(n):
            ch_s, ch_p = s[i], p[i]
            if ch2cnt[ch_s] == 0:
                diff_cnt += 1
            elif ch2cnt[ch_s] == -1:
                diff_cnt -= 1
            ch2cnt[ch_s] += 1
            if ch2cnt[ch_p] == 0:
                diff_cnt += 1
            elif ch2cnt[ch_p] == 1:
                diff_cnt -= 1
            ch2cnt[ch_p] -= 1
        if diff_cnt == 0:
            res.append(0)
        # 先加再减。顺序不能错，先加s的最新字符，再减s的历史字符
        for i in range(n, m):
            ch_add, ch_del = s[i], s[i - n]
            if ch2cnt[ch_add] == 0:
                diff_cnt += 1
            elif ch2cnt[ch_add] == -1:
                diff_cnt -= 1
            ch2cnt[ch_add] += 1
            if ch2cnt[ch_del] == 0:
                diff_cnt += 1
            elif ch2cnt[ch_del] == 1:
                diff_cnt -= 1
            ch2cnt[ch_del] -= 1
            if diff_cnt == 0:
                res.append(i - n + 1)
        return res


if __name__ == '__main__':
    print(Solution().findAnagrams(s="abab", p="ab"))
