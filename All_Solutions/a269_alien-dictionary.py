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
        拓扑排序 + DFS。得到反向拓扑序列
        假设 words = ["wrt","wrf"]，从中可以确定 't' 在 'f' 前面，但是无法确定 'w'、'r' 与它俩之间的顺序。
        所以最终结果只需确保't'、'f'之间的顺序正确即可，至于'w'、'r'，可在任意位置插入。即 'wrtf'、'wtrf'、'rtfw'、…… 都是正确结果。
        """
        # 记录所有的字母，由于有些字母可能不存在后继节点(即 后继节点为空数组)，所以graph中的key集合会小于等于all_ch
        all_ch = set()
        for word in words:
            all_ch.update(word)
        # 记录所有的有向边，pre -> [curs]
        graph = defaultdict(list)
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            for c1, c2 in zip(w1, w2):
                if c1 != c2:
                    graph[c1].append(c2)
                    break
            else:
                # words中允许存在重复单词
                if len(w1) > len(w2):
                    return ""
        # 记录各个字母(顶点)的当前访问状态。0 - 未搜索过；1 - 搜索中，回溯结束时，将字母(顶点)加入stack；2 - 搜索完成，字母(顶点)已加入stack。
        visited = defaultdict(int)
        # 最终返回stack的逆序。因为是cur节点先加入，当pre指向的所有cur节点都加入stack后，才会将pre节点加入stack
        stack = []
        # 记录是否存在环路
        has_loop = False

        def dfs(u: str) -> None:
            nonlocal has_loop
            # 将当前字母(顶点)的状态更新为 搜索中
            visited[u] = 1
            for v in graph[u]:
                if visited[v] == 0:
                    dfs(v)
                    # 剪枝。一旦发现存在环路，立刻停止搜索
                    if has_loop:
                        return
                elif visited[v] == 1:
                    has_loop = True
                    return
            # 只有当当前字母(顶点)的所有后继节点都搜索完成(加入stack)后，当前字母(顶点)才算搜索完成(加入stack)
            visited[u] = 2
            stack.append(u)

        for u in all_ch:
            if visited[u] == 0:
                dfs(u)
                if has_loop:
                    break
        # return "".join(stack[::-1]) if len(stack) == len(all_ch) else ""
        return "" if has_loop else "".join(stack[::-1])

    def alienOrder_2(self, words: List[str]) -> str:
        """拓扑排序 + BFS。得到正向拓扑序列，推荐此方法"""
        # 记录所有的字母，由于有些字母可能不存在后继节点(即 后继节点为空数组)，所以graph中的key集合会小于等于all_ch
        all_ch = set()
        for word in words:
            all_ch.update(word)
        # 记录所有的有向边，pre -> [curs]
        graph = defaultdict(list)
        in_degree = defaultdict(int)
        # 计算所有字母(顶点)的入度。之后将所有入度为0的字母(顶点)加入队列，作为BFS的起点
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            for c1, c2 in zip(w1, w2):
                if c1 != c2:
                    graph[c1].append(c2)
                    in_degree[c2] += 1
                    break
            else:
                # words中允许存在重复单词
                if len(w1) > len(w2):
                    return ""
        # in_degree中的key不一定是完整的，因为有些字母可能不存在前驱节点，所以遍历的是all_ch
        queue = [ch for ch in all_ch if in_degree[ch] == 0]
        for u in queue:
            for v in graph[u]:
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    queue.append(v)
        # 若存在环路，则环路中的所有顶点都无法将入度降到0，也就不会加入到队列了
        return "".join(queue) if len(queue) == len(all_ch) else ""


if __name__ == '__main__':
    print(Solution().alienOrder(words=["wrt", "wrf", "er", "ett", "rftt"]))
