# -*- coding: UTF-8 -*-
"""
title: 最长字符串链
You are given an array of words where each word consists of lowercase English letters.
wordA is a predecessor of wordB if and only if we can insert exactly one letter anywhere in wordA without changing the order of the other characters to make it equal to wordB.
    For example, "abc" is a predecessor of "abac", while "cba" is not a predecessor of "bcad".
A word chain is a sequence of words [word1, word2, ..., wordk] with k >= 1, where word1 is a predecessor of word2, word2 is a predecessor of word3, and so on. A single word is trivially a word chain with k == 1.
Return the length of the longest possible word chain with words chosen from the given list of words.


Example 1:
Input: words = ["a","b","ba","bca","bda","bdca"]
Output: 4
Explanation: One of the longest word chains is ["a","ba","bda","bdca"].

Example 2:
Input: words = ["xbc","pcxbcf","xb","cxbc","pcxbc"]
Output: 5
Explanation: All the words can be put in a word chain ["xb", "xbc", "cxbc", "pcxbc", "pcxbcf"].

Example 3:
Input: words = ["abcd","dbqca"]
Output: 1
Explanation: The trivial word chain ["abcd"] is one of the longest word chains.
["abcd","dbqca"] is not a valid word chain because the ordering of the letters is changed.


Constraints:
1 <= words.length <= 1000
1 <= words[i].length <= 16
words[i] only consists of lowercase English letters.
"""
from collections import defaultdict
from typing import List, DefaultDict


class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        """
        排序 + 哈希表 + 动态规划
        假设 dp[word] 表示以word结尾的单词链的最大长度
        状态转移方程：
        dp[word] 可以从比word长度小1的pre_word转移而来
        dp[word] = max(dp[word], dp[pre_word] + 1)
        """
        res = 0
        word2maxlen = defaultdict(int)
        for word in sorted(words, key=lambda word: len(word)):
            for i in range(len(word)):
                pre_word = word[:i] + word[i + 1:]
                word2maxlen[word] = max(word2maxlen[word], word2maxlen[pre_word] + 1)
            res = max(res, word2maxlen[word])
        return res

    def longestStrChain_2(self, words: List[str]) -> int:
        """哈希表 + 动态规划"""
        size2words = defaultdict(DefaultDict[str, int])
        for word in words:
            size2words[len(word)][word] = 1
        res = 1
        for size in sorted(size2words.keys()):
            if not size2words[size - 1]:
                continue
            for word in size2words[size]:
                for i in range(size):
                    pre = word[:i] + word[i + 1:]
                    if pre in size2words[size - 1] and size2words[size - 1][pre] + 1 > size2words[size][word]:
                        size2words[size][word] = size2words[size - 1][pre] + 1
                        res = max(res, size2words[size][word])
        return res


if __name__ == '__main__':
    print(Solution().longestStrChain_2(["xbc", "pcxbcf", "xb", "cxbc", "pcxbc"]))
