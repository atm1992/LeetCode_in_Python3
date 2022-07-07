# -*- coding: UTF-8 -*-
"""
title: 移除最多的同行或同列石头
On a 2D plane, we place n stones at some integer coordinate points. Each coordinate point may have at most one stone.
A stone can be removed if it shares either the same row or the same column as another stone that has not been removed.
Given an array stones of length n where stones[i] = [xi, yi] represents the location of the ith stone, return the largest possible number of stones that can be removed.


Example 1:
Input: stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
Output: 5
Explanation: One way to remove 5 stones is as follows:
1. Remove stone [2,2] because it shares the same row as [2,1].
2. Remove stone [2,1] because it shares the same column as [0,1].
3. Remove stone [1,2] because it shares the same row as [1,0].
4. Remove stone [1,0] because it shares the same column as [0,0].
5. Remove stone [0,1] because it shares the same row as [0,0].
Stone [0,0] cannot be removed since it does not share a row/column with another stone still on the plane.

Example 2:
Input: stones = [[0,0],[0,2],[1,1],[2,0],[2,2]]
Output: 3
Explanation: One way to make 3 moves is as follows:
1. Remove stone [2,2] because it shares the same row as [2,0].
2. Remove stone [2,0] because it shares the same column as [0,0].
3. Remove stone [0,2] because it shares the same row as [0,0].
Stones [0,0] and [1,1] cannot be removed since they do not share a row/column with another stone still on the plane.

Example 3:
Input: stones = [[0,0]]
Output: 0
Explanation: [0,0] is the only stone on the plane, so you cannot remove it.


Constraints:
1 <= stones.length <= 1000
0 <= xi, yi <= 10^4
No two stones are at the same coordinate point.
"""
from collections import defaultdict
from typing import List


class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        """并查集。看看可以把已有的石头划分为多少堆，有多少堆就意味着最终需要留下几块石头"""
        n = len(stones)
        parent = list(range(n))
        # 初始时，以每个节点为根节点的子树都只有一层，所以高度均为1
        rank = [1] * n

        def find(i: int) -> int:
            # 只有根节点的父节点才是本身
            if i != parent[i]:
                parent[i] = find(parent[i])
            return parent[i]

        def union(i: int, j: int) -> None:
            parent[find(i)] = find(j)

        def union_with_rank(i: int, j: int) -> None:
            """基于rank(秩)的优化"""
            i_root, j_root = find(i), find(j)
            if i_root == j_root:
                return
            if rank[i_root] > rank[j_root]:
                parent[j_root] = i_root
            elif rank[i_root] < rank[j_root]:
                parent[i_root] = j_root
            else:
                parent[i_root] = j_root
                rank[j_root] += 1

        for i in range(n - 1):
            for j in range(i + 1, n):
                if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
                    union_with_rank(i, j)
        return n - sum(i == parent[i] for i in range(n))

    def removeStones_2(self, stones: List[List[int]]) -> int:
        """DFS。将给定的二维平面抽象成图，石头看作是顶点，石头间的同行或同列关系看作是边。
        使用DFS计算连通分量(连通块)的个数，有多少个连通分量(连通块)就意味着最终需要留下几块石头"""
        n = len(stones)
        edges = defaultdict(list)
        for i in range(n - 1):
            for j in range(i + 1, n):
                if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
                    edges[i].append(j)
                    edges[j].append(i)

        def dfs(i: int) -> None:
            visited.add(i)
            for j in edges[i]:
                if j not in visited:
                    dfs(j)

        visited = set()
        cnt = 0
        for i in range(n):
            if i not in visited:
                cnt += 1
                dfs(i)
        return n - cnt

    def removeStones_3(self, stones: List[List[int]]) -> int:
        """优化建图 + DFS。极大提升执行速度"""
        n = len(stones)
        # 记录每行或每列分别有哪些石头
        ij2idxs = defaultdict(list)
        for idx, (i, j) in enumerate(stones):
            ij2idxs[i].append(idx)
            # 可将横坐标与纵坐标用同一个哈希表来记录，只需在纵坐标上加10001就可以区分横坐标与纵坐标了，因为0 <= xi, yi <= 10^4
            ij2idxs[j + 10001].append(idx)
        # 若某一行中有k块石头，则只需记录k-1条边，只要能将属于同一个连通分量(连通块)的石头连起来就行。上个方法中记录的边数太多了
        edges = defaultdict(list)
        for idxs in ij2idxs.values():
            for i in range(1, len(idxs)):
                edges[idxs[i - 1]].append(idxs[i])
                edges[idxs[i]].append(idxs[i - 1])

        def dfs(i: int) -> None:
            visited.add(i)
            for j in edges[i]:
                if j not in visited:
                    dfs(j)

        visited = set()
        cnt = 0
        for i in range(n):
            if i not in visited:
                cnt += 1
                dfs(i)
        return n - cnt


if __name__ == '__main__':
    print(Solution().removeStones_3(stones=[[0, 0], [0, 1], [1, 0], [1, 2], [2, 1], [2, 2]]))
