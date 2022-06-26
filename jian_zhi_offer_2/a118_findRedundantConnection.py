# -*- coding: UTF-8 -*-
"""
title: 多余的边
树可以看成是一个连通且 无环 的 无向 图。
给定往一棵 n 个节点 (节点值 1～n) 的树中添加一条边后的图。添加的边的两个顶点包含在 1 到 n 中间，且这条附加的边不属于树中已存在的边。图的信息记录于长度为 n 的二维数组 edges ，edges[i] = [ai, bi] 表示图中在 ai 和 bi 之间存在一条边。
请找出一条可以删去的边，删除后可使得剩余部分是一个有着 n 个节点的树。如果有多个答案，则返回数组 edges 中最后出现的边。


示例 1：
输入: edges = [[1,2],[1,3],[2,3]]
输出: [2,3]

示例 2：
输入: edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
输出: [1,4]


提示:
n == edges.length
3 <= n <= 1000
edges[i].length == 2
1 <= ai < bi <= edges.length
ai != bi
edges 中无重复元素
给定的图是连通的 
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


if __name__ == '__main__':
    print(Solution().findRedundantConnection(edges=[[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]))
