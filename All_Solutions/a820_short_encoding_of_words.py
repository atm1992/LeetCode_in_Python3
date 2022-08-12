# -*- coding: UTF-8 -*-
"""
title: 单词的压缩编码
A valid encoding of an array of words is any reference string s and array of indices indices such that:
    words.length == indices.length
    The reference string s ends with the '#' character.
    For each index indices[i], the substring of s starting from indices[i] and up to (but not including) the next '#' character is equal to words[i].
Given an array of words, return the length of the shortest reference string s possible of any valid encoding of words.


Example 1:
Input: words = ["time", "me", "bell"]
Output: 10
Explanation: A valid encoding would be s = "time#bell#" and indices = [0, 2, 5].
words[0] = "time", the substring of s starting from indices[0] = 0 to the next '#' is underlined in "time#bell#"
words[1] = "me", the substring of s starting from indices[1] = 2 to the next '#' is underlined in "time#bell#"
words[2] = "bell", the substring of s starting from indices[2] = 5 to the next '#' is underlined in "time#bell#"

Example 2:
Input: words = ["t"]
Output: 2
Explanation: A valid encoding would be s = "t#" and indices = [0].


Constraints:
1 <= words.length <= 2000
1 <= words[i].length <= 7
words[i] consists of only lowercase letters.
"""
from typing import List


class Trie:
    def __init__(self):
        self.children = [None] * 26

    def insert(self, word: str) -> None:
        node = self
        for ch in word:
            idx = ord(ch) - ord('a')
            if not node.children[idx]:
                node.children[idx] = Trie()
            node = node.children[idx]

    def is_prefix(self, prefix: str) -> bool:
        node = self
        for ch in prefix:
            idx = ord(ch) - ord('a')
            if not node.children[idx]:
                return False
            node = node.children[idx]
        return True


class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        """字典树"""
        words.sort(key=lambda word: len(word), reverse=True)
        trie = Trie()
        res = 0
        for word in words:
            if trie.is_prefix(word[::-1]):
                continue
            trie.insert(word[::-1])
            res += len(word) + 1
        return res

    def minimumLengthEncoding_2(self, words: List[str]) -> int:
        n = len(words)
        # 根据逆序后的单词，按字典序升序。
        # 例如：['abc', 'bc', 'wa', 'a', 'ha'] ————> ['a', 'ha', 'wa', 'bc', 'abc']
        words.sort(key=lambda word: word[::-1])
        res = 0
        for idx, word in enumerate(words):
            # 上面的 'a', 'bc' 会被抛弃
            if idx + 1 < n and words[idx + 1].endswith(word):
                continue
            res += len(word) + 1
        return res


if __name__ == '__main__':
    print(Solution().minimumLengthEncoding(["time", "me", "bell"]))
