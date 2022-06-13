# -*- coding: UTF-8 -*-
"""
title: 最短的单词编码
单词数组 words 的 有效编码 由任意助记字符串 s 和下标数组 indices 组成，且满足：
    words.length == indices.length
    助记字符串 s 以 '#' 字符结尾
    对于每个下标 indices[i] ，s 的一个从 indices[i] 开始、到下一个 '#' 字符结束（但不包括 '#'）的 子字符串 恰好与 words[i] 相等
给定一个单词数组 words ，返回成功对 words 进行编码的最小助记字符串 s 的长度 。


示例 1：
输入：words = ["time", "me", "bell"]
输出：10
解释：一组有效编码为 s = "time#bell#" 和 indices = [0, 2, 5] 。
words[0] = "time" ，s 开始于 indices[0] = 0 到下一个 '#' 结束的子字符串，如加粗部分所示 "time#bell#"
words[1] = "me" ，s 开始于 indices[1] = 2 到下一个 '#' 结束的子字符串，如加粗部分所示 "time#bell#"
words[2] = "bell" ，s 开始于 indices[2] = 5 到下一个 '#' 结束的子字符串，如加粗部分所示 "time#bell#"

示例 2：
输入：words = ["t"]
输出：2
解释：一组有效编码为 s = "t#" 和 indices = [0] 。


提示：
1 <= words.length <= 2000
1 <= words[i].length <= 7
words[i] 仅由小写字母组成
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
