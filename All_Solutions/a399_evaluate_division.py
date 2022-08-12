# -*- coding: UTF-8 -*-
"""
title: 除法求值
You are given an array of variable pairs equations and an array of real numbers values, where equations[i] = [Ai, Bi] and values[i] represent the equation Ai / Bi = values[i]. Each Ai or Bi is a string that represents a single variable.
You are also given some queries, where queries[j] = [Cj, Dj] represents the jth query where you must find the answer for Cj / Dj = ?.
Return the answers to all queries. If a single answer cannot be determined, return -1.0.
Note: The input is always valid. You may assume that evaluating the queries will not result in division by zero and that there is no contradiction.


Example 1:
Input: equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
Output: [6.00000,0.50000,-1.00000,1.00000,-1.00000]
Explanation:
Given: a / b = 2.0, b / c = 3.0
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ?
return: [6.0, 0.5, -1.0, 1.0, -1.0 ]

Example 2:
Input: equations = [["a","b"],["b","c"],["bc","cd"]], values = [1.5,2.5,5.0], queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
Output: [3.75000,0.40000,5.00000,0.20000]

Example 3:
Input: equations = [["a","b"]], values = [0.5], queries = [["a","b"],["b","a"],["a","c"],["x","y"]]
Output: [0.50000,2.00000,-1.00000,-1.00000]


Constraints:
1 <= equations.length <= 20
equations[i].length == 2
1 <= Ai.length, Bi.length <= 5
values.length == equations.length
0.0 < values[i] <= 20.0
1 <= queries.length <= 20
queries[i].length == 2
1 <= Cj.length, Dj.length <= 5
Ai, Bi, Cj, Dj consist of lower case English letters and digits.
"""
from collections import defaultdict
from typing import List, Set, DefaultDict


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        """DFS"""
        graph = defaultdict(DefaultDict[str, float])
        for (a, b), v in zip(equations, values):
            graph[a][b] = v
            graph[b][a] = 1.0 / v

        def dfs(a: str, b: str, visited: Set[str]) -> float:
            if a in visited:
                return -1.0
            if b in graph[a]:
                return graph[a][b]
            visited.add(a)
            for div, v in graph[a].items():
                # a / b = (a / div) * (div / b) = v * tmp
                tmp = dfs(div, b, visited)
                # 0.0 < values[i]，只有当存在无法确定的答案时，才会返回 -1.0
                if tmp != -1.0:
                    return v * tmp
            return -1.0

        res = []
        for a, b in queries:
            if a not in graph or b not in graph:
                res.append(-1.0)
            elif a == b:
                res.append(1.0)
            else:
                res.append(dfs(a, b, set()))
        return res

    def calcEquation_2(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        """Floyd 算法。适用于大量查询的情况，避免每次查询都要搜索一次，预先处理好所有结果，之后直接读取即可"""
        node_cnt = 0
        node2id = {}
        # 给每个node分配一个唯一的id
        for a, b in equations:
            if a not in node2id:
                node2id[a] = node_cnt
                node_cnt += 1
            if b not in node2id:
                node2id[b] = node_cnt
                node_cnt += 1
        # 1 <= equations.length <= 20，最多40个节点
        graph = [[-1.0] * node_cnt for _ in range(node_cnt)]
        # 填表
        for (a, b), v in zip(equations, values):
            a_id, b_id = node2id[a], node2id[b]
            graph[a_id][b_id] = v
            graph[b_id][a_id] = 1.0 / v
        # 拓展结果。注意：这里的顺序不能写成 i、j、k，必须先遍历k，i、j的顺序无所谓
        for k in range(node_cnt):
            for i in range(node_cnt):
                for j in range(node_cnt):
                    # 0.0 < values[i]
                    if graph[i][k] > 0 and graph[k][j] > 0:
                        # 当 i == j 时，graph[i][j] 会被填为 1.0，因为 graph[i][k] = v，graph[k][j] = graph[k][i] = 1.0 / v
                        graph[i][j] = graph[i][k] * graph[k][j]
        res = []
        for a, b in queries:
            if a not in node2id or b not in node2id:
                res.append(-1.0)
            else:
                res.append(graph[node2id[a]][node2id[b]])
        return res

    def calcEquation_3(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        """带权并查集。并查集 —— 支持合并(union)与查询(find)操作的集合(set)，是一种树型的数据结构，常以森林来表示。"""
        node_cnt = 0
        node2id = {}
        # 给每个node分配一个唯一的id
        for a, b in equations:
            if a not in node2id:
                node2id[a] = node_cnt
                node_cnt += 1
            if b not in node2id:
                node2id[b] = node_cnt
                node_cnt += 1
        # 初始时，认为各个节点的父节点(根节点)为本身。通常命名为 father or parent
        father = list(range(node_cnt))
        # 因为初始时认为各个节点的父节点(根节点)为本身，所以各个节点到根节点(本身)的权重均为 1.0
        weight = [1.0] * node_cnt

        def union(a_id: int, b_id: int, v: float) -> None:
            """若a_id、b_id之前不在同一棵树(同一个集合)中，则会将两棵树(两个集合)进行合并。合并后，a_root指向b_root"""
            a_root = find_father(a_id)
            b_root = find_father(b_id)
            if a_root == b_root:
                return
            # 将a_root指向b_root
            father[a_root] = b_root
            # weight[a_root] 表示a_root到b_root的权重。
            # v 为a_id到b_id的权重，weight[b_id] 为b_id到b_root的权重，weight[a_id] 为a_id到a_root的权重
            # a_id -> a_root -> b_root 的权重 == a_id -> b_id -> b_root 的权重
            weight[a_root] = v * weight[b_id] / weight[a_id]

        def find_father(node_id: int) -> int:
            """查找输入节点的根节点编号。在查找过程中，会进行路径压缩。查找结束后，输入节点将会直接指向根节点，并会更新相应的权重"""
            # 只有根节点的父节点才为本身
            if node_id != father[node_id]:
                # 逐步向上查找，直到找到根节点
                root = find_father(father[node_id])
                # 在查找的同时，更新当前节点的权重
                weight[node_id] *= weight[father[node_id]]
                # 将当前节点的父节点更新为根节点
                father[node_id] = root
            return father[node_id]

        for (a, b), v in zip(equations, values):
            # a, b 两个节点若不在同一个集合，则会进行集合合并
            union(node2id[a], node2id[b], v)

        res = []
        for a, b in queries:
            if a not in node2id or b not in node2id:
                res.append(-1.0)
            else:
                a_id, b_id = node2id[a], node2id[b]
                # 若这两个节点最终指向同一个根节点，则说明它们在同一个集合中
                if find_father(a_id) == find_father(b_id):
                    # weight[a_id] 表示节点a到最终根节点的权重；weight[b_id] 表示节点b到最终根节点的权重
                    res.append(weight[a_id] / weight[b_id])
                else:
                    res.append(-1.0)
        return res


if __name__ == '__main__':
    print(Solution().calcEquation_3(equations=[["a", "b"], ["b", "c"]], values=[2.0, 3.0],
                                    queries=[["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]))
