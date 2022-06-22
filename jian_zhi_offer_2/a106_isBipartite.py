# -*- coding: UTF-8 -*-
"""
title: 二分图
存在一个 无向图 ，图中有 n 个节点。其中每个节点都有一个介于 0 到 n - 1 之间的唯一编号。
给定一个二维数组 graph ，表示图，其中 graph[u] 是一个节点数组，由节点 u 的邻接节点组成。形式上，对于 graph[u] 中的每个 v ，都存在一条位于节点 u 和节点 v 之间的无向边。该无向图同时具有以下属性：
    不存在自环（graph[u] 不包含 u）。
    不存在平行边（graph[u] 不包含重复值）。
    如果 v 在 graph[u] 内，那么 u 也应该在 graph[v] 内（该图是无向图）
    这个图可能不是连通图，也就是说两个节点 u 和 v 之间可能不存在一条连通彼此的路径。
二分图 定义：如果能将一个图的节点集合分割成两个独立的子集 A 和 B ，并使图中的每一条边的两个节点一个来自 A 集合，一个来自 B 集合，就将这个图称为 二分图 。
如果图是二分图，返回 true ；否则，返回 false 。


示例 1：
输入：graph = [[1,2,3],[0,2],[0,1,3],[0,2]]
输出：false
解释：不能将节点分割成两个独立的子集，以使每条边都连通一个子集中的一个节点与另一个子集中的一个节点。

示例 2：
输入：graph = [[1,3],[0,2],[1,3],[0,2]]
输出：true
解释：可以将节点分成两组: {0, 2} 和 {1, 3} 。


提示：
graph.length == n
1 <= n <= 100
0 <= graph[u].length < n
0 <= graph[u][i] <= n - 1
graph[u] 不会包含 u
graph[u] 的所有值 互不相同
如果 graph[u] 包含 v，那么 graph[v] 也会包含 u

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
