# -*- coding: UTF-8 -*-
"""
title: 添加与搜索单词 - 数据结构设计
Design a data structure that supports adding new words and finding if a string matches any previously added string.
Implement the WordDictionary class:
    WordDictionary() Initializes the object.
    void addWord(word) Adds word to the data structure, it can be matched later.
    bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.


Example:
Input
["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
Output
[null,null,null,null,false,true,true,true]
Explanation
WordDictionary wordDictionary = new WordDictionary();
wordDictionary.addWord("bad");
wordDictionary.addWord("dad");
wordDictionary.addWord("mad");
wordDictionary.search("pad"); // return False
wordDictionary.search("bad"); // return True
wordDictionary.search(".ad"); // return True
wordDictionary.search("b.."); // return True


Constraints:
1 <= word.length <= 25
word in addWord consists of lowercase English letters.
word in search consist of '.' or lowercase English letters.
There will be at most 3 dots in word for search queries.
At most 10^4 calls will be made to addWord and search.
"""
from collections import defaultdict


class TrieNode:
    def __init__(self):
        # 字典树（前缀树）。26叉树
        self.children = [None] * 26
        self.is_end = False

    def insert(self, word: str) -> None:
        node = self
        for ch in word:
            idx = ord(ch) - ord('a')
            if not node.children[idx]:
                node.children[idx] = TrieNode()
            node = node.children[idx]
        node.is_end = True


class WordDictionary:

    def __init__(self):
        self.trie_root = TrieNode()

    def addWord(self, word: str) -> None:
        self.trie_root.insert(word)

    def search(self, word: str) -> bool:
        n = len(word)

        def dfs(idx: int, node: TrieNode) -> bool:
            if idx == n:
                return node.is_end
            ch = word[idx]
            if ch != '.':
                child = node.children[ord(ch) - ord('a')]
                if child is not None and dfs(idx + 1, child):
                    return True
            else:
                for child in node.children:
                    if child is not None and dfs(idx + 1, child):
                        return True
            return False

        return dfs(0, self.trie_root)


class WordDictionary2:
    """执行速度比上面的字典树快很多"""

    def __init__(self):
        self.words = set()
        self.len2words = defaultdict(list)

    def addWord(self, word: str) -> None:
        if word not in self.words:
            self.words.add(word)
            self.len2words[len(word)].append(word)

    def search(self, word: str) -> bool:
        if '.' not in word:
            return word in self.words
        n = len(word)
        for item in self.len2words[n]:
            cnt = 0
            while cnt < n and word[cnt] in ['.', item[cnt]]:
                cnt += 1
            if cnt == n:
                return True
        return False


if __name__ == '__main__':
    obj = WordDictionary2()
    obj.addWord('word')
    print(obj.search('w..d'))
