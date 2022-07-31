# -*- coding: UTF-8 -*-
"""
title: 查找集群内的「关键连接」
There are n servers numbered from 0 to n - 1 connected by undirected server-to-server connections forming a network where connections[i] = [ai, bi] represents a connection between servers ai and bi. Any server can reach other servers directly or indirectly through the network.
A critical connection is a connection that, if removed, will make some servers unable to reach some other server.
Return all critical connections in the network in any order.


Example 1:
Input: n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]
Output: [[1,3]]
Explanation: [[3,1]] is also accepted.

Example 2:
Input: n = 2, connections = [[0,1]]
Output: [[0,1]]


Constraints:
2 <= n <= 10^5
n - 1 <= connections.length <= 10^5
0 <= ai, bi <= n - 1
ai != bi
There are no repeated connections.
"""
from collections import defaultdict
from typing import List


class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        """
        Tarjan算法 求解无向图的桥。Tarjan算法是基于DFS的算法，用于求解图的连通性问题。Tarjan算法可在线性时间内求出无向图的割点与桥，
        进一步可以求解无向图的双连通分量；还可求解有向图的强连通分量、必经点与必经边。
        无向图的割点：若从无向图中删除节点 x 以及所有与 x 关联的边之后，无向图被分成两个或两个以上的不相连的子图，则称节点 x 为无向图的割点。
        无向图的桥：若从无向图中删除边 e 之后，无向图被分成两个不相连的子图，则称边 e 为无向图的桥或割边。
        无向图中的边要么在环上，要么在链上，在环上的所有边都不是关键连接，在链上的所有边都是关键连接。所以可以忽略掉环上的所有边，即 将环上的所有点合并成一个点。
        时间戳：DFS访问每个节点时，都会给当前被访问节点分配一个时间戳，从0开始，-1表示该节点未被访问过。
        追溯值：从当前节点出发，能够访问到的所有节点中，时间戳最小的值。如果当前节点在环上，则当前节点所在环中的所有节点都会被更新为这个最小的时间戳(追溯值)。
        如果一个节点的追溯值等于初次访问时分配的时间戳，就表示从这个节点出发的所有子节点，都没办法走到该节点的父节点，说明该节点的父节点 与 该节点之间的边是关键连接；
        如果一个节点的追溯值不等于初次访问时分配的时间戳，就表示从这个节点出发的子节点中，可以从该节点的父节点走回该节点，说明该节点的父节点 与 该节点之间的边在一个环中。
        """

        def dfs(cur, cur_time, parent) -> int:
            """
            验证当前节点cur的追溯值是否等于初次访问时parent分配的时间戳cur_time，最后返回当前节点cur的追溯值。
            :param cur: 当前节点的编号，0 ~ n-1，初始值为0，表示根节点
            :param cur_time: 初次访问当前节点时分配的时间戳，初始值为0
            :param parent: 当前节点的父节点的编号，初始值为-1，表示根节点的父节点
            :return: 当前节点cur的追溯值
            """
            visit_time[cur] = cur_time
            for nxt in graph[cur]:
                if nxt == parent:
                    continue
                # 子节点已被访问过，则说明[cur, nxt]在一个环中
                elif visit_time[nxt] != -1:
                    # 注意：这里不能直接写cur_time，因为在整个for循环中，visit_time[cur]有可能已被更新过，而不再是初始的cur_time
                    visit_time[cur] = min(visit_time[cur], visit_time[nxt])
                # 子节点暂时未被访问过
                else:
                    # 先计算子节点的追溯值，再更新当前节点的追溯值
                    visit_time[cur] = min(visit_time[cur], dfs(nxt, cur_time + 1, cur))
            # 需要排除初始根节点0，它肯定满足visit_time[cur] == cur_time，因为值都为0。但是初始根节点的父节点为-1，是我们虚拟出来的一个节点。
            # 初始根节点有可能是关键连接中的一个节点，当访问到它的某个子节点时，会把这个子节点与它之间的关键连接加入到res
            if visit_time[cur] == cur_time and cur != 0:
                res.append([parent, cur])
            return visit_time[cur]

        graph = defaultdict(list)
        for a, b in connections:
            graph[a].append(b)
            graph[b].append(a)
        # 初始时，所有节点都没被访问过，所以访问时间戳均为-1
        visit_time = [-1] * n
        res = []
        dfs(0, 0, -1)
        return res


if __name__ == '__main__':
    print(Solution().criticalConnections(n=4, connections=[[0, 1], [1, 2], [2, 0], [1, 3]]))
