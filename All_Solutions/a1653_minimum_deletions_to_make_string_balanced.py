# -*- coding: UTF-8 -*-
"""
title: 使字符串平衡的最少删除次数
You are given a string s consisting only of characters 'a' and 'b'​​​​.
You can delete any number of characters in s to make s balanced. s is balanced if there is no pair of indices (i,j) such that i < j and s[i] = 'b' and s[j]= 'a'.
Return the minimum number of deletions needed to make s balanced.


Example 1:
Input: s = "aababbab"
Output: 2
Explanation: You can either:
Delete the characters at 0-indexed positions 2 and 6 ("aababbab" -> "aaabbb"), or
Delete the characters at 0-indexed positions 3 and 6 ("aababbab" -> "aabbbb").

Example 2:
Input: s = "bbaaaaabb"
Output: 2
Explanation: The only solution is to delete the first two characters.


Constraints:
1 <= s.length <= 10^5
s[i] is 'a' or 'b'​​.
"""


class Solution:
    def minimumDeletions(self, s: str) -> int:
        """
        枚举
        最终平衡有3种情况：
        1、最后只剩下'a'，即 删除了所有的'b'
        2、最后只剩下'b'，即 删除了所有的'a'
        3、找到一条合适的分割线，使得前面都是'a'，后面都是'b'，即 删除了分割线前面所有的'b'以及分割线后面所有的'a'
        这3种情况取最小值即为最终答案
        """
        left_b, right_a = 0, s.count('a')
        # 将res的初始值设置为第二种情况，删除了所有的'a'
        res = right_a
        for ch in s:
            if ch == 'a':
                right_a -= 1
            else:
                left_b += 1
            # 当遍历到字符串s的最末尾时，其实就是第一种情况，此时的left_b就是s中的'b'总数
            res = min(res, left_b + right_a)
        return res

    def minimumDeletions_2(self, s: str) -> int:
        """
        动态规划
        设dp[i]表示使前i个字符平衡的最少删除次数
        状态转移方程：
        1、若s[i]为'b'，则 dp[i] = dp[i-1]
        2、若s[i]为'a'，则可选择保留或删除，若需保留，则需把前面的所有'b'都删除；若需删除，则删除次数加1。即 dp[i] = min(dp[i-1] + 1, b_cnt)
        """
        dp, b_cnt = 0, 0
        for ch in s:
            if ch == 'a':
                dp = min(dp + 1, b_cnt)
            else:
                b_cnt += 1
        return dp


if __name__ == '__main__':
    print(Solution().minimumDeletions_2(s="aababbab"))
