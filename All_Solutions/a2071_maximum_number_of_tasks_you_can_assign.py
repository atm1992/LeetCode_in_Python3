# -*- coding: UTF-8 -*-
"""
title: 你可以安排的最多任务数目
You have n tasks and m workers. Each task has a strength requirement stored in a 0-indexed integer array tasks, with the ith task requiring tasks[i] strength to complete. The strength of each worker is stored in a 0-indexed integer array workers, with the jth worker having workers[j] strength. Each worker can only be assigned to a single task and must have a strength greater than or equal to the task's strength requirement (i.e., workers[j] >= tasks[i]).
Additionally, you have pills magical pills that will increase a worker's strength by strength. You can decide which workers receive the magical pills, however, you may only give each worker at most one magical pill.
Given the 0-indexed integer arrays tasks and workers and the integers pills and strength, return the maximum number of tasks that can be completed.


Example 1:
Input: tasks = [3,2,1], workers = [0,3,3], pills = 1, strength = 1
Output: 3
Explanation:
We can assign the magical pill and tasks as follows:
- Give the magical pill to worker 0.
- Assign worker 0 to task 2 (0 + 1 >= 1)
- Assign worker 1 to task 1 (3 >= 2)
- Assign worker 2 to task 0 (3 >= 3)

Example 2:
Input: tasks = [5,4], workers = [0,0,0], pills = 1, strength = 5
Output: 1
Explanation:
We can assign the magical pill and tasks as follows:
- Give the magical pill to worker 0.
- Assign worker 0 to task 0 (0 + 5 >= 5)

Example 3:
Input: tasks = [10,15,30], workers = [0,10,10,10,10], pills = 3, strength = 10
Output: 2
Explanation:
We can assign the magical pills and tasks as follows:
- Give the magical pill to worker 0 and worker 1.
- Assign worker 0 to task 0 (0 + 10 >= 10)
- Assign worker 1 to task 1 (10 + 10 >= 15)
The last pill is not given because it will not make any worker strong enough for the last task.


Constraints:
n == tasks.length
m == workers.length
1 <= n, m <= 5 * 10^4
0 <= pills <= m
0 <= tasks[i], workers[j], strength <= 10^9
"""
from collections import deque
from typing import List


class Solution:
    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        """二分查找 + 贪心check + 双端队列"""
        m, n = len(workers), len(tasks)
        tasks.sort()
        workers.sort()

        def check(num: int) -> bool:
            """
            选择值最小的num个任务和值最大的num个worker进行匹配，若能完成这num个任务，则返回True
            从大到小遍历所有任务，若当前任务可以被值最大的worker完成，则pop值最大的worker；若不能完成，则说明需要使用药片，
            此时选择使用药片后恰好能完成任务的worker
            """
            remain_pills = pills
            # 使用一个双端队列来记录能够完成当前任务的所有worker(包括使用药片)
            cur_usable_workers = deque()
            w_idx = m - 1
            # 从大到小遍历值最小的num个任务
            for i in range(num - 1, -1, -1):
                cur_task = tasks[i]
                while w_idx >= m - num and workers[w_idx] + strength >= cur_task:
                    cur_usable_workers.appendleft(workers[w_idx])
                    w_idx -= 1
                if not cur_usable_workers:
                    return False
                if cur_usable_workers[-1] >= cur_task:
                    cur_usable_workers.pop()
                else:
                    if remain_pills == 0:
                        return False
                    cur_usable_workers.popleft()
                    remain_pills -= 1
            return True

        left, right = 0, min(m, n)
        while left < right:
            mid = (left + right + 1) // 2
            if check(mid):
                left = mid
            else:
                right = mid - 1
        return left


if __name__ == '__main__':
    print(Solution().maxTaskAssign(tasks=[5, 4], workers=[0, 0, 0], pills=1, strength=5))
