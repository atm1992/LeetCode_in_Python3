# -*- coding: UTF-8 -*-
"""
title: 最小高度树
A tree is an undirected graph in which any two vertices are connected by exactly one path. In other words, any connected graph without simple cycles is a tree.
Given a tree of n nodes labelled from 0 to n - 1, and an array of n - 1 edges where edges[i] = [ai, bi] indicates that there is an undirected edge between the two nodes ai and bi in the tree, you can choose any node of the tree as the root. When you select a node x as the root, the result tree has height h. Among all possible rooted trees, those with minimum height (i.e. min(h))  are called minimum height trees (MHTs).
Return a list of all MHTs' root labels. You can return the answer in any order.
The height of a rooted tree is the number of edges on the longest downward path between the root and a leaf.


Example 1:
Input: n = 4, edges = [[1,0],[1,2],[1,3]]
Output: [1]
Explanation: As shown, the height of the tree is 1 when the root is the node with label 1 which is the only MHT.

Example 2:
Input: n = 6, edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]
Output: [3,4]


Constraints:
1 <= n <= 2 * 10^4
edges.length == n - 1
0 <= ai, bi < n
ai != bi
All the pairs (ai, bi) are distinct.
The given input is guaranteed to be a tree and there will be no repeated edges.

解题思路：
dist[x][y] 表示节点x到节点y的距离，假设树中距离最长的两个节点为 (x,y)，它们之间的距离为max_dist = dist[x][y]，
则可推导出以任意节点为根节点的树，其最小高度一定为 min_height = math.ceil(max_dist / 2)，并且高度最小的树根节点一定在节点x到节点y的路径上。
假设在节点x到节点y的路径上有m个节点：n_0 ——> n_1 ——> …… ——> n_m-1，则最长路径的长度为m-1
1、若m为偶数，则最小高度树的根节点为n_m/2-1或n_m/2，一侧的路径长度为m/2-1，另一侧的路径长度为m/2，因此树的最小高度为m/2;
2、若m为奇数，则最小高度树的根节点为n_(m-1)/2，两侧的路径长度均为(m-1)/2，因此树的最小高度为(m-1)/2。
"""
from collections import deque
from typing import List


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        """
        BFS查找最长路径。
        首先找到距离节点0最远的节点x，再找到距离节点x最远的节点y，节点x与节点y之间的路径就是最长路径，最后找到根节点。
        """
        if n == 1:
            return [0]
        graph = [[] for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        parent = [0] * n

        def bfs(start: int) -> int:
            """查找指定起始节点的最远节点"""
            visited = [False] * n
            visited[start] = True
            queue = deque([start])
            x = start
            while queue:
                x = queue.popleft()
                for y in graph[x]:
                    if visited[y]:
                        continue
                    visited[y] = True
                    parent[y] = x
                    queue.append(y)
            return x

        # 找到距离节点0最远的节点x
        x = bfs(0)
        # 找到距离节点x最远的节点y
        y = bfs(x)
        longest_path = []
        parent[x] = -1
        # 从节点y到节点x之间的最长路径
        while y != -1:
            longest_path.append(y)
            y = parent[y]
        m = len(longest_path)
        return [longest_path[(m - 1) // 2]] if m & 1 else [longest_path[m // 2 - 1], longest_path[m // 2]]

    def findMinHeightTrees_2(self, n: int, edges: List[List[int]]) -> List[int]:
        """
        DFS查找最长路径。
        首先找到距离节点0最远的节点x，再找到距离节点x最远的节点y，节点x与节点y之间的路径就是最长路径，最后找到根节点。
        """
        if n == 1:
            return [0]
        graph = [[] for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        parent = [0] * n
        max_depth, farmost_node = 0, -1

        def dfs(x: int, parent_node: int, depth: int) -> None:
            """查找指定起始节点的最远节点。最终退出dfs时，farmost_node就是距离节点x最远的节点"""
            nonlocal max_depth, farmost_node
            if depth > max_depth:
                max_depth, farmost_node = depth, x
            parent[x] = parent_node
            for y in graph[x]:
                # 因为graph中记录的都是无向边，父节点、子节点都在一个数组中，无法区分，但因为每个节点都只有一个父节点，dfs树是从根节点向叶节点访问的，
                # 所以不需要使用一个visited数组，只需传入一个parent_node变量即可。遍历某个节点的无向边数组之前，只有父节点是被访问过的，其它节点(均为子节点)肯定没被访问过
                if y == parent_node:
                    continue
                dfs(y, x, depth + 1)

        dfs(0, -1, 1)
        max_depth = 0
        # 进入dfs后，会设置 parent[farmost_node] = -1
        dfs(farmost_node, -1, 1)
        longest_path = []
        while farmost_node != -1:
            longest_path.append(farmost_node)
            farmost_node = parent[farmost_node]
        m = len(longest_path)
        return [longest_path[(m - 1) // 2]] if m & 1 else [longest_path[m // 2 - 1], longest_path[m // 2]]

    def findMinHeightTrees_3(self, n: int, edges: List[List[int]]) -> List[int]:
        """拓扑排序。从最外层的叶节点一直往里删，删到剩余节点个数小于等于2，此时剩下的节点就是根节点。"""
        if n == 1:
            return [0]
        graph = [[] for _ in range(n)]
        degree = [0] * n
        for a, b in edges:
            degree[a] += 1
            degree[b] += 1
            graph[a].append(b)
            graph[b].append(a)
        queue = deque([i for i in range(n) if degree[i] == 1])
        # 剩余节点个数
        rest_cnt = n
        while rest_cnt > 2:
            rest_cnt -= len(queue)
            for _ in range(len(queue)):
                x = queue.popleft()
                for y in graph[x]:
                    degree[y] -= 1
                    if degree[y] == 1:
                        queue.append(y)
        return list(queue)


if __name__ == '__main__':
    print(Solution().findMinHeightTrees_3(n=6, edges=[[3, 0], [3, 1], [3, 2], [3, 4], [5, 4]]))
