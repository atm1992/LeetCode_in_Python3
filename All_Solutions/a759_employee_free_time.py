# -*- coding: UTF-8 -*-
"""
title: 员工空闲时间
We are given a list schedule of employees, which represents the working time for each employee.
Each employee has a list of non-overlapping Intervals, and these intervals are in sorted order.
Return the list of finite intervals representing common, positive-length free time for all employees, also in sorted order.
(Even though we are representing Intervals in the form [x, y], the objects inside are Intervals, not lists or arrays. For example, schedule[0][0].start = 1, schedule[0][0].end = 2, and schedule[0][0][0] is not defined).  Also, we wouldn't include intervals like [5, 5] in our answer, as they have zero length.


Example 1:
Input: schedule = [[[1,2],[5,6]],[[1,3]],[[4,10]]]
Output: [[3,4]]
Explanation: There are a total of three employees, and all common
free time intervals would be [-inf, 1], [3, 4], [10, inf].
We discard any intervals that contain inf as they aren't finite.

Example 2:
Input: schedule = [[[1,3],[6,7]],[[2,4]],[[2,5],[9,12]]]
Output: [[5,6],[7,9]]


Constraints:
1 <= schedule.length , schedule[i].length <= 50
0 <= schedule[i].start < schedule[i].end <= 10^8
"""
import heapq


# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end


class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        """
        事件(扫描线)
        对于每个区间[s, e]，可看作是两个事件，当time为s时，balance++；当time为e时，balance--。只需统计balance为0的区间
        """
        # 在之后的events升序中，先OPEN再CLOSE。这里设置为-1、1，是为了之后直接使用OPEN/CLOSE的值进行balance++/balance--
        OPEN, CLOSE = -1, 1
        events = []
        for emp in schedule:
            for interval in emp:
                events.append((interval.start, OPEN))
                events.append((interval.end, CLOSE))
        events.sort()
        res = []
        # 0 <= schedule[i].start
        pre, balance = -1, 0
        for cur, status in events:
            if balance == 0 and pre > -1:
                res.append(Interval(pre, cur))
            balance -= status
            pre = cur
        return res

    def employeeFreeTime_2(self, schedule: '[[Interval]]') -> '[Interval]':
        """优先队列"""
        res = []
        # 记录各个员工的第一次工作的开始时间。idx - 员工编号；0 - 第一次工作
        queue = [(emp[0].start, idx, 0) for idx, emp in enumerate(schedule)]
        heapq.heapify(queue)
        # 用于跟踪最新的时间
        anchor = queue[0][0]
        while queue:
            cur, emp_idx, work_idx = heapq.heappop(queue)
            # 若距离最近一次工作的开始时间还有些时间，则这段时间就是空闲的
            if anchor < cur:
                res.append(Interval(anchor, cur))
            anchor = max(anchor, schedule[emp_idx][work_idx].end)
            if work_idx + 1 < len(schedule[emp_idx]):
                heapq.heappush(queue, (schedule[emp_idx][work_idx + 1].start, emp_idx, work_idx + 1))
        return res


if __name__ == '__main__':
    arr = [[[1, 2], [5, 6]], [[1, 3]], [[4, 10]]]
    schedule = []
    for emp in arr:
        tmp = []
        for s, e in emp:
            tmp.append(Interval(s, e))
        schedule.append(tmp)
    res = Solution().employeeFreeTime_2(schedule)
    ans = [f'[{item.start},{item.end}]' for item in res]
    print('[' + ','.join(ans) + ']')
