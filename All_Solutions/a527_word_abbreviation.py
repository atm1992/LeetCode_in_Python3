# -*- coding: UTF-8 -*-
"""
title: 单词缩写
Given an array of distinct strings words, return the minimal possible abbreviations for every word.
The following are the rules for a string abbreviation:
    The initial abbreviation for each word is: the first character, then the number of characters in between, followed by the last character.
    If more than one word shares the same abbreviation, then perform the following operation:
        Increase the prefix (characters in the first part) of each of their abbreviations by 1.
            For example, say you start with the words ["abcdef","abndef"] both initially abbreviated as "a4f". Then, a sequence of operations would be ["a4f","a4f"] -> ["ab3f","ab3f"] -> ["abc2f","abn2f"].
        This operation is repeated until every abbreviation is unique.
    At the end, if an abbreviation did not make a word shorter, then keep it as the original word.


Example 1:
Input: words = ["like","god","internal","me","internet","interval","intension","face","intrusion"]
Output: ["l2e","god","internal","me","i6t","interval","inte4n","f2e","intr4n"]

Example 2:
Input: words = ["aa","aaa"]
Output: ["aa","aaa"]


Constraints:
1 <= words.length <= 400
2 <= words[i].length <= 400
words[i] consists of lowercase English letters.
All the strings of words are unique.
"""
from collections import defaultdict
from typing import List


class Trie:
    def __init__(self):
        self.children = defaultdict(Trie)
        self.word_cnt = 0

    def insert(self, word: str) -> None:
        node = self
        for ch in word:
            node = node.children[ch]
            node.word_cnt += 1


class Solution:
    def wordsAbbreviation(self, words: List[str]) -> List[str]:
        """
        分组 + 字典树
        """
        groups = defaultdict(list)
        # 先对words按 (word长度, word首字母, word尾字母) 进行分组
        for idx, word in enumerate(words):
            groups[(len(word), word[0], word[-1])].append((word, idx))
        res = [''] * len(words)
        for group in groups.values():
            # 针对每个分组，建一棵字典树
            root = Trie()
            # 先将当前分组中的所有word都插入到字典树中
            for word, _ in group:
                root.insert(word)
            # 遍历当前分组中的所有word
            for word, idx in group:
                node = root
                for i, ch in enumerate(word):
                    # 若当前字母是当前word在同组的所有word中独有的，则说明可以得到当前word唯一的缩写了。
                    # 因为原始的words中不存在两个完全相同的word，并且同组的所有word的长度是相同的，
                    # 所以在同组中不存在一个word是另一个word的前缀问题，因此下面这个条件一定是成立的
                    if node.children[ch].word_cnt == 1:
                        abbr_len = len(word) - i - 2
                        abbr = word[:i + 1] + str(abbr_len) + word[-1] if abbr_len > 1 else word
                        res[idx] = abbr
                        break
                    node = node.children[ch]
        return res


if __name__ == '__main__':
    print(Solution().wordsAbbreviation(words=["like", "god", "internal", "me", "internet", "interval", "intension", "face", "intrusion"]))
