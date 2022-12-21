# -*- coding: UTF-8 -*-
"""
title: 匹配子序列的单词数
Given a string s and an array of strings words, return the number of words[i] that is a subsequence of s.
A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.
    For example, "ace" is a subsequence of "abcde".


Example 1:
Input: s = "abcde", words = ["a","bb","acd","ace"]
Output: 3
Explanation: There are three strings in words that are a subsequence of s: "a", "acd", "ace".

Example 2:
Input: s = "dsahjpjauf", words = ["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"]
Output: 2
 

Constraints:
1 <= s.length <= 5 * 10^4
1 <= words.length <= 5000
1 <= words[i].length <= 50
s and words[i] consist of only lowercase English letters.
"""
from collections import defaultdict
from typing import List


class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        """二分查找"""
        ch2idxs = defaultdict(list)
        for idx, ch in enumerate(s):
            ch2idxs[ch].append(idx)
        res, n = 0, len(s)
        for word in words:
            if len(word) > n:
                continue
            idx = -1
            for ch in word:
                if ch not in ch2idxs or ch2idxs[ch][-1] <= idx:
                    break
                left, right = 0, len(ch2idxs[ch]) - 1
                while left < right:
                    mid = (left + right) // 2
                    if ch2idxs[ch][mid] <= idx:
                        left = mid + 1
                    else:
                        right = mid
                idx = ch2idxs[ch][left]
            else:
                res += 1
        return res

    def numMatchingSubseq_2(self, s: str, words: List[str]) -> int:
        """多指针。将words中的全部word同时和字符串s进行匹配"""
        ch2word_idxs = defaultdict(list)
        for idx, word in enumerate(words):
            ch2word_idxs[word[0]].append((idx, 0))
        res = 0
        for ch in s:
            for i, w_i in ch2word_idxs.pop(ch, []):
                w_i += 1
                if w_i == len(words[i]):
                    res += 1
                else:
                    ch2word_idxs[words[i][w_i]].append((i, w_i))
        return res


if __name__ == '__main__':
    print(Solution().numMatchingSubseq_2(s="dsahjpjauf", words=["ahjpjau", "ja", "ahbwzgqnuk", "tnmlanowax"]))
