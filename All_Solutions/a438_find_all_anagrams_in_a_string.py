# -*- coding: UTF-8 -*-
"""
title: 找到字符串中所有字母异位词
Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.


Example 1:
Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".

Example 2:
Input: s = "abab", p = "ab"
Output: [0,1,2]
Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".


Constraints:
1 <= s.length, p.length <= 3 * 10^4
s and p consist of lowercase English letters.
"""
from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        """滑动窗口"""
        len_s, len_p = len(s), len(p)
        res = []
        # 此时没法初始化滑动窗口，所以需要单独处理
        if len_s < len_p:
            return res
        s_cnt = [0] * 26
        p_cnt = [0] * 26
        for i in range(len_p):
            s_cnt[ord(s[i]) - ord('a')] += 1
            p_cnt[ord(p[i]) - ord('a')] += 1
        if s_cnt == p_cnt:
            res.append(0)
        for i in range(len_p, len_s):
            s_cnt[ord(s[i - len_p]) - ord('a')] -= 1
            s_cnt[ord(s[i]) - ord('a')] += 1
            if s_cnt == p_cnt:
                res.append(i - len_p + 1)
        return res

    def findAnagrams_2(self, s: str, p: str) -> List[int]:
        """优化的滑动窗口"""
        len_s, len_p = len(s), len(p)
        res = []
        # 此时没法初始化滑动窗口，所以需要单独处理
        if len_s < len_p:
            return res
        cnt = [0] * 26
        for i in range(len_p):
            cnt[ord(s[i]) - ord('a')] += 1
            cnt[ord(p[i]) - ord('a')] -= 1
        diff = 26 - cnt.count(0)
        if diff == 0:
            res.append(0)
        for i in range(len_p, len_s):
            s_out = ord(s[i - len_p]) - ord('a')
            s_in = ord(s[i]) - ord('a')

            # 该字符的数量将从不匹配变为匹配
            if cnt[s_out] == 1:
                diff -= 1
            # 该字符的数量将从匹配变为不匹配
            elif cnt[s_out] == 0:
                diff += 1
            cnt[s_out] -= 1

            # 该字符的数量将从不匹配变为匹配
            if cnt[s_in] == -1:
                diff -= 1
            # 该字符的数量将从匹配变为不匹配
            elif cnt[s_in] == 0:
                diff += 1
            cnt[s_in] += 1

            if diff == 0:
                res.append(i - len_p + 1)
        return res

    def findAnagrams_3(self, s: str, p: str) -> List[int]:
        """可变长度的滑动窗口"""
        len_s, len_p = len(s), len(p)
        res = []
        if len_s < len_p:
            return res
        cnt = [0] * 26
        for ch in p:
            cnt[ord(ch) - ord('a')] += 1
        low, high = 0, 0
        while high < len_s:
            if cnt[ord(s[high]) - ord('a')] > 0:
                # 指针high不断消耗cnt数组中计数为正数的字符
                cnt[ord(s[high]) - ord('a')] -= 1
                high += 1
                # 注意：上一行代码已经将high加1，所以high - low才有可能等于len_p
                if high - low == len_p:
                    res.append(low)
            else:
                # 当指针high指向的字符在cnt数组中被消耗完了，则通过指针low来补给。当指针high指向的字符在p中不存在的时候，
                # low 会一直向前移，移动到high + 1，从而使得这个p中不存在的字符在cnt数组中的计数为1
                cnt[ord(s[low]) - ord('a')] += 1
                low += 1
        return res


if __name__ == '__main__':
    print(Solution().findAnagrams_3(s="abab", p="ab"))
