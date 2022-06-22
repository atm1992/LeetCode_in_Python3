# -*- coding: UTF-8 -*-
"""
title: 判断二分图
There is an undirected graph with n nodes, where each node is numbered between 0 and n - 1. You are given a 2D array graph, where graph[u] is an array of nodes that node u is adjacent to. More formally, for each v in graph[u], there is an undirected edge between node u and node v. The graph has the following properties:
    There are no self-edges (graph[u] does not contain u).
    There are no parallel edges (graph[u] does not contain duplicate values).
    If v is in graph[u], then u is in graph[v] (the graph is undirected).
    The graph may not be connected, meaning there may be two nodes u and v such that there is no path between them.
A graph is bipartite if the nodes can be partitioned into two independent sets A and B such that every edge in the graph connects a node in set A and a node in set B.
Return true if and only if it is bipartite.


Example 1:
Input: graph = [[1,2,3],[0,2],[0,1,3],[0,2]]
Output: false
Explanation: There is no way to partition the nodes into two independent sets such that every edge connects a node in one and a node in the other.

Example 2:
Input: graph = [[1,3],[0,2],[1,3],[0,2]]
Output: true
Explanation: We can partition the nodes into two sets: {0, 2} and {1, 3}.


Constraints:
graph.length == n
1 <= n <= 100
0 <= graph[u].length < n
0 <= graph[u][i] <= n - 1
graph[u] does not contain u.
All the values of graph[u] are unique.
If graph[u] contains v, then graph[v] contains u.

解题思路：       # 染色法
1、若给定的无向图是连通的，则可从任一节点开始染色(假设染成红色)，之后从这个节点开始遍历整个图，与它直接相连的所有节点都染成另一种颜色(假设为绿色)，
表示那些直接相连的节点与它不属于同一个集合。然后再把与这些绿色节点直接相连的所有节点都染成红色，染色过程中，这些相连节点可能存在3种情况：
1）未被染色过，则直接染为红色；
2）已被染成红色，则无需再染色，忽略
3）已被染成绿色，则返回False，说明给定的无向图不是一个二分图
注意：由于题目并没要求给定的无向图是连通的，所以需要进行多次遍历，直到每个节点都被染色，或确定答案为False为止。每次遍历都是从一个未被染色过的节点开始
"""
from collections import deque
from typing import List


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        """DFS"""

        def dfs(node: int, c: int) -> None:
            nonlocal res
            color[node] = c
            other_c = GREEN if c == RED else RED
            for neighbor in graph[node]:
                if color[neighbor] == UNCOLORED:
                    dfs(neighbor, other_c)
                elif color[neighbor] != other_c:
                    res = False
                if not res:
                    break

        n = len(graph)
        UNCOLORED, RED, GREEN = 0, 1, 2
        # 初始时，所有节点都是未被染色过的
        color = [UNCOLORED] * n
        res = True
        for i in range(n):
            if color[i] == UNCOLORED:
                # 先染成红色
                dfs(i, RED)
                if not res:
                    break
        return res

    def isBipartite_2(self, graph: List[List[int]]) -> bool:
        """BFS"""
        n = len(graph)
        UNCOLORED, RED, GREEN = 0, 1, 2
        # 初始时，所有节点都是未被染色过的
        color = [UNCOLORED] * n
        for i in range(n):
            if color[i] != UNCOLORED:
                continue
            queue = deque([i])
            color[i] = RED
            while queue:
                node = queue.popleft()
                other_c = GREEN if color[node] == RED else RED
                for neighbor in graph[node]:
                    if color[neighbor] == UNCOLORED:
                        color[neighbor] = other_c
                        queue.append(neighbor)
                    elif color[neighbor] != other_c:
                        return False
        return True
