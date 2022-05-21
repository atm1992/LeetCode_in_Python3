# -*- coding: UTF-8 -*-
"""
title: 字符串中的变位词
给定两个字符串 s1 和 s2，写一个函数来判断 s2 是否包含 s1 的某个变位词。
换句话说，第一个字符串的排列之一是第二个字符串的 子串 。


示例 1：
输入: s1 = "ab" s2 = "eidbaooo"
输出: True
解释: s2 包含 s1 的排列之一 ("ba").

示例 2：
输入: s1= "ab" s2 = "eidboaoo"
输出: False


提示：
1 <= s1.length, s2.length <= 10^4
s1 和 s2 仅包含小写字母
"""
from collections import defaultdict


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """滑动窗口"""
        n1, n2 = len(s1), len(s2)
        if n1 > n2:
            return False
        diff_cnt = 0
        ch2cnt = defaultdict(int)
        # 先加再减。顺序不能错，先加s2的字符，再减s1的字符
        for i in range(n1):
            ch1, ch2 = s1[i], s2[i]
            if ch2cnt[ch2] == 0:
                diff_cnt += 1
            elif ch2cnt[ch2] == -1:
                diff_cnt -= 1
            ch2cnt[ch2] += 1
            if ch2cnt[ch1] == 0:
                diff_cnt += 1
            elif ch2cnt[ch1] == 1:
                diff_cnt -= 1
            ch2cnt[ch1] -= 1
        if diff_cnt == 0:
            return True
        # 先加再减。顺序不能错，先加s2的最新字符，再减s2的历史字符
        for i in range(n1, n2):
            ch2_add, ch2_del = s2[i], s2[i - n1]
            if ch2cnt[ch2_add] == 0:
                diff_cnt += 1
            elif ch2cnt[ch2_add] == -1:
                diff_cnt -= 1
            ch2cnt[ch2_add] += 1
            if ch2cnt[ch2_del] == 0:
                diff_cnt += 1
            elif ch2cnt[ch2_del] == 1:
                diff_cnt -= 1
            ch2cnt[ch2_del] -= 1
            if diff_cnt == 0:
                return True
        return False

    def checkInclusion_2(self, s1: str, s2: str) -> bool:
        """双指针"""
        n1, n2 = len(s1), len(s2)
        if n1 > n2:
            return False
        ch2cnt = defaultdict(int)
        for ch in s1:
            ch2cnt[ch] -= 1
        left = 0
        for right, ch in enumerate(s2):
            ch2cnt[ch] += 1
            while ch2cnt[ch] > 0:
                ch2cnt[s2[left]] -= 1
                left += 1
            if right - left + 1 == n1:
                return True
        return False


if __name__ == '__main__':
    print(Solution().checkInclusion_2(s1="ab", s2="eidbaooo"))
