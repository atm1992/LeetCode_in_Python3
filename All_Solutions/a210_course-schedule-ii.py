# -*- coding: UTF-8 -*-
"""
title: 课程表 II
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.
    For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.


Example 1:
Input: numCourses = 2, prerequisites = [[1,0]]
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1].

Example 2:
Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
Output: [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].

Example 3:
Input: numCourses = 1, prerequisites = []
Output: [0]


Constraints:
1 <= numCourses <= 2000
0 <= prerequisites.length <= numCourses * (numCourses - 1)
prerequisites[i].length == 2
0 <= ai, bi < numCourses
ai != bi
All the pairs [ai, bi] are distinct.
"""
from collections import defaultdict, deque
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """拓扑排序。广度优先遍历"""
        res = []
        # 记录所有有向边，pre -> [curs]
        edges = defaultdict(list)
        # 统计各个节点的入度。只有入度为0的节点，才可加入queue
        in_degree = [0] * numCourses
        for cur, pre in prerequisites:
            edges[pre].append(cur)
            in_degree[cur] += 1
        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
        while queue:
            u = queue.popleft()
            res.append(u)
            for v in edges[u]:
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    queue.append(v)
        return [] if len(res) < numCourses else res

    def findOrder_2(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """拓扑排序。深度优先遍历"""
        res = []
        # 记录所有有向边，pre -> [curs]
        edges = defaultdict(list)
        # 记录每个节点的状态。0 - 未搜索；1 - 搜索中，等待回溯时加入stack；2 - 搜索完成，该节点已加入stack。
        visited = [0] * numCourses
        # 最终返回结果为stack的逆序。cur节点先加入，所有cur节点都加入后，再加入pre节点
        stack = []
        # 标识有向图中是否存在环路
        has_loop = False
        for cur, pre in prerequisites:
            edges[pre].append(cur)

        def dfs(u: int) -> None:
            nonlocal has_loop
            # 将当前节点标记为 搜索中
            visited[u] = 1
            for v in edges[u]:
                if visited[v] == 0:
                    dfs(v)
                    # 剪枝。一旦发现存在环路，立刻停止搜索
                    if has_loop:
                        return
                elif visited[v] == 1:
                    has_loop = True
                    return
            # 该节点的所有后继节点都搜索完成后，再将当前节点加入stack
            visited[u] = 2
            stack.append(u)

        for u in range(numCourses):
            if has_loop:
                break
            if visited[u] == 0:
                dfs(u)
        return [] if has_loop else stack[::-1]


if __name__ == '__main__':
    print(Solution().findOrder_2(numCourses=4, prerequisites=[[1, 0], [2, 0], [3, 1], [3, 2]]))
