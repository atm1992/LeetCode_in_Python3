# -*- coding: UTF-8 -*-
"""
title: 课程顺序
现在总共有 numCourses 门课需要选，记为 0 到 numCourses-1。
给定一个数组 prerequisites ，它的每一个元素 prerequisites[i] 表示两门课程之间的先修顺序。 例如 prerequisites[i] = [ai, bi] 表示想要学习课程 ai ，需要先完成课程 bi 。
请根据给出的总课程数  numCourses 和表示先修顺序的 prerequisites 得出一个可行的修课序列。
可能会有多个正确的顺序，只要任意返回一种就可以了。如果不可能完成所有课程，返回一个空数组。


示例 1:
输入: numCourses = 2, prerequisites = [[1,0]]
输出: [0,1]
解释: 总共有 2 门课程。要学习课程 1，你需要先完成课程 0。因此，正确的课程顺序为 [0,1] 。

示例 2:
输入: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
输出: [0,1,2,3] or [0,2,1,3]
解释: 总共有 4 门课程。要学习课程 3，你应该先完成课程 1 和课程 2。并且课程 1 和课程 2 都应该排在课程 0 之后。
 因此，一个正确的课程顺序是 [0,1,2,3] 。另一个正确的排序是 [0,2,1,3] 。

示例 3:
输入: numCourses = 1, prerequisites = []
输出: [0]
解释: 总共 1 门课，直接修第一门课就可。


提示:
1 <= numCourses <= 2000
0 <= prerequisites.length <= numCourses * (numCourses - 1)
prerequisites[i].length == 2
0 <= ai, bi < numCourses
ai != bi
prerequisites 中不存在重复元素
"""
from collections import defaultdict, deque
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """拓扑排序 + BFS"""
        res = []
        # 记录所有的有向边，pre -> [curs]
        edges = defaultdict(list)
        in_degree = [0] * numCourses
        # 计算所有课程(顶点)的入度。然后将所有入度为0的课程(顶点)加入队列，作为BFS的起点
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
        return res if len(res) == numCourses else []

    def findOrder_2(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """拓扑排序 + DFS"""
        res = []
        # 记录所有的有向边，pre -> [curs]
        edges = defaultdict(list)
        for cur, pre in prerequisites:
            edges[pre].append(cur)
        # 记录各个课程(顶点)的当前访问状态。0 - 未搜索过；1 - 搜索中，回溯结束时，将课程(顶点)加入stack；2 - 搜索完成，课程(顶点)已加入stack。
        visited = [0] * numCourses
        # 最终返回stack的逆序。因为是cur节点先加入，当pre指向的所有cur节点都加入stack后，才会将pre节点加入stack
        stack = []
        # 记录是否存在环路
        has_loop = False

        def dfs(u: int) -> None:
            nonlocal has_loop
            # 将当前课程(顶点)的状态更新为 搜索中
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
                    # 只有当当前课程(顶点)的所有后继节点都搜索完成(加入stack)后，当前课程(顶点)才算搜索完成(加入stack)
            visited[u] = 2
            stack.append(u)

        for u in range(numCourses):
            if visited[u] == 0:
                dfs(u)
                if has_loop:
                    break
        # return stack[::-1] if len(stack) == numCourses else []
        return [] if has_loop else stack[::-1]
