# -*- coding: UTF-8 -*-
"""
title: 统计子树中城市之间最大距离
There are n cities numbered from 1 to n. You are given an array edges of size n-1, where edges[i] = [ui, vi] represents a bidirectional edge between cities ui and vi. There exists a unique path between each pair of cities. In other words, the cities form a tree.
A subtree is a subset of cities where every city is reachable from every other city in the subset, where the path between each pair passes through only the cities from the subset. Two subtrees are different if there is a city in one subtree that is not present in the other.
For each d from 1 to n-1, find the number of subtrees in which the maximum distance between any two cities in the subtree is equal to d.
Return an array of size n-1 where the dth element (1-indexed) is the number of subtrees in which the maximum distance between any two cities is equal to d.
Notice that the distance between the two cities is the number of edges in the path between them.


Example 1:
Input: n = 4, edges = [[1,2],[2,3],[2,4]]
Output: [3,4,0]
Explanation:
The subtrees with subsets {1,2}, {2,3} and {2,4} have a max distance of 1.
The subtrees with subsets {1,2,3}, {1,2,4}, {2,3,4} and {1,2,3,4} have a max distance of 2.
No subtree has two nodes where the max distance between them is 3.

Example 2:
Input: n = 2, edges = [[1,2]]
Output: [1]

Example 3:
Input: n = 3, edges = [[1,2],[2,3]]
Output: [2,1]


Constraints:
2 <= n <= 15
edges.length == n-1
edges[i].length == 2
1 <= ui, vi <= n
All pairs (ui, vi) are distinct.
"""
from collections import defaultdict
from typing import List


class Solution:
    def countSubgraphsForEachDiameter(self, n: int, edges: List[List[int]]) -> List[int]:
        """
        二进制枚举 + DFS。计算二叉树的直径可参考LeetCode题543
        枚举所有的节点集合，注意：一个节点集合并不一定是一棵树，也可能是森林(不连通的多棵树)
        例如：11 表示节点集合{1,2}，2^n - 1 表示包含了所有节点的集合，即 {1,2,……,n}
        为方便表示，将节点的编号改为从0开始，即 0 ~ n-1
        """
        res = [0] * (n - 1)
        graph = defaultdict(list)
        for u, v in edges:
            graph[u - 1].append(v - 1)
            graph[v - 1].append(u - 1)

        for mask in range(3, 1 << n):
            # 直径diameter至少为1，因此节点集合中至少要有两个节点
            if mask & (mask - 1) == 0:
                continue
            visited, diameter = 0, 0

            def dfs(u: int) -> int:
                """计算以节点u为根节点的子树高度"""
                nonlocal visited, diameter
                # 标记节点u被访问过
                visited |= 1 << u
                height = 0
                # 注意：这里跟LeetCode题543不同的是，这里的不是二叉树
                for v in graph[u]:
                    # 节点v没被访问过，并且节点v在当前集合mask中
                    if (visited >> v & 1) == 0 and mask >> v & 1:
                        tmp = dfs(v)
                        diameter = max(diameter, height + tmp)
                        height = max(height, tmp)
                return height + 1

            # 从当前集合mask中的编号最大的节点开始递归，其实可以从任意一个节点开始
            dfs(mask.bit_length() - 1)
            # 当前集合mask表示的是一棵连通的树
            if visited == mask:
                res[diameter - 1] += 1
        return res


if __name__ == '__main__':
    print(Solution().countSubgraphsForEachDiameter(n=4, edges=[[1, 2], [2, 3], [2, 4]]))
