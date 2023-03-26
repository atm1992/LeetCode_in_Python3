# -*- coding: utf-8 -*-
# @date: 2023/3/25
# @author: liuquan
"""
title: 收集树中金币
There exists an undirected and unrooted tree with n nodes indexed from 0 to n - 1. You are given an integer n and a 2D integer array edges of length n - 1, where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the tree. You are also given an array coins of size n where coins[i] can be either 0 or 1, where 1 indicates the presence of a coin in the vertex i.
Initially, you choose to start at any vertex in the tree. Then, you can perform the following operations any number of times: 
    Collect all the coins that are at a distance of at most 2 from the current vertex, or
    Move to any adjacent vertex in the tree.
Find the minimum number of edges you need to go through to collect all the coins and go back to the initial vertex.
Note that if you pass an edge several times, you need to count it into the answer several times.


Example 1:
Input: coins = [1,0,0,0,0,1], edges = [[0,1],[1,2],[2,3],[3,4],[4,5]]
Output: 2
Explanation: Start at vertex 2, collect the coin at vertex 0, move to vertex 3, collect the coin at vertex 5 then move back to vertex 2.

Example 2:
Input: coins = [0,0,0,1,1,0,0,1], edges = [[0,1],[0,2],[1,3],[1,4],[2,5],[5,6],[5,7]]
Output: 2
Explanation: Start at vertex 0, collect the coins at vertices 4 and 3, move to vertex 2,  collect the coin at vertex 7, then move back to vertex 0.


Constraints:
n == coins.length
1 <= n <= 3 * 10^4
0 <= coins[i] <= 1
edges.length == n - 1
edges[i].length == 2
0 <= ai, bi < n
ai != bi
edges represents a valid tree.
"""
from collections import deque
from typing import List


class Solution:
    def collectTheCoins(self, coins: List[int], edges: List[List[int]]) -> int:
        """
        拓扑排序
        1、先使用拓扑排序删除不含金币的子树，因为这些子树无需访问，之后所有的叶子节点都是有金币的
        2、只需考虑有金币的叶子，因为不在叶子上的金币顺路就能收集到
        3、从有金币的叶子出发，标记节点的层级，设叶子节点的层级为0，则只需在层级为2及以上的节点之间游走就能收集到所有的金币
        起始节点可以选择任意一个层级为2及以上的节点
        """
        n = len(coins)
        graph = [[] for _ in range(n)]
        # 叶子节点的degree为1
        degrees = [0] * n
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
            degrees[a] += 1
            degrees[b] += 1
        queue = deque()
        # 拓扑排序，去掉不含金币的所有子树(剪枝)，直到树上的所有叶子节点都是有金币的
        for i, (d, c) in enumerate(zip(degrees, coins)):
            # 找到所有金币为0的叶子节点
            if d == 1 and c == 0:
                queue.append(i)
        while queue:
            for b in graph[queue.popleft()]:
                degrees[b] -= 1
                if degrees[b] == 1 and coins[b] == 0:
                    queue.append(b)
        # 再次拓扑排序，标记所有节点的层级，叶子节点的层级为0
        for i, (d, c) in enumerate(zip(degrees, coins)):
            # 找到所有金币为1的叶子节点
            if d == 1 and c == 1:
                queue.append(i)
        # 若至多只有一个叶节点有金币，则可以直接收集，无需经过任何边
        if len(queue) <= 1:
            return 0
        levels = [0] * n
        while queue:
            a = queue.popleft()
            for b in graph[a]:
                degrees[b] -= 1
                if degrees[b] == 1:
                    levels[b] = levels[a] + 1
                    queue.append(b)
        # 只需经过所有层级为2及以上的节点之间的边。因为要返回到原点，而且题目给定的是树，因此不存在环，所以需要原路返回，因此乘以2。
        return sum(levels[a] >= 2 and levels[b] >= 2 for a, b in edges) * 2


if __name__ == '__main__':
    print(Solution().collectTheCoins(coins=[1, 0, 0, 0, 0, 1], edges=[[0, 1], [1, 2], [2, 3], [3, 4], [4, 5]]))
