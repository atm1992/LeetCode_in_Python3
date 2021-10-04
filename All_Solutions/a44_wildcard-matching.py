# -*- coding: UTF-8 -*-
"""
title: 通配符匹配
Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*' where:
'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).
The matching should cover the entire input string (not partial).


Example 1:
Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".

Example 2:
Input: s = "aa", p = "*"
Output: true
Explanation: '*' matches any sequence.

Example 3:
Input: s = "cb", p = "?a"
Output: false
Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.

Example 4:
Input: s = "adceb", p = "*a*b"
Output: true
Explanation: The first '*' matches the empty sequence, while the second '*' matches the substring "dce".

Example 5:
Input: s = "acdcb", p = "a*c?b"
Output: false


Constraints:
0 <= s.length, p.length <= 2000
s contains only lowercase English letters.
p contains only lowercase English letters, '?' or '*'.
"""


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        """动态规划。用dp[i][j]表示 s 的前 i 个字符与 p 中的前 j 个字符是否能够匹配"""

        def matches(i: int, j: int) -> bool:
            # s中的第i个字符(下标为i-1) 与 p中的第j个字符(下标为j-1) 是否匹配
            if i < 1 or j < 1:
                return False
            return s[i - 1] == p[j - 1] or p[j - 1] == '?'

        m, n = len(s), len(p)
        # m+1行，n+1列
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        # s和p都为空字符串时，结果为True
        dp[0][0] = True
        for i in range(m + 1):
            # 除了s也为空字符串的情况。其余p为空字符串的时候，结果都为False
            for j in range(1, n + 1):
                if p[j - 1] == '*':
                    # '*' 匹配0个字符 或 1个字符
                    dp[i][j] = dp[i][j - 1] or dp[i - 1][j]
                elif matches(i, j):
                    dp[i][j] = dp[i - 1][j - 1]
        return dp[m][n]

    def isMatch_2(self, s: str, p: str) -> bool:
        """贪心算法。上个方法的瓶颈在于对星号 * 的处理方式：使用动态规划枚举所有的情况。
        可将模式p看作是由多个子模式ui(不含星号)与之间的(单个或连续多个, 连续多个等价于单个)星号拼接而来，即 *u1*u2*……*un*。
        先从字符串s的第一个字符(下标为0)开始匹配u1中的第一个字符，若匹配，则继续匹配下一个字符；
        若不匹配，则从字符串s的第二个字符开始重新匹配u1，表示使用u1前面的星号去覆盖s的第一个字符。以此类推 ……
        若模式p不是以星号结尾，则不断地匹配 s 和 p 的结尾字符，直到 p 为空(p中没有星号)或 p 的结尾字符是星号为止；
        若模式p不是以星号开头，则不断地匹配 s 和 p 的开头字符，直到 p 为空(p中没有星号)或 p 的开头字符是星号为止。
        若在字符串s中依次找到了u1、u2、……、un，则表示字符串s与模式p匹配。
        """

        def is_char_match(s_ch: str, p_ch: str) -> bool:
            return s_ch == p_ch or p_ch == '?'

        s_right, p_right = len(s) - 1, len(p) - 1
        # 找到p中最后一个星号的下标，即 让模式p以星号结尾
        while s_right >= 0 and p_right >= 0 and p[p_right] != '*':
            if is_char_match(s[s_right], p[p_right]):
                s_right -= 1
                p_right -= 1
            else:
                return False
        # 模式p中没有星号，此时若字符串s也没有字符了，则正好匹配成功，否则匹配失败。
        # 如果字符串s没有字符了，而模式p还有字符，不一定匹配失败，因为如果模式p剩余的都是星号，则还是匹配成功的
        if p_right == -1:
            return s_right == -1
        # s_record记录此次子模式ui的匹配是从字符串s中的哪个下标开始，p_record表示子模式ui在模式p中的下标。
        # 若模式p是以星号开头，则p_record = p_idx = 1。p_record = p_idx = 0 是为了兼容处理模式p不以星号开头的情况。
        # 若p_record == 0，则表示子模式ui前面没有星号
        s_record = s_idx = 0
        p_record = p_idx = 0
        while s_idx <= s_right and p_idx <= p_right:
            if p[p_idx] == '*':
                p_idx += 1
                # 更新此次子模式ui匹配的开始下标
                s_record, p_record = s_idx, p_idx
            elif is_char_match(s[s_idx], p[p_idx]):
                s_idx += 1
                p_idx += 1
            # 模式p中的当前字符既不是星号，也没有匹配上字符串s中的当前字符。
            # p_record != 0 说明p_record前面有星号；s_record + 1 <= s_right 说明字符串s还有字符可用来匹配ui
            elif p_record != 0 and s_record + 1 <= s_right:
                # 之所以是在s_record基础上加1，而不是在s_idx基础上加1。考虑特殊情况：si为sssr, ui为ssr，s_idx为2时，字符匹配失败，
                # 此时若将s_idx更新为3，则最终匹配失败。而如果将s_record从0更新为1，则最终匹配成功，此时会用ui前面的星号去覆盖si[0]
                s_record += 1
                s_idx, p_idx = s_record, p_record
            else:
                return False
        # all([]) == True。若模式p只剩星号或者恰好为空了，则匹配成功
        return all(p[i] == '*' for i in range(p_idx, p_right + 1))


if __name__ == '__main__':
    print(Solution().isMatch_2(s="a", p="aa"))
