# -*- coding: utf-8 -*-
# @date: 2023/4/12
# @author: liuquan
"""
title: 段式回文
You are given a string text. You should split it to k substrings (subtext1, subtext2, ..., subtextk) such that:
    subtexti is a non-empty string.
    The concatenation of all the substrings is equal to text (i.e., subtext1 + subtext2 + ... + subtextk == text).
    subtexti == subtextk - i + 1 for all valid values of i (i.e., 1 <= i <= k).
Return the largest possible value of k.


Example 1:
Input: text = "ghiabcdefhelloadamhelloabcdefghi"
Output: 7
Explanation: We can split the string on "(ghi)(abcdef)(hello)(adam)(hello)(abcdef)(ghi)".

Example 2:
Input: text = "merchant"
Output: 1
Explanation: We can split the string on "(merchant)".

Example 3:
Input: text = "antaprezatepzapreanta"
Output: 11
Explanation: We can split the string on "(a)(nt)(a)(pre)(za)(tep)(za)(pre)(a)(nt)(a)".


Constraints:
1 <= text.length <= 1000
text consists only of lowercase English characters.
"""


class Solution:
    def longestDecomposition(self, text: str) -> int:
        """
        贪心 + 双指针
        先找到text中最短的 prefix == suffix，然后继续查找中间的剩余字符串，直到pre_e > suf_s
        """
        res = 0
        pre_s, pre_e = 0, 1
        suf_s, suf_e = len(text) - 1, len(text)
        while pre_e <= suf_s:
            if text[pre_s:pre_e] == text[suf_s:suf_e]:
                res += 2
                pre_s = pre_e
                suf_e = suf_s
            pre_e += 1
            suf_s -= 1
        # 判断中间的剩余字符串是否为空，若不为空，则将中间剩余的那部分单独作为一个子字符串
        # 注意：中间剩余的那部分也可能就是text本身，此时的res还是初始值0，pre_s != suf_e 可以最终返回1
        return res + (pre_s != suf_e)
