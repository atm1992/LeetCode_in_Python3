# -*- coding: UTF-8 -*-
"""
title: 连接所有点的最小费用
You are given an array points representing integer coordinates of some points on a 2D-plane, where points[i] = [xi, yi].
The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan distance between them: |xi - xj| + |yi - yj|, where |val| denotes the absolute value of val.
Return the minimum cost to make all points connected. All points are connected if there is exactly one simple path between any two points.


Example 1:
Input: points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
Output: 20
Explanation:
We can connect the points as shown above to get the minimum cost of 20.
Notice that there is a unique path between every pair of points.

Example 2:
Input: points = [[3,12],[-2,5],[-4,1]]
Output: 18


Constraints:
1 <= points.length <= 1000
-10^6 <= xi, yi <= 10^6
All pairs (xi, yi) are distinct.

解题思路：
要求得到了一张 n 个节点的完全图，任意两点之间的距离均为它们的曼哈顿距离。假设在这个图中取得一个子图，恰满足子图的任意两点之间有且仅有一条简单路径，且这个子图的所有边的总权值之和尽可能小。
能满足任意两点之间有且仅有一条简单路径的只有树，且这棵树包含 n 个节点。这棵树就叫做给定图的生成树，其中总权值最小的生成树，称为最小生成树。
在一个包含所有顶点的无向图中，查找拥有最小总权值的子图(需包含所有顶点)，这个子图就是最小生成树(Minimum Spanning Tree, MST)。树其实可看作是一个无环连通图。
最小生成树的两个经典算法：Kruskal算法、Prim算法。
1、Kruskal以边为主导，时间主要取决于边数，比较适合于稀疏图(Sparse Graph)，稀疏图通常用邻接表存储；
    - 将所有边按长度从小到大进行排序，依次考虑是否加入到最小生成树中。若加入这个边不会产生环路，则加入进来；否则不能加入。使用并查集来判断是否会产生环路。
2、Prim算法以顶点为主导，与图中边数无关，比较适合于稠密图(Dense Graph)，稠密图通常用邻接矩阵存储。
    - 初始状态下，任选一个顶点加入。之后每一轮，加入一个未加入的顶点，具体方法：计算未加入顶点与所有已加入顶点之间的最小距离，加入最小距离所对应的未加入顶点。
3、Kruskal算法需结合使用并查集；Prim算法需结合使用优先队列(最小堆)。
"""
import heapq
from typing import List


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        """
        最小生成树的经典算法 - Kruskal算法。该算法的基本思想就是从小到大加入边，是一个贪心算法。
        算法流程为：
        1、将图 G = {V, E} 中的所有边按长度从小到大进行排序，等长的边可按任意顺序。
        2、初始化图为 G' = {V, null}，从前向后扫描排序后的边，若扫描到的边e在G'中连接了两个不同的连通分量，则将它插入G'中
            - 使用并查集来维护连通性
            - 图的顶点集合不能为空，但边的集合可以为空
        3、最后得到的图G'就是图G的最小生成树
        """
        n = len(points)
        parent = list(range(n))
        """
        并查集的union过程，有两种优化方式：基于 size 的优化、基于 rank(秩) 的优化。这两种方式二选一
        并查集的find过程，有一种优化方式：路径压缩。对find的优化 与 对union的优化不冲突，可以同时使用。
        无论是对union优化，还是对find进行优化，都是为了加快查找集合根节点的过程，查找集合根节点的时间复杂度为O(h)，h 表示树的高度。
        上面这些优化都是为了减小树的高度，从而加快运行速度，即使不做任何优化，最终结果也不会有什么问题，就是运行速度比较慢而已。
        基于 rank(秩) 的优化 .vs. 基于 size 的优化：
        1、两者都是为了减小树的高度，不过按size合并在有些场景下，并不能使树的高度最小
        2、按rank(秩)合并，可确保合并后，树的高度是最小的。rank(秩) 可理解为以当前节点为根节点的子树的高度
        """
        # 初始时，以每个节点为根节点的子树都只有一层，所以高度均为1
        rank = [1] * n
        # 初始时，每个节点所在的集合树中都只有一个节点
        size = [1] * n

        def find(i: int) -> int:
            if i != parent[i]:
                # 这里就是find的路径压缩，直接将当前节点i的父节点指向集合根节点
                parent[i] = find(parent[i])
            return parent[i]

        def has_not_union_without_optimize(i: int, j: int) -> bool:
            """
            若节点i与节点j已经在同一连通分量中了，则无需再连接了，当前这条边就可以不用了，因此返回False；
            若节点i与节点j之前不在相同连通分量中，则使用当前这条边连接这两个不同的连通分量，执行union操作，然后返回True。
            """
            i_root, j_root = find(i), find(j)
            if i_root == j_root:
                return False
            parent[i_root] = j_root
            return True

        def has_not_union_with_size(i: int, j: int) -> bool:
            """
            若节点i与节点j已经在同一连通分量中了，则无需再连接了，当前这条边就可以不用了，因此返回False；
            若节点i与节点j之前不在相同连通分量中，则使用当前这条边连接这两个不同的连通分量，执行union操作，然后返回True。
            """
            i_root, j_root = find(i), find(j)
            if i_root == j_root:
                return False
            # 将元素少的集合根节点指向元素多的集合根节点，这样大概率能生成一个高度比较低的树。注意：说的是大概率
            if size[i_root] < size[j_root]:
                parent[i_root] = j_root
                size[j_root] += size[i_root]
            else:
                parent[j_root] = i_root
                size[i_root] += size[j_root]
            return True

        def has_not_union_with_rank(i: int, j: int) -> bool:
            """
            若节点i与节点j已经在同一连通分量中了，则无需再连接了，当前这条边就可以不用了，因此返回False；
            若节点i与节点j之前不在相同连通分量中，则使用当前这条边连接这两个不同的连通分量，执行union操作，然后返回True。
            """
            i_root, j_root = find(i), find(j)
            if i_root == j_root:
                return False
            # 将高度小的树合并到高度大的树，从而确保合并后，树的高度最小。
            # 若合并前，两棵树的高度一样，则任意将一棵树a合并到另一棵树b，合并后，树b的高度要加1，树a的高度不变
            if rank[i_root] < rank[j_root]:
                # 因为合并前，j_root的高度至少比i_root的高度大1，所以合并后，并不会对i_root、j_root的高度有任何影响。
                parent[i_root] = j_root
            elif rank[i_root] > rank[j_root]:
                parent[j_root] = i_root
            else:
                parent[i_root] = j_root
                rank[j_root] += 1
            return True

        def get_dist(i: int, j: int) -> int:
            return abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])

        edges = []
        for i in range(n - 1):
            for j in range(i + 1, n):
                edges.append((get_dist(i, j), i, j))
        edges.sort()
        res = 0
        edge_cnt = 0
        for dist, i, j in edges:
            """
            测试结果：
            1、has_not_union_without_optimize，通过72/72测试用例，执行用时：1252 ms
            2、has_not_union_with_size，通过72/72测试用例，执行用时：1308 ms
            3、has_not_union_with_rank，通过72/72测试用例，执行用时：1652 ms
            可能是因为测试数据量太小，看不出优化效果。
            """
            if has_not_union_without_optimize(i, j):
                res += dist
                edge_cnt += 1
                # n个节点的图，只需n-1条边
                if edge_cnt == n - 1:
                    break
        return res

    def minCostConnectPoints_2(self, points: List[List[int]]) -> int:
        """最小生成树的经典算法 - Prim算法"""

        def get_dist(i: int, j: int) -> int:
            return abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])

        n = len(points)
        unvisited = set(range(n))
        # 记录未加入顶点与所有已加入顶点之间的最小距离
        # -10^6 <= xi, yi <= 10^6，顶点之间的最小距离 <= 4 * 10^6。起始顶点设为顶点0，顶点0到自身的距离为0
        min_dists = [0] + [4000001] * (n - 1)
        # (dist, id)
        queue = [(0, 0)]
        res = 0
        while queue:
            dist, i = heapq.heappop(queue)
            if i not in unvisited:
                continue
            unvisited.remove(i)
            res += dist
            for j in unvisited:
                tmp = get_dist(i, j)
                if tmp < min_dists[j]:
                    min_dists[j] = tmp
                    heapq.heappush(queue, (tmp, j))
        return res


if __name__ == '__main__':
    print(Solution().minCostConnectPoints_2(points=[[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]))
