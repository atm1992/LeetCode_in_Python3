# -*- coding: UTF-8 -*-
"""
title: 不同的子序列 II
Given a string s, return the number of distinct non-empty subsequences of s. Since the answer may be very large, return it modulo 10^9 + 7.
A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not.


Example 1:
Input: s = "abc"
Output: 7
Explanation: The 7 distinct subsequences are "a", "b", "c", "ab", "ac", "bc", and "abc".

Example 2:
Input: s = "aba"
Output: 6
Explanation: The 6 distinct subsequences are "a", "b", "ab", "aa", "ba", and "aba".

Example 3:
Input: s = "aaa"
Output: 3
Explanation: The 3 distinct subsequences are "a", "aa" and "aaa".


Constraints:
1 <= s.length <= 2000
s consists of lowercase English letters.
"""


class Solution:
    def distinctSubseqII(self, s: str) -> int:
        """
        动态规划
        设dp[i]表示字符串s中的前i个字符所组成的不同子序列(必须包含第i个字符)的个数
        状态转移方程：
        枚举子序列中的倒数第2个字符，此时需注意去重，若 0 < j1 < j2 < i 且 s[j1] == s[j2]，则以s[j2]结尾的子序列会包含所有以s[j1]结尾的子序列，
        因此，对于相同的若干个字符，只需累加其中最后一个的dp值即可。所以最终结果也是累加每个字符最后一次出现时的dp值
        """
        mod = 10 ** 9 + 7
        ch2last_idx = {}
        dp = []
        for i, ch in enumerate(s):
            # 只有当前一个字符的子序列
            tmp = 1
            for last_idx in ch2last_idx.values():
                tmp = (tmp + dp[last_idx]) % mod
            dp.append(tmp)
            ch2last_idx[ch] = i
        res = 0
        for last_idx in ch2last_idx.values():
            res = (res + dp[last_idx]) % mod
        return res

    def distinctSubseqII_2(self, s: str) -> int:
        """优化的动态规划。其实可以直接在上面的哈希表中记录每个字符最后一次出现时的dp值，而不用记录每个字符最后一次出现时的idx"""
        mod = 10 ** 9 + 7
        ch2dp = {}
        for ch in s:
            # 只有当前一个字符的子序列
            tmp = 1
            for dp in ch2dp.values():
                tmp = (tmp + dp) % mod
            ch2dp[ch] = tmp
        res = 0
        for dp in ch2dp.values():
            res = (res + dp) % mod
        return res

    def distinctSubseqII_3(self, s: str) -> int:
        """继续优化的动态规划。其实上面的第二个for循环可以省略，直接在第一个for循环中向res累加每个字符的dp值增量"""
        mod = 10 ** 9 + 7
        ch2dp = {}
        res = 0
        for ch in s:
            # res就是之前的累加和，最后再加上子序列中只有当前一个字符的情况
            # cur = res + 1
            # res = res + cur - pre = 2 * res - pre + 1
            res, ch2dp[ch] = (2 * res - ch2dp.get(ch, 0) + 1) % mod, (res + 1) % mod
        return res


if __name__ == '__main__':
    print(Solution().distinctSubseqII_3(s="abc"))
