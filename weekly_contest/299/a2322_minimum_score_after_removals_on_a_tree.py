# -*- coding: UTF-8 -*-
"""
title: 从树中删除边的最小分数
There is an undirected connected tree with n nodes labeled from 0 to n - 1 and n - 1 edges.
You are given a 0-indexed integer array nums of length n where nums[i] represents the value of the ith node. You are also given a 2D integer array edges of length n - 1 where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the tree.
Remove two distinct edges of the tree to form three connected components. For a pair of removed edges, the following steps are defined:
    Get the XOR of all the values of the nodes for each of the three components respectively.
    The difference between the largest XOR value and the smallest XOR value is the score of the pair.
        For example, say the three components have the node values: [4,5,7], [1,9], and [3,3,3]. The three XOR values are 4 ^ 5 ^ 7 = 6, 1 ^ 9 = 8, and 3 ^ 3 ^ 3 = 3. The largest XOR value is 8 and the smallest XOR value is 3. The score is then 8 - 3 = 5.
Return the minimum score of any possible pair of edge removals on the given tree.


Example 1:
Input: nums = [1,5,5,4,11], edges = [[0,1],[1,2],[1,3],[3,4]]
Output: 9
Explanation: The diagram above shows a way to make a pair of removals.
- The 1st component has nodes [1,3,4] with values [5,4,11]. Its XOR value is 5 ^ 4 ^ 11 = 10.
- The 2nd component has node [0] with value [1]. Its XOR value is 1 = 1.
- The 3rd component has node [2] with value [5]. Its XOR value is 5 = 5.
The score is the difference between the largest and smallest XOR value which is 10 - 1 = 9.
It can be shown that no other pair of removals will obtain a smaller score than 9.

Example 2:
Input: nums = [5,5,2,4,4,2], edges = [[0,1],[1,2],[5,2],[4,3],[1,3]]
Output: 0
Explanation: The diagram above shows a way to make a pair of removals.
- The 1st component has nodes [3,4] with values [4,4]. Its XOR value is 4 ^ 4 = 0.
- The 2nd component has nodes [1,0] with values [5,5]. Its XOR value is 5 ^ 5 = 0.
- The 3rd component has nodes [2,5] with values [2,2]. Its XOR value is 2 ^ 2 = 0.
The score is the difference between the largest and smallest XOR value which is 0 - 0 = 0.
We cannot obtain a smaller score than 0.


Constraints:
n == nums.length
3 <= n <= 1000
1 <= nums[i] <= 10^8
edges.length == n - 1
edges[i].length == 2
0 <= ai, bi < n
ai != bi
edges represents a valid tree.
"""
from typing import List


class Solution:
    def minimumScore(self, nums: List[int], edges: List[List[int]]) -> int:
        """
        DFS。利用时间戳来快速判断节点之间的祖孙(父子)关系
        DFS过程中，维护一个全局的时间戳timer，每访问一个新节点，timer就加1。使用两个数组in_time、out_time来分别记录进入(递归开始)某个节点的时间戳以及离开(递归结束)某个节点的时间戳。
        时间戳的性质：
        假设现有一棵以a为根节点的树，该子树中存在一个节点b，DFS过程中，必须先递归完以b为根节点的子树，才能结束对以a为根节点的树的递归。
        所以，区间[in_time[b], out_time[b]]必然在区间[in_time[a], out_time[a]]内，即 in_time[a] < in_time[b] && out_time[b] < out_time[a]
        DFS过程中，除了记录in_time、out_time以外，还需用一个数组xor来记录以某个节点为根节点的子树的异或和。
        假设现有一棵以a为根节点的树，待删除的两条边分别为b-c、d-e，删除这两条边后，将会形成3棵树：以a为根节点的树、以c为根节点的树、以e为根节点的树。
        此时可分为3种情况：
        1、若节点c是节点e的祖先节点，则3棵树的异或和分别为：xor[a] ^ xor[c], xor[c] ^ xor[e], xor[e]
        2、若节点e是节点c的祖先节点，则3棵树的异或和分别为：xor[a] ^ xor[e], xor[e] ^ xor[c], xor[c]
        3、若节点c与节点e不存在祖孙关系，则3棵树的异或和分别为：xor[a] ^ xor[c] ^ xor[e], xor[c], xor[e]
        """
        n = len(nums)
        graph = [[] for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        timer = 0
        in_time, out_time, xor = [0] * n, [0] * n, [0] * n

        def dfs(cur: int, father: int) -> None:
            """因为graph中记录的都是无向边，父节点、子节点都在一个数组中，无法区分，但因为每个节点都只有一个父节点，dfs树是从根节点向叶节点访问的，
            所以不需要使用一个visited数组，只需传入一个father变量即可。遍历某个节点的无向边数组之前，只有父节点是被访问过的，其它节点(均为子节点)肯定没被访问过"""
            nonlocal timer
            timer += 1
            in_time[cur] = timer
            xor[cur] = nums[cur]
            for nxt in graph[cur]:
                if nxt == father:
                    continue
                dfs(nxt, cur)
                xor[cur] ^= xor[nxt]
            timer += 1
            out_time[cur] = timer

        # 假设根节点0的父节点为-1
        dfs(0, -1)
        res = float('inf')
        # 枚举其它两棵子树的根节点i、j
        for i in range(1, n - 1):
            for j in range(i + 1, n):
                # i 是 j 的祖先节点
                if in_time[i] < in_time[j] and out_time[j] < out_time[i]:
                    a, b, c = xor[0] ^ xor[i], xor[i] ^ xor[j], xor[j]
                # j 是 i 的祖先节点
                elif in_time[j] < in_time[i] and out_time[i] < out_time[j]:
                    a, b, c = xor[0] ^ xor[j], xor[j] ^ xor[i], xor[i]
                # i 与 j 不存在祖孙关系
                else:
                    a, b, c = xor[0] ^ xor[i] ^ xor[j], xor[i], xor[j]
                res = min(res, max(a, b, c) - min(a, b, c))
                # 不可能存在比0还小的分数
                if res == 0:
                    return 0
        return res


if __name__ == '__main__':
    print(Solution().minimumScore(nums=[1, 5, 5, 4, 11], edges=[[0, 1], [1, 2], [1, 3], [3, 4]]))
