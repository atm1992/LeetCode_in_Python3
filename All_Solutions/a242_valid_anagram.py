# -*- coding: UTF-8 -*-
"""
title: 有效的字母异位词
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.


Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false


Constraints:
1 <= s.length, t.length <= 5 * 10^4
s and t consist of lowercase English letters.

Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?
"""
from collections import Counter, defaultdict


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        return Counter(s) == Counter(t)

    def isAnagram_2(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        ch2cnt = defaultdict(int)
        for s_ch, t_ch in zip(s, t):
            ch2cnt[s_ch] += 1
            ch2cnt[t_ch] -= 1
            if ch2cnt[s_ch] == 0:
                ch2cnt.pop(s_ch)
            if t_ch in ch2cnt and ch2cnt[t_ch] == 0:
                ch2cnt.pop(t_ch)
        return not ch2cnt


if __name__ == '__main__':
    print(Solution().isAnagram(s="rat", t="car"))
