# -*- coding: UTF-8 -*-
"""
title: 最大单词长度乘积
Given a string array words, return the maximum value of length(word[i]) * length(word[j]) where the two words do not share common letters. If no such two words exist, return 0.


Example 1:
Input: words = ["abcw","baz","foo","bar","xtfn","abcdef"]
Output: 16
Explanation: The two words can be "abcw", "xtfn".

Example 2:
Input: words = ["a","ab","abc","d","cd","bcd","abcd"]
Output: 4
Explanation: The two words can be "ab", "cd".

Example 3:
Input: words = ["a","aa","aaa","aaaa"]
Output: 0
Explanation: No such pair of words.


Constraints:
2 <= words.length <= 1000
1 <= words[i].length <= 1000
words[i] consists only of lowercase English letters.
"""
from typing import List
from collections import defaultdict


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
