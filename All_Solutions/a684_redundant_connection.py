# -*- coding: UTF-8 -*-
"""
title: 冗余连接
In this problem, a tree is an undirected graph that is connected and has no cycles.
You are given a graph that started as a tree with n nodes labeled from 1 to n, with one additional edge added. The added edge has two different vertices chosen from 1 to n, and was not an edge that already existed. The graph is represented as an array edges of length n where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the graph.
Return an edge that can be removed so that the resulting graph is a tree of n nodes. If there are multiple answers, return the answer that occurs last in the input.


Example 1:
Input: edges = [[1,2],[1,3],[2,3]]
Output: [2,3]

Example 2:
Input: edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
Output: [1,4]


Constraints:
n == edges.length
3 <= n <= 1000
edges[i].length == 2
1 <= ai < bi <= edges.length
ai != bi
There are no repeated edges.
The given graph is connected.
"""
from typing import List


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        """
        并查集。
        n个节点的树，正常情况下应该只有n-1条边，而edges中有n条边，则多出来的那条边会使得树中出现环，顺序遍历edges，使得环出现的那条边就是需要删除的。
        """

        def union(i: int, j: int) -> None:
            father[find_father(i)] = find_father(j)

        def find_father(i: int) -> int:
            if i != father[i]:
                father[i] = find_father(father[i])
            return father[i]

        n = len(edges)
        # 1～n 这n个节点的根节点，初始时为本身
        father = list(range(n + 1))
        for i, j in edges:
            # i、j 这两个节点已经在树中了，i、j 之间再添加一条边的话，就会出现环了
            if find_father(i) == find_father(j):
                return [i, j]
            union(i, j)
