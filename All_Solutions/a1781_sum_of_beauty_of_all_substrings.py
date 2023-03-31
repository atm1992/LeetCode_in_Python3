# -*- coding: utf-8 -*-
# @date: 2023/3/30
# @author: liuquan
"""
title: 所有子字符串美丽值之和
The beauty of a string is the difference in frequencies between the most frequent and least frequent characters.
    For example, the beauty of "abaacc" is 3 - 1 = 2.
Given a string s, return the sum of beauty of all of its substrings.


Example 1:
Input: s = "aabcb"
Output: 5
Explanation: The substrings with non-zero beauty are ["aab","aabc","aabcb","abcb","bcb"], each with beauty equal to 1.

Example 2:
Input: s = "aabcbaa"
Output: 17


Constraints:
1 <= s.length <= 500
s consists of only lowercase English letters.
"""
from collections import defaultdict


class Solution:
    def beautySum(self, s: str) -> int:
        """
        枚举 + 计数
        """
        res, n = 0, len(s)
        # 要想满足美丽值大于0，子字符串的长度至少为3。长度为1、2的子字符串，其美丽值一定为0
        for i in range(n - 2):
            ch2cnt = defaultdict(int)
            for j in range(i, n):
                ch2cnt[s[j]] += 1
                if j >= i + 2:
                    res += max(ch2cnt.values()) - min(ch2cnt.values())
        return res
