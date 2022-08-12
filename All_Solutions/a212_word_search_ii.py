# -*- coding: UTF-8 -*-
"""
title: 单词搜索 II
Given an m x n board of characters and a list of strings words, return all words on the board.
Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.


Example 1:
Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
Output: ["eat","oath"]

Example 2:
Input: board = [["a","b"],["c","d"]], words = ["abcb"]
Output: []


Constraints:
m == board.length
n == board[i].length
1 <= m, n <= 12
board[i][j] is a lowercase English letter.
1 <= words.length <= 3 * 10^4
1 <= words[i].length <= 10
words[i] consists of lowercase English letters.
All the strings of words are unique.
"""
from typing import List
from collections import defaultdict


class TrieNode:
    def __init__(self):
        # ch -> TrieNode()。若当前node是某个单词的结尾，则node.word为整个单词字符串，否则为默认值空字符串
        self.children = defaultdict(TrieNode)
        self.word = ""

    def insert(self, word: str) -> None:
        node = self
        for ch in word:
            # node.children[ch] 的默认值为 TrieNode()
            node = node.children[ch]
        # 若node.word不等于默认值""，就表示这个TrieNode节点是当前word的尾节点
        node.word = word


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        """回溯 + 字典树"""
        trie_root = TrieNode()
        for word in words:
            trie_root.insert(word)

        def dfs(node: TrieNode, i: int, j: int) -> None:
            ch = board[i][j]
            if ch not in node.children:
                return
            node = node.children[ch]
            if node.word != "":
                # 这里不return的原因是，words中可能存在这样的两个单词，单词a是单词b的前缀，所以需要继续向下遍历
                res.add(node.word)
            # 在此次回溯中，避免走回这里
            board[i][j] = '#'
            for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if 0 <= x < m and 0 <= y < n and board[x][y] != '#':
                    dfs(node, x, y)
            board[i][j] = ch

        # 同一个单词可能在多个不同的路径中出现，所以需要去重
        res = set()
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                dfs(trie_root, i, j)
        return list(res)

    def findWords_2(self, board: List[List[str]], words: List[str]) -> List[str]:
        """回溯 + 字典树。除了可以使用set对结果集进行去重，还可以在dfs过程中，匹配过一次后，将该单词从字典树中删除，不断对字典树进行剪枝。执行速度比上面快很多"""
        trie_root = TrieNode()
        for word in words:
            trie_root.insert(word)

        def dfs(node: TrieNode, i: int, j: int) -> None:
            ch = board[i][j]
            if ch not in node.children:
                return
            child = node.children[ch]
            if child.word != "":
                res.append(child.word)
                # 将该单词从字典树中删除，该单词将不再会被添加到res中了
                child.word = ""
            if child.children:
                # 在此次回溯中，避免走回这里
                board[i][j] = '#'
                for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                    if 0 <= x < m and 0 <= y < n and board[x][y] != '#':
                        dfs(child, x, y)
                board[i][j] = ch
            else:
                # 若当前node的子节点没有子节点了，则可将当前子节点从node.children中删除，逐步对字典树进行剪枝
                node.children.pop(ch)

        # 同一个单词可能在多个不同的路径中出现，所以需要去重
        res = []
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                dfs(trie_root, i, j)
        return res


if __name__ == '__main__':
    print(Solution().findWords(
        board=[["o", "a", "a", "n"], ["e", "t", "a", "e"], ["i", "h", "k", "r"], ["i", "f", "l", "v"]],
        words=["oath", "pea", "eat", "rain"]))
