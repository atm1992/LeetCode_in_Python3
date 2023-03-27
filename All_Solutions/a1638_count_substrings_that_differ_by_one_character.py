# -*- coding: utf-8 -*-
# @date: 2023/3/27
# @author: liuquan
"""
title: 统计只差一个字符的子串数目
Given two strings s and t, find the number of ways you can choose a non-empty substring of s and replace a single character by a different character such that the resulting substring is a substring of t. In other words, find the number of substrings in s that differ from some substring in t by exactly one character.
For example, the underlined substrings in "computer" and "computation" only differ by the 'e'/'a', so this is a valid way.
Return the number of substrings that satisfy the condition above.
A substring is a contiguous sequence of characters within a string.


Example 1:
Input: s = "aba", t = "baba"
Output: 6
Explanation: The following are the pairs of substrings from s and t that differ by exactly 1 character:
("aba", "baba")
("aba", "baba")
("aba", "baba")
("aba", "baba")
("aba", "baba")
("aba", "baba")
The underlined portions are the substrings that are chosen from s and t.

Example 2:
Input: s = "ab", t = "bb"
Output: 3
Explanation: The following are the pairs of substrings from s and t that differ by 1 character:
("ab", "bb")
("ab", "bb")
("ab", "bb")
The underlined portions are the substrings that are chosen from s and t.


Constraints:
1 <= s.length, t.length <= 100
s and t consist of lowercase English letters only.
"""


class Solution:
    def countSubstrings(self, s: str, t: str) -> int:
        """枚举。因为数据规模不大"""
        res = 0
        m, n = len(s), len(t)
        for i in range(m):
            for j in range(n):
                diff = 0
                for k in range(min(m - i, n - j)):
                    if s[i + k] != t[j + k]:
                        diff += 1
                    if diff == 1:
                        res += 1
                    elif diff > 1:
                        break
        return res

    def countSubstrings_2(self, s: str, t: str) -> int:
        """
        动态规划
        若s[i] != t[j]，且 s[i-a:i] == t[j-a:j] and s[i+1:i+b+1] == t[j+1:j+b+1]，则可组成只差一个字符的子串有 (a + 1) * (b + 1) 个
        这里的a表示s[i]与t[j]左侧相同的最大长度left[i][j]，b表示s[i]与t[j]右侧相同的最大长度right[i][j]
        状态转移方程：
        left[i][j] = left[i-1][j-1] + 1 if s[i-1] == t[j-1] else 0
        right[i][j] = right[i+1][j+1] + 1 if s[i+1] == t[j+1] else 0
        """
        m, n = len(s), len(t)
        left, right = [[0] * n for _ in range(m)], [[0] * n for _ in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                if s[i - 1] == t[j - 1]:
                    left[i][j] = left[i - 1][j - 1] + 1
        for i in range(m - 2, -1, -1):
            for j in range(n - 2, -1, -1):
                if s[i + 1] == t[j + 1]:
                    right[i][j] = right[i + 1][j + 1] + 1
        res = 0
        for i, s_ch in enumerate(s):
            for j, t_ch in enumerate(t):
                if s_ch != t_ch:
                    res += (left[i][j] + 1) * (right[i][j] + 1)
        return res


if __name__ == '__main__':
    print(Solution().countSubstrings_2(s="ab", t="bb"))
