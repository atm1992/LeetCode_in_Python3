# -*- coding: UTF-8 -*-
"""
title: 同构字符串
Given two strings s and t, determine if they are isomorphic.
Two strings s and t are isomorphic if the characters in s can be replaced to get t.
All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.


Example 1:
Input: s = "egg", t = "add"
Output: true

Example 2:
Input: s = "foo", t = "bar"
Output: false

Example 3:
Input: s = "paper", t = "title"
Output: true


Constraints:
1 <= s.length <= 5 * 10^4
t.length == s.length
s and t consist of any valid ascii character.
"""


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        """
        哈希表。
        不同字符不能映射到同一个字符上，相同字符只能映射到同一个字符上。例如：s中的字符'b'刚开始的时候，映射到了t中的字符'y'，那么，s中的字符'b'就不能再映射到其它字符了，反之同理。
        """
        s2t, t2s = {}, {}
        for i in range(len(s)):
            s_ch = s[i]
            t_ch = t[i]
            # 这两个条件，一个都不能少。例如：s = "badc", t = "baba"
            if (s_ch in s2t and s2t[s_ch] != t_ch) or (t_ch in t2s and t2s[t_ch] != s_ch):
                return False
            s2t[s_ch] = t_ch
            t2s[t_ch] = s_ch
        return True


if __name__ == '__main__':
    print(Solution().isIsomorphic(s="bbbaaaba", t="aaabbbba"))
