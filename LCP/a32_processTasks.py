# -*- coding: UTF-8 -*-
"""
title: 批量处理任务
某实验室计算机待处理任务以 [start,end,period] 格式记于二维数组 tasks，表示完成该任务的时间范围为起始时间 start 至结束时间 end 之间，需要计算机投入 period 的时长，注意：
    period 可为不连续时间
    首尾时间均包含在内
处于开机状态的计算机可同时处理任意多个任务，请返回电脑最少开机多久，可处理完所有任务。


示例 1：
输入：tasks = [[1,3,2],[2,5,3],[5,6,2]]
输出：4
解释：
tasks[0] 选择时间点 2、3；
tasks[1] 选择时间点 2、3、5；
tasks[2] 选择时间点 5、6；
因此计算机仅需在时间点 2、3、5、6 四个时刻保持开机即可完成任务。

示例 2：
输入：tasks = [[2,3,1],[5,5,1],[5,6,2]]
输出：3
解释：
tasks[0] 选择时间点 2 或 3；
tasks[1] 选择时间点 5；
tasks[2] 选择时间点 5、6；
因此计算机仅需在时间点 2、5、6 或 3、5、6 三个时刻保持开机即可完成任务。


提示：
2 <= tasks.length <= 10^5
tasks[i].length == 3
0 <= tasks[i][0] <= tasks[i][1] <= 10^9
1 <= tasks[i][2] <= tasks[i][1]-tasks[i][0] + 1
"""
from typing import List


class Solution:
    def processTasks(self, tasks: List[List[int]]) -> int:
        """
        排序 + 贪心 + 单调栈 + 前缀和 + 二分查找。
        本题参考周赛336的2589题的方法二，因为本题的数据量比2589题的大很多，所以2589题的方法一会运行超时
        """
        tasks.sort(key=lambda task: task[1])
        # 因为0 <= tasks[i][0]，所以初始值(哨兵)的右端点不能为-1，若为(-1, -1, 0)，则当第一个task的start为0时，会将初始值(哨兵)进行合并。
        # 需要保证初始值(哨兵)不被合并，即 stack 始终不为空
        stack = [(-2, -2, 0)]
        for s, e, p in tasks:
            l, r = 0, len(stack) - 1
            while l < r:
                mid = (l + r + 1) // 2
                # 二分查找当前task的start所在的区间或前一个区间
                if stack[mid][0] <= s:
                    l = mid
                else:
                    r = mid - 1
            _, se, sp = stack[l]
            p -= stack[-1][2] - sp
            # 若当前task的start在某个区间内，则还需算上在该区间内已使用的时间点
            if s <= se:
                p -= se - s + 1
            if p <= 0:
                continue
            # 从右到左合并小区间。最终的p = 之前剩余的p + 右侧若干个小区间已使用的时间点
            while e - stack[-1][1] <= p:
                ts, te, _ = stack.pop()
                p += te - ts + 1
            # 将上面右侧的若干个小区间合并为一个大区间。退出上述while循环时，e - p > stack[-1][1]，即 e - p + 1 > stack[-1][1]
            stack.append((e - p + 1, e, stack[-1][2] + p))
        return stack[-1][2]


if __name__ == '__main__':
    print(Solution().processTasks(tasks=[[0, 0, 1]]))
