# -*- coding: UTF-8 -*-
"""
title: 重构字符串
Given a string s, rearrange the characters of s so that any two adjacent characters are not the same.
Return any possible rearrangement of s or return "" if not possible.


Example 1:
Input: s = "aab"
Output: "aba"

Example 2:
Input: s = "aaab"
Output: ""


Constraints:
1 <= s.length <= 500
s consists of lowercase English letters.
"""
import heapq
from collections import Counter


class Solution:
    def reorganizeString(self, s: str) -> str:
        """基于最大堆的贪心"""
        n = len(s)
        ch2cnt = Counter(s)
        if max(ch2cnt.values()) > (n + 1) // 2:
            return ""
        cnt_ch = []
        for ch, cnt in ch2cnt.items():
            # heapq 默认是最小堆，先按-cnt数字升序，再按ch字典序升序。-cnt相等时，必须要能对ch排序。
            # 假设 ch2cnt 中的值为 [(-3, 'a'), (-3, 'b')]，对ch排序可以确保每次都是 a/b、a/b 、a/b 的取，而不会第一次是a/b，下一次又变成b/a
            # 若不能对ch排序，则需确保append到res的第一个字符不能与上一次的最后一个字符相同。
            cnt_ch.append((-cnt, ch))
        heapq.heapify(cnt_ch)
        res = []
        while len(cnt_ch) > 1:
            cnt_1, ch_1 = heapq.heappop(cnt_ch)
            cnt_2, ch_2 = heapq.heappop(cnt_ch)
            res.extend([ch_1, ch_2])
            # 因为 cnt_1、cnt_2 是负数
            cnt_1 += 1
            cnt_2 += 1
            if cnt_1 < 0:
                heapq.heappush(cnt_ch, (cnt_1, ch_1))
            if cnt_2 < 0:
                heapq.heappush(cnt_ch, (cnt_2, ch_2))
        if cnt_ch:
            res.append(cnt_ch[0][1])
        return ''.join(res)


if __name__ == '__main__':
    print(Solution().reorganizeString("aab"))
