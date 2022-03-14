# -*- coding: UTF-8 -*-
"""
title: 单词接龙
A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:
    Every adjacent pair of words differs by a single letter.
    Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
    sk == endWord
Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.


Example 1:
Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5
Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.

Example 2:
Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
Output: 0
Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.


Constraints:
1 <= beginWord.length <= 10
endWord.length == beginWord.length
1 <= wordList.length <= 5000
wordList[i].length == beginWord.length
beginWord, endWord, and wordList[i] consist of lowercase English letters.
beginWord != endWord
All the words in wordList are unique.
"""
import string
from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set = set(wordList)
        if endWord not in word_set:
            return 0
        forward_set, backward_set = {beginWord}, {endWord}
        word_len = len(beginWord)
        # 若存在最短路径，则路径长度最小为2，即 beginWord ——> endWord
        cnt = 2
        while forward_set:
            if len(forward_set) > len(backward_set):
                forward_set, backward_set = backward_set, forward_set
            word_set -= forward_set
            tmp_set = set()
            for word in forward_set:
                for i in range(word_len):
                    for ch in string.ascii_lowercase:
                        tmp_word = word[:i] + ch + word[i + 1:]
                        if tmp_word in word_set:
                            tmp_set.add(tmp_word)
            if tmp_set & backward_set:
                return cnt
            forward_set = tmp_set
            cnt += 1
        return 0


if __name__ == '__main__':
    print(Solution().ladderLength(beginWord="hit", endWord="cog", wordList=["hot", "dot", "dog", "lot", "log", "cog"]))
