# -*- coding: UTF-8 -*-
"""
title: 公交路线
You are given an array routes representing bus routes where routes[i] is a bus route that the ith bus repeats forever.
    For example, if routes[0] = [1, 5, 7], this means that the 0th bus travels in the sequence 1 -> 5 -> 7 -> 1 -> 5 -> 7 -> 1 -> ... forever.
You will start at the bus stop source (You are not on any bus initially), and you want to go to the bus stop target. You can travel between bus stops by buses only.
Return the least number of buses you must take to travel from source to target. Return -1 if it is not possible.


Example 1:
Input: routes = [[1,2,7],[3,6,7]], source = 1, target = 6
Output: 2
Explanation: The best strategy is take the first bus to the bus stop 7, then take the second bus to the bus stop 6.

Example 2:
Input: routes = [[7,12],[4,5,15],[6],[15,19],[9,12,13]], source = 15, target = 12
Output: -1


Constraints:
1 <= routes.length <= 500.
1 <= routes[i].length <= 10^5
All the values of routes[i] are unique.
sum(routes[i].length) <= 10^5
0 <= routes[i][j] < 10^6
0 <= source, target < 10^6
"""
from collections import defaultdict, deque
from typing import List


class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        """BFS。超时，通过44/45个测试用例"""
        if source == target:
            return 0
        graph = defaultdict(set)
        for route in routes:
            for stop in route:
                graph[stop].update(route)
                graph[stop].remove(stop)
        res = 0
        queue = deque([source])
        visited = {source}
        while queue:
            res += 1
            for _ in range(len(queue)):
                for nxt in graph[queue.popleft()]:
                    if nxt in visited:
                        continue
                    if nxt == target:
                        return res
                    queue.append(nxt)
                    visited.add(nxt)
        return -1

    def numBusesToDestination_2(self, routes: List[List[int]], source: int, target: int) -> int:
        """优化建图 + BFS。车站(stop)数量远多于公交路线(bus)数量，所以不要记录车站与车站之间的关系。"""
        if source == target:
            return 0
        n = len(routes)
        # stop ——> [buses]
        graph = defaultdict(list)
        # 记录从source车站到乘上某个bus所需的最少上车次数，上车次数就等价于题目问的乘坐的公交车数量。如果某个bus会经过source车站，则上车次数为1
        # 也可以起到visited的作用
        dist = [-1] * n
        queue = deque()
        for i in range(n):
            for stop in routes[i]:
                if stop == source:
                    # 将包含source车站的公交路线(bus)入队
                    queue.append(i)
                    dist[i] = 1
                graph[stop].append(i)
        while queue:
            i = queue.popleft()
            for stop in routes[i]:
                if stop == target:
                    return dist[i]
                for bus in graph[stop]:
                    if dist[bus] == -1:
                        dist[bus] = dist[i] + 1
                        queue.append(bus)
        return -1

    def numBusesToDestination_3(self, routes: List[List[int]], source: int, target: int) -> int:
        """优化建图 + BFS。车站(stop)数量远多于公交路线(bus)数量，所以不要记录车站与车站之间的关系。
        将每条公交路线都看做一个节点，若两条公交路线之间存在换乘车站(相同车站)，则认为这两条公交路线之间存在一条长度为1的边。
        n = len(routes)，图中共有n个节点(n条公交路线)。
        建图方案：遍历所有公交路线，记录每个车站都属于哪些公交路线(一个车站可以对应多条公交路线)。然后再遍历这些公交路线，在这些公交路线(节点)之间连一条边。
        """
        if source == target:
            return 0
        n = len(routes)
        # stop ——> [buses]
        graph = defaultdict(list)
        # bus ——> [buses]
        # edges = defaultdict(list)
        # 稠密图用邻接矩阵，稀疏图用邻接表。本题更可能是稠密图，edges[bus_i][bus_j] == True or False
        edges = [[False] * n for _ in range(n)]
        for i in range(n):
            for stop in routes[i]:
                for j in graph[stop]:
                    edges[i][j] = edges[j][i] = True
                # edges[i][i] = False
                graph[stop].append(i)
        # 记录从source车站到乘上某个bus所需的最少上车次数，上车次数就等价于题目问的乘坐的公交车数量。如果某个bus会经过source车站，则上车次数为1
        # 也可以起到visited的作用
        dist = [-1] * n
        queue = deque()
        for bus in graph[source]:
            dist[bus] = 1
            queue.append(bus)
        while queue:
            i = queue.popleft()
            for j in range(n):
                if edges[i][j] and dist[j] == -1:
                    dist[j] = dist[i] + 1
                    queue.append(j)
        # routes.length <= 500. 顶多把所有公交车都坐一遍，所以最终结果 <= 500
        res = 501
        for bus in graph[target]:
            if dist[bus] != -1:
                res = min(res, dist[bus])
        return -1 if res == 501 else res


if __name__ == '__main__':
    print(Solution().numBusesToDestination_2(routes=[[7, 12], [4, 5, 15], [6], [15, 19], [9, 12, 13]], source=15,
                                             target=12))
