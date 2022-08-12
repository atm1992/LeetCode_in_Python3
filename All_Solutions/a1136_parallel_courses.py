# -*- coding: UTF-8 -*-
"""
title: 并行课程
You are given an integer n, which indicates that there are n courses labeled from 1 to n. You are also given an array relations where relations[i] = [prevCoursei, nextCoursei], representing a prerequisite relationship between course prevCoursei and course nextCoursei: course prevCoursei has to be taken before course nextCoursei.
In one semester, you can take any number of courses as long as you have taken all the prerequisites in the previous semester for the courses you are taking.
Return the minimum number of semesters needed to take all courses. If there is no way to take all the courses, return -1.


Example 1:
Input: n = 3, relations = [[1,3],[2,3]]
Output: 2
Explanation: The figure above represents the given graph.
In the first semester, you can take courses 1 and 2.
In the second semester, you can take course 3.

Example 2:
Input: n = 3, relations = [[1,2],[2,3],[3,1]]
Output: -1
Explanation: No course can be studied because they are prerequisites of each other.


Constraints:
1 <= n <= 5000
1 <= relations.length <= 5000
relations[i].length == 2
1 <= prevCoursei, nextCoursei <= n
prevCoursei != nextCoursei
All the pairs [prevCoursei, nextCoursei] are unique.
"""
from collections import defaultdict, deque
from typing import List


class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        """拓扑排序 + BFS"""
        graph = defaultdict(list)
        in_degree = [0] * (n + 1)
        for pre, nxt in relations:
            graph[pre].append(nxt)
            in_degree[nxt] += 1
        queue = deque([i for i in range(1, n + 1) if in_degree[i] == 0])
        res = 0
        while queue:
            res += 1
            for _ in range(len(queue)):
                cur = queue.popleft()
                for nxt in graph[cur]:
                    in_degree[nxt] -= 1
                    if in_degree[nxt] == 0:
                        queue.append(nxt)
        return res if sum(in_degree) == 0 else -1


if __name__ == '__main__':
    print(Solution().minimumSemesters(n=3, relations=[[1, 3], [2, 3]]))
