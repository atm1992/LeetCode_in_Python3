# -*- coding: utf-8 -*-
# @date: 2023/4/1
# @author: liuquan
"""
title: 图中的最短环
There is a bi-directional graph with n vertices, where each vertex is labeled from 0 to n - 1. The edges in the graph are represented by a given 2D integer array edges, where edges[i] = [ui, vi] denotes an edge between vertex ui and vertex vi. Every vertex pair is connected by at most one edge, and no vertex has an edge to itself.
Return the length of the shortest cycle in the graph. If no cycle exists, return -1.
A cycle is a path that starts and ends at the same node, and each edge in the path is used only once.


Example 1:
Input: n = 7, edges = [[0,1],[1,2],[2,0],[3,4],[4,5],[5,6],[6,3]]
Output: 3
Explanation: The cycle with the smallest length is : 0 -> 1 -> 2 -> 0

Example 2:
Input: n = 4, edges = [[0,1],[0,2]]
Output: -1
Explanation: There are no cycles in this graph.


Constraints:
2 <= n <= 1000
1 <= edges.length <= 1000
edges[i].length == 2
0 <= ui, vi < n
ui != vi
There are no repeated edges.
"""
from collections import defaultdict, deque
from typing import List


class Solution:
    def findShortestCycle(self, n: int, edges: List[List[int]]) -> int:
        """
        BFS。将所有度大于等于2的点作为起点，计算包含该点的最短环长度。度小于2的节点不可能在环中
        """
        nodes = set()
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            if len(graph[u]) >= 2:
                nodes.add(u)
            if len(graph[v]) >= 2:
                nodes.add(v)
        # n个节点最多组成长度为n的环。若最终res为n+1，则表示不存在环，返回 -1
        res = n + 1
        # 至少要3个节点才能组成环
        while len(nodes) >= 3:
            cur = nodes.pop()
            # cur, father
            queue = deque([(cur, -1)])
            node2dist = {cur: 0}
            found = False
            while queue:
                u, f = queue.popleft()
                d = node2dist[u]
                for v in graph[u]:
                    if v == f:
                        continue
                    if v in node2dist:
                        res = min(res, d + node2dist[v] + 1)
                        found = True
                        break
                    # 只有在nodes中的节点才有可能在环中
                    if v in nodes:
                        queue.append((v, u))
                        node2dist[v] = d + 1
                if found:
                    break
        return -1 if res == n + 1 else res


if __name__ == '__main__':
    print(Solution().findShortestCycle(n=7, edges=[[5, 0], [4, 0], [1, 5], [6, 1], [3, 4], [2, 6], [2, 1]]))
