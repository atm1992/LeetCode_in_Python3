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
        """双向BFS。先使用beginword向下扩展，扩展后得到的节点数为m，再使用endWord向上扩展，扩展后得到的节点数为n。
        若m<n，则继续向下扩展；若m>n，则继续向上扩展。双向扩展可以降低时间复杂度"""
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
            # 使用word_set保存尚未访问过的word，forward_set表示当前while循环中即将访问的word集合
            word_set -= forward_set
            # tmp_set表示forward_set的下一层会访问到的word集合
            tmp_set = set()
            for word in forward_set:
                for i in range(word_len):
                    for ch in string.ascii_lowercase:
                        tmp_word = word[:i] + ch + word[i+1:]
                        if tmp_word in word_set:
                            tmp_set.add(tmp_word)
            # 若当前层的下一层与反方向的最新层有交集，则表示最短路径已产生
            if tmp_set & backward_set:
                return cnt
            forward_set = tmp_set
            cnt += 1
        return 0


if __name__ == '__main__':
    print(Solution().ladderLength(beginWord="hit", endWord="cog", wordList=["hot", "dot", "dog", "lot", "log", "cog"]))
