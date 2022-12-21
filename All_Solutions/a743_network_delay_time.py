# -*- coding: UTF-8 -*-
"""
title: 网络延迟时间
You are given a network of n nodes, labeled from 1 to n. You are also given times, a list of travel times as directed edges times[i] = (ui, vi, wi), where ui is the source node, vi is the target node, and wi is the time it takes for a signal to travel from source to target.
We will send a signal from a given node k. Return the minimum time it takes for all the n nodes to receive the signal. If it is impossible for all the n nodes to receive the signal, return -1.


Example 1:
Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
Output: 2

Example 2:
Input: times = [[1,2,1]], n = 2, k = 1
Output: 1

Example 3:
Input: times = [[1,2,1]], n = 2, k = 2
Output: -1


Constraints:
1 <= k <= n <= 100
1 <= times.length <= 6000
times[i].length == 3
1 <= ui, vi <= n
ui != vi
0 <= wi <= 100
All the pairs (ui, vi) are unique. (i.e., no multiple edges.)
"""
import heapq
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        """朴素Dijkstra，适用于稠密图。求出从节点k到其余所有节点的最短路径，其中的最大值就是答案。
        由于本题的边数(6000)远大于顶点数(100)，所以是一张稠密图，因此在运行时间上，朴素Dijkstra要略快于堆优化Dijkstra"""
        # 题目给定的n个节点编号是从1到n，为了对应数组下标(从0开始)，因此将所有的节点编号减1
        # 使用邻接矩阵来存储稠密图，此时边的数量接近于顶点数量的平方
        graph = [[float('inf')] * n for _ in range(n)]
        for u, v, w in times:
            graph[u - 1][v - 1] = w
        # 记录从节点k到其余所有节点的最短路径
        dists = [float('inf')] * n
        dists[k - 1] = 0
        # 将所有节点分为两类：已确定与节点k之间的最短路径长度的节点，即 已确定节点；未确定与节点k之间的最短路径长度的节点，即 未确定节点。
        # used[i]为True，表示节点i为已确定节点
        used = [False] * n
        # 每次循环都确定一个节点，当n个节点都变成了已确定节点，循环结束
        for _ in range(n):
            # 每次都从所有的未确定节点中选择一个与节点k距离最短的节点
            u = -1
            for i, flag in enumerate(used):
                if not flag and (u == -1 or dists[i] < dists[u]):
                    u = i
            used[u] = True
            for v, w in enumerate(graph[u]):
                dists[v] = min(dists[v], dists[u] + w)
        res = max(dists)
        return res if res < float('inf') else -1

    def networkDelayTime_2(self, times: List[List[int]], n: int, k: int) -> int:
        """堆优化Dijkstra，使用优先队列(最小堆)，适用于稀疏图。求出从节点k到其余所有节点的最短路径，其中的最大值就是答案"""
        # 题目给定的n个节点编号是从1到n，为了对应数组下标(从0开始)，因此将所有的节点编号减1
        # 使用邻接表来存储稀疏图，此时边的数量接近于顶点数量
        graph = [[] for _ in range(n)]
        for u, v, w in times:
            graph[u - 1].append((v - 1, w))
        # 记录从节点k到其余所有节点的最短路径
        dists = [float('inf')] * n
        dists[k - 1] = 0
        # (dist, u) 表示从节点k到节点u的路径长度为dist。初始时，从节点k到节点k的路径长度为0
        queue = [(0, k - 1)]
        while queue:
            dist, u = heapq.heappop(queue)
            # 这里的dist只可能大于等于dists[u]，不可能会小于dists[u]
            if dist > dists[u]:
                continue
            for v, w in graph[u]:
                if dist + w < dists[v]:
                    dists[v] = dist + w
                    heapq.heappush(queue, (dist + w, v))
        res = max(dists)
        return res if res < float('inf') else -1


if __name__ == '__main__':
    print(Solution().networkDelayTime(times=[[2, 1, 1], [2, 3, 1], [3, 4, 1]], n=4, k=2))
