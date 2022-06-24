# -*- coding: UTF-8 -*-
"""
title: 火星词典
There is a new alien language that uses the English alphabet. However, the order among the letters is unknown to you.
You are given a list of strings words from the alien language's dictionary, where the strings in words are sorted lexicographically by the rules of this new language.
Return a string of the unique letters in the new alien language sorted in lexicographically increasing order by the new language's rules. If there is no solution, return "". If there are multiple solutions, return any of them.
A string s is lexicographically smaller than a string t if at the first letter where they differ, the letter in s comes before the letter in t in the alien language. If the first min(s.length, t.length) letters are the same, then s is smaller if and only if s.length < t.length.


Example 1:
Input: words = ["wrt","wrf","er","ett","rftt"]
Output: "wertf"

Example 2:
Input: words = ["z","x"]
Output: "zx"

Example 3:
Input: words = ["z","x","z"]
Output: ""
Explanation: The order is invalid, so return "".


Constraints:
1 <= words.length <= 100
1 <= words[i].length <= 100
words[i] consists of only lowercase English letters.
"""
from collections import defaultdict
from typing import List


class Solution:
    def alienOrder(self, words: List[str]) -> str:
        """
        拓扑排序 + DFS
        假设 words = ["wrt","wrf"]，从中可以确定 't' 在 'f' 前面，但是无法确定 'w'、'r' 与它俩之间的顺序。
        所以最终结果只需确保't'、'f'之间的顺序正确即可，至于'w'、'r'，可在任意位置插入。即 'wrtf'、'wtrf'、'rtfw'、…… 都是正确结果。
        """
        # 构建字符集
        char_set = set()
        for word in words:
            char_set.update(word)
        char_set_size = len(char_set)

        # 构建有向图。位置在前的字符为key，位置在其后的所有字符组成列表作为value
        graph = defaultdict(list)
        n = len(words)
        for i in range(n - 1):
            w1, w2 = words[i], words[i + 1]
            len1, len2 = len(w1), len(w2)
            for j in range(max(len1, len2)):
                # 不合法，即使是j同时到达len1、len2，即 w1 与 w2完全相同，那也是不合法的
                if j == len2:
                    return ""
                # 表示通过w1 与 w2无法确定字符间的顺序，因为w1恰好是w2的前缀
                if j == len1:
                    break
                if w1[j] != w2[j]:
                    graph[w1[j]].append(w2[j])
                    break

        # 拓扑排序
        # 记录有向图中是否存在环，若存在环，则表示不合法
        has_cycle = False
        cur_visited = set()
        all_visited = set()
        # 记录排序结果
        res = []

        def dfs(ch: str) -> None:
            nonlocal has_cycle
            if ch in cur_visited:
                has_cycle = True
                return
            if ch in all_visited:
                return
            all_visited.add(ch)
            cur_visited.add(ch)
            for next_ch in graph[ch]:
                dfs(next_ch)
                # 剪枝
                if has_cycle:
                    return
            # 注意：res中的字符是最终结果的逆序
            res.append(ch)
            cur_visited.remove(ch)

        for ch in list(graph.keys()):
            dfs(ch)
            if has_cycle:
                return ""
            # 已经确定了所有字符间的顺序，没必要继续循环了
            if len(res) == char_set_size:
                break

        # 整理最终结果
        if len(res) < char_set_size:
            res.extend(list(char_set - set(res)))
        return ''.join(res[::-1])


if __name__ == '__main__':
    print(Solution().alienOrder(words=["wrt", "wrf", "er", "ett", "rftt"]))
