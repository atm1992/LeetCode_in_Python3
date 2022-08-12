# -*- coding: UTF-8 -*-
"""
title: 数据流中的移动平均值
Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.
Implement the MovingAverage class:
    MovingAverage(int size) Initializes the object with the size of the window size.
    double next(int val) Returns the moving average of the last size values of the stream.


Example 1:
Input
["MovingAverage", "next", "next", "next", "next"]
[[3], [1], [10], [3], [5]]
Output
[null, 1.0, 5.5, 4.66667, 6.0]
Explanation
MovingAverage movingAverage = new MovingAverage(3);
movingAverage.next(1); // return 1.0 = 1 / 1
movingAverage.next(10); // return 5.5 = (1 + 10) / 2
movingAverage.next(3); // return 4.66667 = (1 + 10 + 3) / 3
movingAverage.next(5); // return 6.0 = (10 + 3 + 5) / 3


Constraints:
1 <= size <= 1000
-10^5 <= val <= 10^5
At most 104 calls will be made to next.
"""
from collections import deque


class MovingAverage:
    """前缀和 + 双端队列"""

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.size = size
        self.pre_sum = deque([0])
        self.cnt = 0

    def next(self, val: int) -> float:
        self.pre_sum.append(val + self.pre_sum[-1])
        if self.cnt == self.size:
            self.pre_sum.popleft()
        else:
            self.cnt += 1
        return (self.pre_sum[-1] - self.pre_sum[0]) / self.cnt


class MovingAverage2:
    """窗口和 + 双端队列。前缀和可能会溢出"""

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.size = size
        self.queue = deque()
        self.window_sum = 0
        self.cnt = 0

    def next(self, val: int) -> float:
        self.window_sum += val
        self.queue.append(val)
        if self.cnt == self.size:
            self.window_sum -= self.queue.popleft()
        else:
            self.cnt += 1
        return self.window_sum / self.cnt


class MovingAverage3:
    """基于数组的循环队列"""

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.size = size
        self.nums = [0] * size
        self.window_sum = 0
        self.idx = 0
        self.cnt = 0

    def next(self, val: int) -> float:
        self.cnt += 1
        self.idx = (self.idx + 1) % self.size
        self.window_sum += val - self.nums[self.idx]
        self.nums[self.idx] = val
        return self.window_sum / min(self.cnt, self.size)
