# -*- coding: UTF-8 -*-
"""
title: 单词演变
在字典（单词列表） wordList 中，从单词 beginWord 和 endWord 的 转换序列 是一个按下述规格形成的序列：
    序列中第一个单词是 beginWord 。
    序列中最后一个单词是 endWord 。
    每次转换只能改变一个字母。
    转换过程中的中间单词必须是字典 wordList 中的单词。
给定两个长度相同但内容不同的单词 beginWord 和 endWord 和一个字典 wordList ，找到从 beginWord 到 endWord 的 最短转换序列 中的 单词数目 。如果不存在这样的转换序列，返回 0。


示例 1：
输入：beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
输出：5
解释：一个最短转换序列是 "hit" -> "hot" -> "dot" -> "dog" -> "cog", 返回它的长度 5。

示例 2：
输入：beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
输出：0
解释：endWord "cog" 不在字典中，所以无法进行转换。


提示：
1 <= beginWord.length <= 10
endWord.length == beginWord.length
1 <= wordList.length <= 5000
wordList[i].length == beginWord.length
beginWord、endWord 和 wordList[i] 由小写英文字母组成
beginWord != endWord
wordList 中的所有字符串 互不相同
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
