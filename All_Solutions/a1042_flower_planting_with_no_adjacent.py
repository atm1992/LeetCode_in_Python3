# -*- coding: UTF-8 -*-
"""
title: 不邻接植花
You have n gardens, labeled from 1 to n, and an array paths where paths[i] = [xi, yi] describes a bidirectional path between garden xi to garden yi. In each garden, you want to plant one of 4 types of flowers.
All gardens have at most 3 paths coming into or leaving it.
Your task is to choose a flower type for each garden such that, for any two gardens connected by a path, they have different types of flowers.
Return any such a choice as an array answer, where answer[i] is the type of flower planted in the (i+1)th garden. The flower types are denoted 1, 2, 3, or 4. It is guaranteed an answer exists.


Example 1:
Input: n = 3, paths = [[1,2],[2,3],[3,1]]
Output: [1,2,3]
Explanation:
Gardens 1 and 2 have different types.
Gardens 2 and 3 have different types.
Gardens 3 and 1 have different types.
Hence, [1,2,3] is a valid answer. Other valid answers include [1,2,4], [1,4,2], and [3,2,1].

Example 2:
Input: n = 4, paths = [[1,2],[3,4]]
Output: [1,2,1,2]

Example 3:
Input: n = 4, paths = [[1,2],[2,3],[3,4],[4,1],[1,3],[2,4]]
Output: [1,2,3,4]


Constraints:
1 <= n <= 10^4
0 <= paths.length <= 2 * 10^4
paths[i].length == 2
1 <= xi, yi <= n
xi != yi
Every garden has at most 3 paths coming into or leaving it.
"""
from collections import defaultdict
from typing import List


class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        """贪心。因为所有花园最多有 3 条路径可以进入或离开，也就意味着每个花园最多只有3个相邻花园，但有4种花可以选择。
        所以对于任一花园，只需从相邻花园没种过的花中任选一种即可，它的选择并不会对它的非相邻花园有任何影响，所以之后也不会出现矛盾点，因此不需要回溯"""
        edges = defaultdict(list)
        for u, v in paths:
            edges[u].append(v)
            edges[v].append(u)
        all_options = {1, 2, 3, 4}
        res = [0] * n
        for u in range(1, n + 1):
            options = all_options - set(res[v - 1] for v in edges[u])
            # 从相邻花园没种过的花中任选一种
            res[u - 1] = options.pop()
        return res
