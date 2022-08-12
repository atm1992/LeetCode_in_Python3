# -*- coding: UTF-8 -*-
"""
title: 省份数量
There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.
A province is a group of directly or indirectly connected cities and no other cities outside of the group.
You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.
Return the total number of provinces.


Example 1:
Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
Output: 2

Example 2:
Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
Output: 3


Constraints:
1 <= n <= 200
n == isConnected.length
n == isConnected[i].length
isConnected[i][j] is 1 or 0.
isConnected[i][i] == 1
isConnected[i][j] == isConnected[j][i]
"""
from collections import deque
from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        """DFS"""

        def dfs(i: int) -> None:
            visited.add(i)
            for j in graph[i]:
                if j not in visited:
                    dfs(j)

        res = 0
        n = len(isConnected)
        visited = set()
        graph = [[] for _ in range(n)]
        for i in range(n - 1):
            for j in range(i + 1, n):
                if isConnected[i][j] == 1:
                    graph[i].append(j)
                    graph[j].append(i)

        for i in range(n):
            if i not in visited:
                dfs(i)
                res += 1
        return res

    def findCircleNum_2(self, isConnected: List[List[int]]) -> int:
        """BFS"""
        res = 0
        n = len(isConnected)
        visited = set()
        queue = deque()
        graph = [[] for _ in range(n)]
        for i in range(n - 1):
            for j in range(i + 1, n):
                if isConnected[i][j] == 1:
                    graph[i].append(j)
                    graph[j].append(i)

        for i in range(n):
            if i in visited:
                continue
            queue.append(i)
            while queue:
                u = queue.popleft()
                visited.add(u)
                for v in graph[u]:
                    if v not in visited:
                        queue.append(v)
            res += 1
        return res

    def findCircleNum_3(self, isConnected: List[List[int]]) -> int:
        """并查集"""

        def union(i: int, j: int) -> None:
            """合并i、j所在的两棵树(两个集合)。合并后，i_root指向j_root"""
            father[find_father(i)] = find_father(j)

        def find_father(i: int) -> int:
            """查找输入节点的根节点"""
            # 只有根节点的父节点才为本身
            if i != father[i]:
                father[i] = find_father(father[i])
            return father[i]

        n = len(isConnected)
        # 初始时，认为各个节点的父节点(根节点)为本身。通常命名为 father or parent
        father = list(range(n))
        for i in range(n - 1):
            for j in range(i + 1, n):
                if isConnected[i][j] == 1:
                    union(i, j)
        # 统计有多少个根节点，因为只有根节点的父节点才为本身，即 i == father[i]
        return sum(i == father[i] for i in range(n))
