# -*- coding: UTF-8 -*-
"""
title: 正则表达式匹配。
Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:
'.' Matches any single character.​​​​
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).


Example 1:
Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".

Example 2:
Input: s = "aa", p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".

Example 3:
Input: s = "ab", p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".

Example 4:
Input: s = "aab", p = "c*a*b"
Output: true
Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore, it matches "aab".

Example 5:
Input: s = "mississippi", p = "mis*is*p*."
Output: false


Constraints:
1 <= s.length <= 20
1 <= p.length <= 30
s contains only lowercase English letters.
p contains only lowercase English letters, '.', and '*'.
It is guaranteed for each appearance of the character '*', there will be a previous valid character to match.
"""


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        """
        动态规划。用f[i][j]表示 s 的前 i 个字符与 p 中的前 j 个字符是否能够匹配。状态转移方程分为p中的第j个字符是否为 * 两种情况进行讨论。
        若为*，则需要将j-1、j作为一个组合进行匹配
        """
        m, n = len(s), len(p)

        def matches(i: int, j: int) -> bool:
            # s中的第i个字符(下标为i-1) 与 p中的第j个字符(下标为j-1) 是否匹配
            if i < 1 or j < 1:
                return False
            return s[i - 1] == p[j - 1] or p[j - 1] == '.'

        # m为行，n为列
        f = [[False] * (n + 1) for _ in range(m + 1)]
        # s、p均为空字符串时，匹配结果设为True
        f[0][0] = True
        for i in range(m + 1):
            # j==0时，即 p 为空字符串，除了s也为空字符串时，匹配结果为True，其余情况下，匹配结果都是False。
            # 而s为空字符串时，p 不为空字符串，匹配结果也有可能为True，例如：...*.
            for j in range(1, n + 1):
                # s中的i-1对应f中的i，p中的j-1对应f中的j
                if p[j - 1] == '*':
                    # 对于逻辑变量(True/False)，True or False 等价于 True | False；True and False 等价于 True & False。
                    # 对于数值变量，则有区别，一个是位运算，而一个是逻辑运算(短路运算)。
                    # 此时的*匹配了0次，直接去掉p中的组合(j-2、j-1)
                    f[i][j] = f[i][j - 2]
                    # 此时的*匹配了1次
                    if matches(i, j - 1):
                        # 相当于直接去掉s中的i-1，之后再让p中的组合(j-2、j-1)去s中匹配0或1次
                        f[i][j] = f[i][j] or f[i - 1][j]
                elif matches(i, j):
                    # p中的一个字符匹配s中的一个字符
                    f[i][j] = f[i - 1][j - 1]
        return f[m][n]


if __name__ == '__main__':
    s = 'mississippi'
    p = 'mis*is*p*.'
    print(Solution().isMatch(s, p))
