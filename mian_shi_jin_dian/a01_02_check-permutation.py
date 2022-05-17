# -*- coding: UTF-8 -*-
"""
title: 判定是否互为字符重排
Given two strings,write a method to decide if one is a permutation of the other.


Example 1:
Input: s1 = "abc", s2 = "bca"
Output: true

Example 2:
Input: s1 = "abc", s2 = "bad"
Output: false


Note:
0 <= len(s1) <= 100
0 <= len(s2) <= 100
"""
from collections import defaultdict


class Solution:
    def CheckPermutation(self, s1: str, s2: str) -> bool:
        """排序"""
        if len(s1) != len(s2):
            return False
        return sorted(s1) == sorted(s2)

    def CheckPermutation_2(self, s1: str, s2: str) -> bool:
        """哈希表"""
        if len(s1) != len(s2):
            return False
        ch2cnt = defaultdict(int)
        diff = 0
        for ch1, ch2 in zip(s1, s2):
            if ch2cnt[ch1] == -1:
                diff -= 1
            elif ch2cnt[ch1] == 0:
                diff += 1
            ch2cnt[ch1] += 1
            if ch2cnt[ch2] == 1:
                diff -= 1
            elif ch2cnt[ch2] == 0:
                diff += 1
            ch2cnt[ch2] -= 1
        return diff == 0

    def CheckPermutation_3(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False
        cnt = [0] * 26
        for ch in s1:
            cnt[ord(ch) - ord('a')] += 1
        for ch in s2:
            cnt[ord(ch) - ord('a')] -= 1
            if cnt[ord(ch) - ord('a')] < 0:
                return False
        return True


if __name__ == '__main__':
    print(Solution().CheckPermutation_2(s1="abc", s2="bca"))
