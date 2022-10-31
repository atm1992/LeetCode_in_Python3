# -*- coding: UTF-8 -*-
"""
title: 无向图中连通分量的数目
You have a graph of n nodes. You are given an integer n and an array edges where edges[i] = [ai, bi] indicates that there is an edge between ai and bi in the graph.
Return the number of connected components in the graph.


Example 1:
Input: n = 5, edges = [[0,1],[1,2],[3,4]]
Output: 2

Example 2:
Input: n = 5, edges = [[0,1],[1,2],[2,3],[3,4]]
Output: 1


Constraints:
1 <= n <= 2000
1 <= edges.length <= 5000
edges[i].length == 2
0 <= ai <= bi < n
ai != bi
There are no repeated edges.
"""
from collections import defaultdict, deque
from typing import List


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        """并查集"""

        def union(i: int, j: int) -> None:
            parent[find(i)] = find(j)

        def find(i: int) -> int:
            if parent[i] != i:
                parent[i] = find(parent[i])
            return parent[i]

        parent = list(range(n))
        for i, j in edges:
            union(i, j)

        return sum(idx == num for idx, num in enumerate(parent))

    def countComponents_2(self, n: int, edges: List[List[int]]) -> int:
        """DFS"""

        def dfs(i: int) -> None:
            visited[i] = True
            for j in graph[i]:
                if not visited[j]:
                    dfs(j)

        graph = defaultdict(list)
        for i, j in edges:
            graph[i].append(j)
            graph[j].append(i)
        visited = [False] * n
        res = 0
        for i in range(n):
            if not visited[i]:
                res += 1
                dfs(i)
        return res

    def countComponents_3(self, n: int, edges: List[List[int]]) -> int:
        """BFS"""

        def bfs(i: int) -> None:
            queue = deque([i])
            while queue:
                cur = queue.popleft()
                for j in graph[cur]:
                    if not visited[j]:
                        visited[j] = True
                        queue.append(j)

        graph = defaultdict(list)
        for i, j in edges:
            graph[i].append(j)
            graph[j].append(i)
        visited = [False] * n
        res = 0
        for i in range(n):
            if not visited[i]:
                res += 1
                visited[i] = True
                bfs(i)
        return res


if __name__ == '__main__':
    print(Solution().countComponents_3(n=5, edges=[[0, 1], [1, 2], [2, 3], [3, 4]]))
