# -*- coding: UTF-8 -*-
"""
title: 课程表
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.
    For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.


Example 1:
Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take.
To take course 1 you should have finished course 0. So it is possible.

Example 2:
Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take.
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.


Constraints:
1 <= numCourses <= 10^5
0 <= prerequisites.length <= 5000
prerequisites[i].length == 2
0 <= ai, bi < numCourses
All the pairs prerequisites[i] are unique.
"""
from collections import defaultdict, deque
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """使用深度优先搜索进行拓扑排序。
        构建一个有向图，然后判断该图是否存在拓扑排序，也就是判断该图是不是一个有向无环图"""
        edges = defaultdict(list)
        # 三种状态：
        # 0 - 未搜索过，还没有搜索到这个节点；
        # 1 - 搜索中，搜索过这个节点，但还没有回溯到该节点，即 该节点还没入栈，因为还有相邻的节点没有搜索完成；
        # 2 - 已搜索完成，搜索过并回溯过这个节点，即 该节点已入栈，并且该节点的所有相邻节点都已出现在栈的更底部位置，满足拓扑排序的要求。
        # cur 要求在pre之前入栈
        visited = [0] * numCourses
        # 存储拓扑排序结果，排序结果会有多个，这里只存储一种即可。因为此题不需要返回拓扑排序结果，所以其实可以去掉stack这个变量
        stack = []
        valid = True

        for cur, pre in prerequisites:
            edges[pre].append(cur)

        def dfs(u: int):
            nonlocal valid
            visited[u] = 1
            for v in edges[u]:
                if visited[v] == 0:
                    dfs(v)
                    # 剪枝
                    if not valid:
                        return
                elif visited[v] == 1:
                    # u想要v在它之前入栈，而v却也想要u在它之前入栈，从而形成了一个回路
                    valid = False
                    return
            # u 的所有后置课程入栈后，u才入栈
            visited[u] = 2
            stack.append(u)

        for i in range(numCourses):
            if not valid:
                break
            if visited[i] == 0:
                dfs(i)
        return valid

    def canFinish_2(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """方法一的深度优先搜索是一种逆向思维：最先被放入栈中的节点是在拓扑排序中最后面的节点。
        其实也可使用正向思维，顺序地生成拓扑排序，这种方法也更加直观"""
        edges = defaultdict(list)
        # 统计每个节点的入度，入度为0的节点才可加入队列
        in_degree = [0] * numCourses
        for cur, pre in prerequisites:
            edges[pre].append(cur)
            in_degree[cur] += 1
        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
        # 因为只需判断是否存在一种拓扑排序，因此可以省去存放答案数组，而只用一个变量来记录被放入答案数组的节点个数，最后判断visited与numCourses是否相等
        visited = 0
        while queue:
            u = queue.popleft()
            visited += 1
            for v in edges[u]:
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    queue.append(v)
        return visited == numCourses


if __name__ == '__main__':
    print(Solution().canFinish_2(numCourses=2, prerequisites=[[1, 0]]))
