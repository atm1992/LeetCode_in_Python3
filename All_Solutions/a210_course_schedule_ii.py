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
from collections import defaultdict
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """拓扑排序 + DFS。得到反向拓扑序列"""
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

    def findOrder_2(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """拓扑排序 + BFS。得到正向拓扑序列，推荐此方法"""
        # 记录所有的有向边，pre -> [curs]
        edges = defaultdict(list)
        in_degree = [0] * numCourses
        # 计算所有课程(顶点)的入度。然后将所有入度为0的课程(顶点)加入队列，作为BFS的起点
        for cur, pre in prerequisites:
            edges[pre].append(cur)
            in_degree[cur] += 1
        queue = [i for i in range(numCourses) if in_degree[i] == 0]
        for u in queue:
            for v in edges[u]:
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    queue.append(v)
        # 若存在环路，则环路中的所有顶点都无法将入度降到0，也就不会加入到队列了
        return queue if len(queue) == numCourses else []


if __name__ == '__main__':
    print(Solution().findOrder_2(numCourses=4, prerequisites=[[1, 0], [2, 0], [3, 1], [3, 2]]))
