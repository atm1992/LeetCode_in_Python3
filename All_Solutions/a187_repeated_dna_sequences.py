# -*- coding: UTF-8 -*-
"""
title: 重复的DNA序列
The DNA sequence is composed of a series of nucleotides abbreviated as 'A', 'C', 'G', and 'T'.
    For example, "ACGAATTCCG" is a DNA sequence.
When studying DNA, it is useful to identify repeated sequences within the DNA.
Given a string s that represents a DNA sequence, return all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule. You may return the answer in any order.


Example 1:
Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
Output: ["AAAAACCCCC","CCCCCAAAAA"]

Example 2:
Input: s = "AAAAAAAAAAAAA"
Output: ["AAAAAAAAAA"]


Constraints:
1 <= s.length <= 10^5
s[i] is either 'A', 'C', 'G', or 'T'.
"""
from collections import defaultdict
from typing import List


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        """哈希表"""
        res = []
        L = 10
        counter = defaultdict(int)
        for i in range(len(s) - L + 1):
            sub_str = s[i:i + L]
            counter[sub_str] += 1
            # 只在 ==2 的时候，才添加到res。而不是 >1 的时候就添加，那样会造成重复添加
            if counter[sub_str] == 2:
                res.append(sub_str)
        return res

    def findRepeatedDnaSequences_2(self, s: str) -> List[str]:
        """
        哈希表 + 滑动窗口 + 位运算。
        因为字符串只包含'A', 'C', 'G', 'T'这4个字符，可以使用2个比特来表示各个字符：00 - 'A', 01 - 'C', 10 - 'G', 11 - 'T'
        使用一个长度为10的滑动窗口来计算当前10个字符对应的int值，假设当前长度为10的子字符串对应的int值为x，
        则下一个长度为10的子字符串对应的int值为 ((x << 2) | ch2int(ch)) & ((1 << 20) - 1)
        解释：((x << 2) | ch2int(ch)) 表示滑动窗口左侧移出一个字符(用2个比特来表示)，右侧进入一个字符。
        & ((1 << 20) - 1) 表示只考虑int值的低20位
        """
        res = []
        L = 10
        n = len(s)
        if n <= L:
            return res
        ch2int = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
        counter = defaultdict(int)
        # 计算初始滑动窗口中的10个字符所对应的int值
        x = 0
        for ch in s[:L]:
            x = (x << 2) | ch2int[ch]
        counter[x] += 1
        for i in range(L, n):
            x = ((x << 2) | ch2int[s[i]]) & ((1 << (2 * L)) - 1)
            counter[x] += 1
            if counter[x] == 2:
                res.append(s[i - L + 1:i + 1])
        return res


if __name__ == '__main__':
    print(Solution().findRepeatedDnaSequences_2("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"))
