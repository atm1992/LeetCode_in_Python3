# -*- coding: UTF-8 -*-
"""
title: 统计无向图中无法互相到达点对数
You are given an integer n. There is an undirected graph with n nodes, numbered from 0 to n - 1. You are given a 2D integer array edges where edges[i] = [ai, bi] denotes that there exists an undirected edge connecting nodes ai and bi.
Return the number of pairs of different nodes that are unreachable from each other.


Example 1:
Input: n = 3, edges = [[0,1],[0,2],[1,2]]
Output: 0
Explanation: There are no pairs of nodes that are unreachable from each other. Therefore, we return 0.

Example 2:
Input: n = 7, edges = [[0,2],[0,5],[2,4],[1,6],[5,4]]
Output: 14
Explanation: There are 14 pairs of nodes that are unreachable from each other:
[[0,1],[0,3],[0,6],[1,2],[1,3],[1,4],[1,5],[2,3],[2,6],[3,4],[3,5],[3,6],[4,6],[5,6]].
Therefore, we return 14.


Constraints:
1 <= n <= 10^5
0 <= edges.length <= 2 * 10^5
edges[i].length == 2
0 <= ai, bi < n
ai != bi
There are no repeated edges.
"""
from collections import defaultdict
from typing import List


class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        """并查集"""

        def union(i: int, j: int) -> None:
            father[find_father(i)] = find_father(j)

        def find_father(i: int) -> int:
            if i != father[i]:
                father[i] = find_father(father[i])
            return father[i]

        father = list(range(n))
        for a, b in edges:
            union(a, b)

        root2size = defaultdict(int)
        # 统计每个连通分量root下的节点个数
        for i in range(n):
            root2size[find_father(i)] += 1
        res = 0
        # 总的节点个数n中除去当前及之前所有的连通分量，剩余的节点个数
        rest_size = n
        # cur_size 表示当前连通分量中的节点个数
        for cur_size in root2size.values():
            rest_size -= cur_size
            res += cur_size * rest_size
        return res

    def countPairs_2(self, n: int, edges: List[List[int]]) -> int:
        """DFS"""

        def dfs(i: int) -> None:
            nonlocal cur_size
            visited[i] = True
            cur_size += 1
            for j in graph[i]:
                if not visited[j]:
                    dfs(j)

        graph = [[] for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        visited = [False] * n
        # 之前所有的连通分量中的节点个数
        existing_size = 0
        # 当前连通分量中的节点个数
        cur_size = 0
        res = 0
        for i in range(n):
            if not visited[i]:
                cur_size = 0
                dfs(i)
                res += cur_size * existing_size
                existing_size += cur_size
        return res


if __name__ == '__main__':
    print(Solution().countPairs(n=7, edges=[[0, 2], [0, 5], [2, 4], [1, 6], [5, 4]]))
