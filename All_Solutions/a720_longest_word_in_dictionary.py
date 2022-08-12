# -*- coding: UTF-8 -*-
"""
title: 词典中最长的单词
Given an array of strings words representing an English Dictionary, return the longest word in words that can be built one character at a time by other words in words.
If there is more than one possible answer, return the longest word with the smallest lexicographical order. If there is no answer, return the empty string.


Example 1:
Input: words = ["w","wo","wor","worl","world"]
Output: "world"
Explanation: The word "world" can be built one character at a time by "w", "wo", "wor", and "worl".

Example 2:
Input: words = ["a","banana","app","appl","ap","apply","apple"]
Output: "apple"
Explanation: Both "apply" and "apple" can be built from other words in the dictionary. However, "apple" is lexicographically smaller than "apply".


Constraints:
1 <= words.length <= 1000
1 <= words[i].length <= 30
words[i] consists of lowercase English letters.
"""
from typing import List


class Trie:
    def __init__(self):
        self.children = [None] * 26
        self.is_end = False

    def insert(self, word: str) -> None:
        node = self
        for ch in word:
            idx = ord(ch) - ord('a')
            if not node.children[idx]:
                node.children[idx] = Trie()
            node = node.children[idx]
        node.is_end = True

    def search(self, word: str) -> bool:
        """查找是否包含当前word的所有前缀单词。单词apple的所有前缀单词为：'appl'、'app'、'ap'、'a' """
        node = self
        for ch in word:
            idx = ord(ch) - ord('a')
            if not node.children[idx] or node.children[idx].is_end == False:
                return False
            node = node.children[idx]
        return True


class Solution:
    def longestWord(self, words: List[str]) -> str:
        """哈希表"""
        # 先按长度升序，再按字典序降序
        words.sort(key=lambda x: (-len(x), x), reverse=True)
        res = ''
        # 空字符串也是符合要求的单词
        visited = {res}
        for word in words:
            if word[:-1] in visited:
                res = word
                visited.add(word)
        return res

    def longestWord_2(self, words: List[str]) -> str:
        """字典树(前缀树)"""
        trie = Trie()
        for word in words:
            trie.insert(word)
        res = ''
        for word in words:
            if trie.search(word) and (len(word) > len(res) or (len(word) == len(res) and word < res)):
                res = word
        return res
