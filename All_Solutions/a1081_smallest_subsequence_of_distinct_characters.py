# -*- coding: UTF-8 -*-
"""
title: 不同字符的最小子序列
Given a string s, return the lexicographically smallest subsequence of s that contains all the distinct characters of s exactly once.


Example 1:
Input: s = "bcabc"
Output: "abc"

Example 2:
Input: s = "cbacdcbc"
Output: "acdb"


Constraints:
1 <= s.length <= 1000
s consists of lowercase English letters.
此题与LeetCode题316相同
"""


class Solution:
    def smallestSubsequence(self, s: str) -> str:
        """
        贪心 + 单调栈
        要想使返回结果的字典序最小，则应尽量使返回结果中的字母升序，因此可使用一个单调递增栈。
        若当前字母小于栈顶字母，且栈顶字母在之后位置还存在，则可以pop栈顶字母；若栈顶字母在之后不存在了，则此时必须保留。
        """
        # 记录每个字母最后一次出现的下标
        ch2idx = {}
        for idx, ch in enumerate(s):
            ch2idx[ch] = idx
        stack = []
        chs_in_stack = set()
        for idx, ch in enumerate(s):
            if ch not in chs_in_stack:
                while stack and stack[-1] > ch and ch2idx[stack[-1]] > idx:
                    chs_in_stack.remove(stack.pop())
                chs_in_stack.add(ch)
                stack.append(ch)
        return ''.join(stack)
