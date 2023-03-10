# -*- coding: UTF-8 -*-
"""
title: 统计可能的树根数目
Alice has an undirected tree with n nodes labeled from 0 to n - 1. The tree is represented as a 2D integer array edges of length n - 1 where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the tree.
Alice wants Bob to find the root of the tree. She allows Bob to make several guesses about her tree. In one guess, he does the following:
    Chooses two distinct integers u and v such that there exists an edge [u, v] in the tree.
    He tells Alice that u is the parent of v in the tree.
Bob's guesses are represented by a 2D integer array guesses where guesses[j] = [uj, vj] indicates Bob guessed uj to be the parent of vj.
Alice being lazy, does not reply to each of Bob's guesses, but just says that at least k of his guesses are true.
Given the 2D integer arrays edges, guesses and the integer k, return the number of possible nodes that can be the root of Alice's tree. If there is no such tree, return 0.


Example 1:
Input: edges = [[0,1],[1,2],[1,3],[4,2]], guesses = [[1,3],[0,1],[1,0],[2,4]], k = 3
Output: 3
Explanation:
Root = 0, correct guesses = [1,3], [0,1], [2,4]
Root = 1, correct guesses = [1,3], [1,0], [2,4]
Root = 2, correct guesses = [1,3], [1,0], [2,4]
Root = 3, correct guesses = [1,0], [2,4]
Root = 4, correct guesses = [1,3], [1,0]
Considering 0, 1, or 2 as root node leads to 3 correct guesses.

Example 2:
Input: edges = [[0,1],[1,2],[2,3],[3,4]], guesses = [[1,0],[3,4],[2,1],[3,2]], k = 1
Output: 5
Explanation:
Root = 0, correct guesses = [3,4]
Root = 1, correct guesses = [1,0], [3,4]
Root = 2, correct guesses = [1,0], [2,1], [3,4]
Root = 3, correct guesses = [1,0], [2,1], [3,2], [3,4]
Root = 4, correct guesses = [1,0], [2,1], [3,2]
Considering any node as root will give at least 1 correct guess.


Constraints:
edges.length == n - 1
2 <= n <= 10^5
1 <= guesses.length <= 10^5
0 <= ai, bi, uj, vj <= n - 1
ai != bi
uj != vj
edges represents a valid tree.
guesses[j] is an edge of the tree.
guesses is unique.
0 <= k <= guesses.length
"""
from collections import defaultdict
from typing import List


class Solution:
    def rootCount(self, edges: List[List[int]], guesses: List[List[int]], k: int) -> int:
        """
        换根DP(树形DP)。动态规划 + 两个DFS
        若节点u和节点v之间有边，则以节点u为根的树转换为以节点v为根节点的树，只有[u, v]和[v, u]这两个guess的正确性变了，其余guess的正确性不变
        """
        g_set = {(u, v) for u, v in guesses}
        p2cs = defaultdict(list)
        for u, v in edges:
            p2cs[u].append(v)
            p2cs[v].append(u)

        def dfs(cur: int, parent: int) -> None:
            nonlocal cnt_0
            for nxt in p2cs[cur]:
                if nxt != parent:
                    cnt_0 += (cur, nxt) in g_set
                    dfs(nxt, cur)

        # 通过DFS构建以节点0为根的树，构建过程中，统计猜对的边数cnt_0
        res, cnt_0 = 0, 0
        dfs(0, -1)

        def reroot(cur: int, parent: int, cnt: int) -> None:
            nonlocal res
            res += cnt >= k
            for nxt in p2cs[cur]:
                if nxt != parent:
                    reroot(nxt, cur, cnt - ((cur, nxt) in g_set) + ((nxt, cur) in g_set))

        reroot(0, -1, cnt_0)
        return res


if __name__ == '__main__':
    print(Solution().rootCount(edges=[[0, 1], [1, 2], [1, 3], [4, 2]], guesses=[[1, 3], [0, 1], [1, 0], [2, 4]], k=3))
