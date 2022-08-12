# -*- coding: UTF-8 -*-
"""
title: 单词替换
In English, we have a concept called root, which can be followed by some other word to form another longer word - let's call this word successor. For example, when the root "an" is followed by the successor word "other", we can form a new word "another".
Given a dictionary consisting of many roots and a sentence consisting of words separated by spaces, replace all the successors in the sentence with the root forming it. If a successor can be replaced by more than one root, replace it with the root that has the shortest length.
Return the sentence after the replacement.


Example 1:
Input: dictionary = ["cat","bat","rat"], sentence = "the cattle was rattled by the battery"
Output: "the cat was rat by the bat"

Example 2:
Input: dictionary = ["a","b","c"], sentence = "aadsfasf absbs bbab cadsfafs"
Output: "a a b c"


Constraints:
1 <= dictionary.length <= 1000
1 <= dictionary[i].length <= 100
dictionary[i] consists of only lower-case letters.
1 <= sentence.length <= 10^6
sentence consists of only lower-case letters and spaces.
The number of words in sentence is in the range [1, 1000]
The length of each word in sentence is in the range [1, 1000]
Every two consecutive words in sentence will be separated by exactly one space.
sentence does not have leading or trailing spaces.
"""
from typing import List


class Trie:
    def __init__(self):
        self.children = [None] * 26
        self.word = ''

    def insert(self, prefix) -> None:
        node = self
        for ch in prefix:
            idx = ord(ch) - ord('a')
            if not node.children[idx]:
                node.children[idx] = Trie()
            if node.children[idx].word:
                return
            node = node.children[idx]
        node.word = prefix

    def get_root(self, word) -> str:
        node = self
        for ch in word:
            idx = ord(ch) - ord('a')
            if not node.children[idx]:
                return word
            if node.children[idx].word:
                return node.children[idx].word
            node = node.children[idx]
        # 特殊情况：输入word是已存储prefix的前缀，例如：输入word为 's'，已存储prefix中有 'sh'，此时应该返回's'，而不是None
        return word


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        res = []
        trie = Trie()
        for prefix in dictionary:
            trie.insert(prefix)
        for word in sentence.split():
            res.append(trie.get_root(word))
        return ' '.join(res)
