# -*- coding: utf-8 -*-
# @date: 2023/5/1
# @author: liuquan
"""
title: 通知所有员工所需的时间
A company has n employees with a unique ID for each employee from 0 to n - 1. The head of the company is the one with headID.
Each employee has one direct manager given in the manager array where manager[i] is the direct manager of the i-th employee, manager[headID] = -1. Also, it is guaranteed that the subordination relationships have a tree structure.
The head of the company wants to inform all the company employees of an urgent piece of news. He will inform his direct subordinates, and they will inform their subordinates, and so on until all employees know about the urgent news.
The i-th employee needs informTime[i] minutes to inform all of his direct subordinates (i.e., After informTime[i] minutes, all his direct subordinates can start spreading the news).
Return the number of minutes needed to inform all the employees about the urgent news.


Example 1:
Input: n = 1, headID = 0, manager = [-1], informTime = [0]
Output: 0
Explanation: The head of the company is the only employee in the company.

Example 2:
Input: n = 6, headID = 2, manager = [2,2,-1,2,2,2], informTime = [0,0,1,0,0,0]
Output: 1
Explanation: The head of the company with id = 2 is the direct manager of all the employees in the company and needs 1 minute to inform them all.
The tree structure of the employees in the company is shown.


Constraints:
1 <= n <= 10^5
0 <= headID < n
manager.length == n
0 <= manager[i] < n
manager[headID] == -1
informTime.length == n
0 <= informTime[i] <= 1000
informTime[i] == 0 if employee i has no subordinates.
It is guaranteed that all the employees can be informed.
"""
from collections import defaultdict
from functools import lru_cache
from typing import List


class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        """建图 + DFS。寻找从根节点到叶节点的最长路径，自顶向下"""
        graph = defaultdict(list)
        for e, m in enumerate(manager):
            if e != headID:
                graph[m].append(e)

        def dfs(cur_id: int) -> int:
            if cur_id not in graph:
                return 0
            return max(dfs(nxt_id) for nxt_id in graph[cur_id]) + informTime[cur_id]

        return dfs(headID)

    def numOfMinutes_2(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        """记忆化搜索。自底向上"""

        @lru_cache(maxsize=n)
        def dfs(cur_id: int) -> int:
            """计算从cur_id到headID的路径长度"""
            if cur_id == headID:
                return 0
            return dfs(manager[cur_id]) + informTime[manager[cur_id]]

        return max(dfs(cur_id) for cur_id in range(n))


if __name__ == '__main__':
    print(Solution().numOfMinutes(n=6, headID=2, manager=[2, 2, -1, 2, 2, 2], informTime=[0, 0, 1, 0, 0, 0]))
