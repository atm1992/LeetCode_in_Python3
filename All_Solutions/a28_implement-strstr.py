# -*- coding: UTF-8 -*-
"""
title: 实现 strStr()
Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Clarification:
What should we return when needle is an empty string? This is a great question to ask during an interview.
For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().


Example 1:
Input: haystack = "hello", needle = "ll"
Output: 2

Example 2:
Input: haystack = "aaaaa", needle = "bba"
Output: -1

Example 3:
Input: haystack = "", needle = ""
Output: 0


Constraints:
0 <= haystack.length, needle.length <= 5 * 10^4
haystack and needle consist of only lower-case English characters.
"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)

    def strStr_2(self, haystack: str, needle: str) -> int:
        """暴力匹配"""
        n, m = len(haystack), len(needle)
        for i in range(n - m + 1):
            if haystack[i:i + m] == needle:
                return i
        return -1

    def strStr_3(self, haystack: str, needle: str) -> int:
        """KMP算法"""
        n, m = len(haystack), len(needle)
        if m == 0:
            return 0
        nxt = [0] * m
        cur = 0
        # 基于模式串needle计算前缀函数(即 next数组)
        for i in range(1, m):
            while cur > 0 and needle[cur] != needle[i]:
                cur = nxt[cur - 1]
            if needle[cur] == needle[i]:
                cur += 1
                nxt[i] = cur
        cur = 0
        # 利用next数组在主串haystack中匹配模式串needle
        for i in range(n):
            while cur > 0 and needle[cur] != haystack[i]:
                cur = nxt[cur - 1]
            if needle[cur] == haystack[i]:
                cur += 1
                if cur == m:
                    return i - m + 1
        return -1


if __name__ == '__main__':
    print(Solution().strStr_3(haystack="hello", needle="ll"))
