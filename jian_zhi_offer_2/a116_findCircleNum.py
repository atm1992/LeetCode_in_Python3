# -*- coding: UTF-8 -*-
"""
title: 省份数量
有 n 个城市，其中一些彼此相连，另一些没有相连。如果城市 a 与城市 b 直接相连，且城市 b 与城市 c 直接相连，那么城市 a 与城市 c 间接相连。
省份 是一组直接或间接相连的城市，组内不含其他没有相连的城市。
给你一个 n x n 的矩阵 isConnected ，其中 isConnected[i][j] = 1 表示第 i 个城市和第 j 个城市直接相连，而 isConnected[i][j] = 0 表示二者不直接相连。
返回矩阵中 省份 的数量。


示例 1：
输入：isConnected = [[1,1,0],[1,1,0],[0,0,1]]
输出：2

示例 2：
输入：isConnected = [[1,0,0],[0,1,0],[0,0,1]]
输出：3


提示：
1 <= n <= 200
n == isConnected.length
n == isConnected[i].length
isConnected[i][j] 为 1 或 0
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


if __name__ == '__main__':
    print(Solution().findCircleNum_3(isConnected=[[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
