# -*- coding: UTF-8 -*-
"""
title：单词接龙 II
A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:
    Every adjacent pair of words differs by a single letter.
    Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
    sk == endWord
Given two words, beginWord and endWord, and a dictionary wordList, return all the shortest transformation sequences from beginWord to endWord, or an empty list if no such sequence exists. Each sequence should be returned as a list of the words [beginWord, s1, s2, ..., sk].


Example 1:
Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: [["hit","hot","dot","dog","cog"],["hit","hot","lot","log","cog"]]
Explanation: There are 2 shortest transformation sequences:
"hit" -> "hot" -> "dot" -> "dog" -> "cog"
"hit" -> "hot" -> "lot" -> "log" -> "cog"

Example 2:
Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
Output: []
Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.


Constraints:
1 <= beginWord.length <= 5
endWord.length == beginWord.length
1 <= wordList.length <= 1000
wordList[i].length == beginWord.length
beginWord, endWord, and wordList[i] consist of lowercase English letters.
beginWord != endWord
All the words in wordList are unique.
"""
import string
from collections import defaultdict, deque
from typing import List


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        """先使用广度优先遍历构建图，构建过程中，可以知道是否存在最短路径。若存在，则再使用回溯(深度优先遍历)得到所有的最短路径"""
        word_set = set(wordList)
        res = []
        if endWord not in word_set:
            return res
        successors = defaultdict(set)
        if not self.__bfs(beginWord, endWord, word_set, successors):
            return res
        path = [beginWord]
        self.__dfs(beginWord, endWord, successors, path, res)
        return res

    def __bfs(self, begin_word: str, end_word: str, word_set: set, successors: dict) -> bool:
        """使用广度优先遍历构建图，得到后继节点列表successors"""
        queue = deque([begin_word])
        # 当前及以上所有层访问过或将要访问到的word列表
        visited = {begin_word}
        # 下一层将要访问到的word列表，这里面的元素一定不在visited中，因为如果某个元素已存在于visited，再把它加入next_level_visited，会没有意义，
        # 在上面层从这个单词出发寻找end_word，一定会比在下面层从这个单词出发的路径短。
        # 开始进入下一层之前，会把next_level_visited中的所有元素全部并入visited
        next_level_visited = set()

        found = False
        word_len = len(begin_word)
        # letters = [chr(i) for i in range(ord('a'), ord('z') + 1)]

        while queue:
            """
            通过记录当前层(行)的长度，来使一维数组代替二维数组。
            从begin_word到同一层中的所有word，路径长度是一致的。
            当found第一次为True时，就表示找了一条从begin_word出发的最短路径，而最短路径可能存在多条，
            所以需要遍历完同一层中的所有word，从而找出所有的最短路径。
            """
            cur_level_len = len(queue)
            for i in range(cur_level_len):
                cur_word = queue.popleft()
                # 使用从'a'到'z'的26个小写字母，逐个尝试替换cur_word的每个位置，从而找到cur_word的所有后继节点，组成一个列表
                for j in range(word_len):
                    for ch in string.ascii_lowercase:
                        tmp_word = cur_word[:j] + ch + cur_word[j + 1:]
                        if tmp_word in word_set:
                            # 表示这个word在上面所有层都没有遍历过，以及在当前层也不会遇到，所以需要把它放入下一层遍历
                            if tmp_word not in visited:
                                # 这个判断放在当前if外面也是可以的
                                if tmp_word == end_word:
                                    found = True
                                # 避免下层元素重复加入队列queue。next_level_visited是会自动去重的
                                if tmp_word not in next_level_visited:
                                    next_level_visited.add(tmp_word)
                                    queue.append(tmp_word)
                                # 将这个word作为cur_word的后继节点
                                successors[cur_word].add(tmp_word)
            # 说明当前层节点的后继节点列表中出现了end_word，没必要再继续遍历下一层了
            if found:
                break
            # 将next_level_visited中的所有元素都加入到visited中
            visited |= next_level_visited
            next_level_visited.clear()
        return found

    def __dfs(self, begin_word: str, end_word: str, successors: dict, path: list, res: list) -> None:
        """使用深度优先遍历得到所有的最短路径"""
        if begin_word == end_word:
            res.append(path[:])
            return
        if begin_word not in successors:
            return
        for next_word in successors[begin_word]:
            path.append(next_word)
            self.__dfs(next_word, end_word, successors, path, res)
            path.pop()

    def findLadders_2(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        """DFS + BFS 双向搜索。先使用beginword向下扩展，扩展后得到的节点数为m，再使用endWord向上扩展，扩展后得到的节点数为n。
        若m<n，则继续向下扩展；若m>n，则继续向上扩展。双向扩展可以降低时间复杂度"""
        word_set = set(wordList)
        if endWord not in word_set:
            return []
        # 初始时，由beginword向下扩展
        forward_set, backward_set, go_forward = {beginWord}, {endWord}, True
        word_len = len(beginWord)
        # 按endWord向上扩展的方向存储，即 离endWord近的word作为key
        successors = defaultdict(set)
        while forward_set:
            if len(forward_set) > len(backward_set):
                forward_set, backward_set, go_forward = backward_set, forward_set, not go_forward
            # 使用word_set保存尚未访问过的word，forward_set表示当前while循环中即将访问的word集合
            word_set -= forward_set
            # tmp_set表示forward_set的下一层会访问到的word集合
            tmp_set = set()
            for word in forward_set:
                for i in range(word_len):
                    for ch in string.ascii_lowercase:
                        tmp_word = word[:i] + ch + word[i + 1:]
                        if tmp_word in word_set:
                            # word为beginWord时，tmp_set中都是只与beginWord相差一个字母的单词，
                            # 这些单词在successors中是作为key，它们的value都只有一个值，那就是beginWord
                            tmp_set.add(tmp_word)
                            if go_forward:
                                successors[tmp_word].add(word)
                            else:
                                successors[word].add(tmp_word)
            # 若当前层的下一层与反方向的最新层有交集，则表示最短路径已产生
            if tmp_set & backward_set:
                res = [[endWord]]
                # 注意：这里不能从beginWord拼接路径到endWord，只能是从endWord拼接到beginWord。
                # 举例：beginWord = 'a', endWord = 'b', wordList = ['b', 'c']。若是从beginWord拼接到endWord，则successors = {'a': ('b', 'c')}，然后产生两条路径：[['a','b'], ['a','c']]。
                # 但如果是从endWord拼接到beginWord，则successors = {'b': ('a',), 'c': ('a',)}， 然后只有一条路径：[['a','b']]
                while res[0][0] != beginWord:
                    res = [[word] + path for path in res for word in successors[path[0]]]
                return res
            forward_set = tmp_set
        return []


if __name__ == '__main__':
    print(Solution().findLadders_2(beginWord="hit", endWord="cog", wordList=["hot", "dot", "dog", "lot", "log", "cog"]))
