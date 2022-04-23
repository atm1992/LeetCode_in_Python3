# -*- coding: UTF-8 -*-
"""
title: 会议室 II
Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], return the minimum number of conference rooms required.


Example 1:
Input: intervals = [[0,30],[5,10],[15,20]]
Output: 2

Example 2:
Input: intervals = [[7,10],[2,4]]
Output: 1


Constraints:
1 <= intervals.length <= 10^4
0 <= starti < endi <= 10^6
"""
from typing import List
import heapq


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        """优先队列"""
        intervals.sort()
        end_heap = []
        heapq.heappush(end_heap, intervals[0][1])
        for interval in intervals[1:]:
            # 若当前会议的开始时间晚于当前最小的会议结束时间，则无需开启新房间。
            # 对应的操作就是先pop最小的会议结束时间，然后push当前会议的结束时间，此时，最小堆的大小并未改变
            if interval[0] >= end_heap[0]:
                heapq.heappop(end_heap)
            # 无论上面有没有pop最小的会议结束时间，都需要将当前会议的结束时间push进去。
            # 区别在于：如果上面pop了，那么最小堆的长度不变，意味着无需开启新房间；若上面没有pop，那么最小堆的长度加1，意味着需要开启新房间。
            heapq.heappush(end_heap, interval[1])
        # 遍历完以后，最小堆的长度即为最终结果。因为在遍历过程中，最小堆的长度要么加1，要么不变，并不会减少，
        # 所以不存在某个房间因会议结束而被移除的情况，只会是用来安排新的会议，房间还保留在最小堆中。
        # 最终最小堆的长度表示的是整个过程中，总共开启过多少个房间，哪怕有些房间在最后时刻已经不在使用了，但它依旧还在最小堆中。
        return len(end_heap)


