# -*- coding: UTF-8 -*-
"""
title: 单词长度的最大乘积
给定一个字符串数组 words，请计算当两个字符串 words[i] 和 words[j] 不包含相同字符时，它们长度的乘积的最大值。假设字符串中只包含英语的小写字母。如果没有不包含相同字符的一对字符串，返回 0。


示例 1:
输入: words = ["abcw","baz","foo","bar","fxyz","abcdef"]
输出: 16
解释: 这两个单词为 "abcw", "fxyz"。它们不包含相同字符，且长度的乘积最大。

示例 2:
输入: words = ["a","ab","abc","d","cd","bcd","abcd"]
输出: 4
解释: 这两个单词为 "ab", "cd"。

示例 3:
输入: words = ["a","aa","aaa","aaaa"]
输出: 0
解释: 不存在这样的两个单词。


提示：
2 <= words.length <= 1000
1 <= words[i].length <= 1000
words[i] 仅包含小写字母
"""
from collections import defaultdict
from typing import List


class Solution:
    def maxProduct(self, words: List[str]) -> int:
        """位运算"""
        masks = []
        for word in words:
            bit = 0
            for ch in word:
                bit |= 1 << (ord(ch) - ord('a'))
            masks.append(bit)
        res = 0
        for bit_i, word_i in zip(masks, words):
            for bit_j, word_j in zip(masks, words):
                if bit_i & bit_j == 0:
                    res = max(res, len(word_i) * len(word_j))
        return res

    def maxProduct_2(self, words: List[str]) -> int:
        """位运算优化"""
        masks = defaultdict(int)
        for word in words:
            bit = 0
            for ch in word:
                bit |= 1 << (ord(ch) - ord('a'))
            masks[bit] = max(masks[bit], len(word))
        res = 0
        for bit_i, len_i in masks.items():
            for bit_j, len_j in masks.items():
                if bit_i & bit_j == 0:
                    res = max(res, len_i * len_j)
        return res


if __name__ == '__main__':
    print(Solution().maxProduct_2(["abcw", "baz", "foo", "bar", "fxyz", "abcdef"]))
