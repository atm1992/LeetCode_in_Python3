# -*- coding: UTF-8 -*-
"""
title: 完成所有任务的最少时间
There is a computer that can run an unlimited number of tasks at the same time. You are given a 2D integer array tasks where tasks[i] = [starti, endi, durationi] indicates that the ith task should run for a total of durationi seconds (not necessarily continuous) within the inclusive time range [starti, endi].
You may turn on the computer only when it needs to run a task. You can also turn it off if it is idle.
Return the minimum time during which the computer should be turned on to complete all tasks.


Example 1:
Input: tasks = [[2,3,1],[4,5,1],[1,5,2]]
Output: 2
Explanation:
- The first task can be run in the inclusive time range [2, 2].
- The second task can be run in the inclusive time range [5, 5].
- The third task can be run in the two inclusive time ranges [2, 2] and [5, 5].
The computer will be on for a total of 2 seconds.

Example 2:
Input: tasks = [[1,3,2],[2,5,3],[5,6,2]]
Output: 4
Explanation:
- The first task can be run in the inclusive time range [2, 3].
- The second task can be run in the inclusive time ranges [2, 3] and [5, 5].
- The third task can be run in the two inclusive time range [5, 6].
The computer will be on for a total of 4 seconds.


Constraints:
1 <= tasks.length <= 2000
tasks[i].length == 3
1 <= starti, endi <= 2000
1 <= durationi <= endi - starti + 1
"""
from typing import List


class Solution:
    def findMinimumTime(self, tasks: List[List[int]]) -> int:
        """
        排序 + 贪心 + 枚举。
        先将所有task按end升序
        每个task的执行时间尽量安排在[start, end]的后半段，因为下一个task要么和当前task没有交集，要么包含当前task的后半段，此时可以共享后半段。
        对于每个task的duration，可以将一部分安排在[start, end]的前半段，从而与上一个task共享，不足duration的部分安排到后半段，与下一个task共享。
        """
        tasks.sort(key=lambda task: task[1])
        # 记录[0, max(end)]区间内已使用的时间点
        used = [False] * (tasks[-1][1] + 1)
        for s, e, d in tasks:
            # 先看下当前task的[start, end]内已使用的时间点是否满足duration
            d -= sum(used[s:e + 1])
            # 若不满足，则从end向start添加未使用过的时间点，因为题目保证 1 <= durationi <= endi - starti + 1
            while d > 0:
                if not used[e]:
                    used[e] = True
                    d -= 1
                e -= 1
        return sum(used)

    def findMinimumTime_2(self, tasks: List[List[int]]) -> int:
        """
        排序 + 贪心 + 单调栈 + 前缀和 + 二分查找。
        由于每次都是从右到左添加未使用过的时间点，此过程相当于将右侧的若干个小区间合并为一个大区间，因此可以使用栈来优化
        栈中保存各个区间的左右端点，以及从栈底到栈顶的区间长度之和(前缀和思想)，注意：保存的并不是该区间内的duration
        区间合并前，使用二分查找当前task的start所在的区间或前一个区间(若start不在任一区间内)，因为栈中的区间是互不相交的，
        所以各个区间的左右端点、以及区间长度之和都是单调递增的，因此可以使用二分查找
        找到start所在的区间或前一个区间后，利用前缀和的长度之差便可得到当前task的[start, end]内已使用的时间点
        若还需添加时间点，则从右到左合并小区间
        """
        tasks.sort(key=lambda task: task[1])
        stack = [(-1, -1, 0)]
        for s, e, d in tasks:
            l, r = 0, len(stack) - 1
            while l < r:
                mid = (l + r + 1) // 2
                # 二分查找当前task的start所在的区间或前一个区间
                if stack[mid][0] <= s:
                    l = mid
                else:
                    r = mid - 1
            _, se, sd = stack[l]
            d -= stack[-1][2] - sd
            # 若当前task的start在某个区间内，则还需算上在该区间内已使用的时间点
            if s <= se:
                d -= se - s + 1
            if d <= 0:
                continue
            # 从右到左合并小区间。最终的d = 之前剩余的d + 右侧若干个小区间已使用的时间点
            while e - stack[-1][1] <= d:
                ts, te, _ = stack.pop()
                d += te - ts + 1
            # 将上面右侧的若干个小区间合并为一个大区间。退出上述while循环时，e - d + 1 > stack[-1][1]
            stack.append((e - d + 1, e, stack[-1][2] + d))
        return stack[-1][2]


if __name__ == '__main__':
    print(Solution().findMinimumTime_2(tasks=[[1, 1, 1]]))
