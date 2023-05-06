# -*- coding: utf-8 -*-
# @date: 2023/5/6
# @author: liuquan
"""
title: 自定义字符串排序
You are given two strings order and s. All the characters of order are unique and were sorted in some custom order previously.
Permute the characters of s so that they match the order that order was sorted. More specifically, if a character x occurs before a character y in order, then x should occur before y in the permuted string.
Return any permutation of s that satisfies this property.


Example 1:
Input: order = "cba", s = "abcd"
Output: "cbad"
Explanation:
"a", "b", "c" appear in order, so the order of "a", "b", "c" should be "c", "b", and "a".
Since "d" does not appear in order, it can be at any position in the returned string. "dcba", "cdba", "cbda" are also valid outputs.

Example 2:
Input: order = "cbafg", s = "abcd"
Output: "cbad"


Constraints:
1 <= order.length <= 26
1 <= s.length <= 200
order and s consist of lowercase English letters.
All the characters of order are unique.
"""
from collections import Counter


class Solution:
    def customSortString(self, order: str, s: str) -> str:
        """自定义排序"""
        ch2ord = {ch: i for i, ch in enumerate(order)}
        return ''.join(sorted(s, key=lambda ch: ch2ord.get(ch, 26)))

    def customSortString_2(self, order: str, s: str) -> str:
        """计数排序"""
        ch2cnt = Counter(s)
        res = ''
        for ch in order:
            if ch2cnt[ch] > 0:
                res += ch * ch2cnt[ch]
                ch2cnt[ch] = 0
        for ch, cnt in ch2cnt.items():
            if cnt > 0:
                res += ch * cnt
        return res


if __name__ == '__main__':
    print(Solution().customSortString_2(order="cbafg", s="abcd"))
