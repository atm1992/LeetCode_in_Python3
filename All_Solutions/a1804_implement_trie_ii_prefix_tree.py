# -*- coding: UTF-8 -*-
"""
title: 实现 Trie （前缀树）II
A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.
Implement the Trie class:
    Trie() Initializes the trie object.
    void insert(String word) Inserts the string word into the trie.
    int countWordsEqualTo(String word) Returns the number of instances of the string word in the trie.
    int countWordsStartingWith(String prefix) Returns the number of strings in the trie that have the string prefix as a prefix.
    void erase(String word) Erases the string word from the trie.


Example 1:
Input
["Trie", "insert", "insert", "countWordsEqualTo", "countWordsStartingWith", "erase", "countWordsEqualTo", "countWordsStartingWith", "erase", "countWordsStartingWith"]
[[], ["apple"], ["apple"], ["apple"], ["app"], ["apple"], ["apple"], ["app"], ["apple"], ["app"]]
Output
[null, null, null, 2, 2, null, 1, 1, null, 0]
Explanation
Trie trie = new Trie();
trie.insert("apple");               // Inserts "apple".
trie.insert("apple");               // Inserts another "apple".
trie.countWordsEqualTo("apple");    // There are two instances of "apple" so return 2.
trie.countWordsStartingWith("app"); // "app" is a prefix of "apple" so return 2.
trie.erase("apple");                // Erases one "apple".
trie.countWordsEqualTo("apple");    // Now there is only one instance of "apple" so return 1.
trie.countWordsStartingWith("app"); // return 1
trie.erase("apple");                // Erases "apple". Now the trie is empty.
trie.countWordsStartingWith("app"); // return 0


Constraints:
1 <= word.length, prefix.length <= 2000
word and prefix consist only of lowercase English letters.
At most 3 * 10^4 calls in total will be made to insert, countWordsEqualTo, countWordsStartingWith, and erase.
It is guaranteed that for any function call to erase, the string word will exist in the trie.
"""


class Trie:

    def __init__(self):
        # 26叉树
        self.children = [None] * 26
        # 注意：需要区分 以某字符结尾的单词数 和 以某字符为前缀的单词数，不能单纯地使用 self.is_end = True 和 self.as_prefix 来记录以某字符结尾的单词数，
        # 因为即使该字符是某单词的结尾，以该字符结尾的单词数 和 以该字符为前缀的单词数 之间也不一定相等关系，也可能是小于关系。
        self.as_word = 0
        self.as_prefix = 0

    def insert(self, word: str) -> None:
        node = self
        for ch in word:
            idx = ord(ch) - ord('a')
            if not node.children[idx]:
                # 将对应字符所在下标的元素赋值为一个Trie节点
                node.children[idx] = Trie()
            node = node.children[idx]
            node.as_prefix += 1
        node.as_word += 1

    def countWordsEqualTo(self, word: str) -> int:
        node = self
        for ch in word:
            idx = ord(ch) - ord('a')
            if not node.children[idx]:
                return 0
            node = node.children[idx]
        return node.as_word

    def countWordsStartingWith(self, prefix: str) -> int:
        node = self
        for ch in prefix:
            idx = ord(ch) - ord('a')
            if not node.children[idx]:
                return 0
            node = node.children[idx]
        return node.as_prefix

    def erase(self, word: str) -> None:
        node = self
        for ch in word:
            idx = ord(ch) - ord('a')
            # It is guaranteed that for any function call to erase, the string word will exist in the trie.
            node = node.children[idx]
            node.as_prefix -= 1
        node.as_word -= 1


if __name__ == '__main__':
    obj = Trie()
    obj.insert("apple")
    obj.insert("apple")
    print(obj.countWordsEqualTo("apple"))
    print(obj.countWordsStartingWith("app"))
    obj.erase("apple")
    print(obj.countWordsEqualTo("apple"))
    print(obj.countWordsStartingWith("app"))
    obj.erase("apple")
    print(obj.countWordsStartingWith("app"))
