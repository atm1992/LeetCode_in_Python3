# -*- coding: UTF-8 -*-
"""
title: 滑动窗口的平均值
给定一个整数数据流和一个窗口大小，根据该滑动窗口的大小，计算滑动窗口里所有数字的平均值。
实现 MovingAverage 类：
    MovingAverage(int size) 用窗口大小 size 初始化对象。
    double next(int val) 成员函数 next 每次调用的时候都会往滑动窗口增加一个整数，请计算并返回数据流中最后 size 个值的移动平均值，即滑动窗口里所有数字的平均值。


示例：
输入：
inputs = ["MovingAverage", "next", "next", "next", "next"]
inputs = [[3], [1], [10], [3], [5]]
输出：
[null, 1.0, 5.5, 4.66667, 6.0]
解释：
MovingAverage movingAverage = new MovingAverage(3);
movingAverage.next(1); // 返回 1.0 = 1 / 1
movingAverage.next(10); // 返回 5.5 = (1 + 10) / 2
movingAverage.next(3); // 返回 4.66667 = (1 + 10 + 3) / 3
movingAverage.next(5); // 返回 6.0 = (10 + 3 + 5) / 3


提示：
1 <= size <= 1000
-10^5 <= val <= 10^5
最多调用 next 方法 10^4 次
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


if __name__ == '__main__':
    obj = MovingAverage2(3)
    print(obj.next(1))
    print(obj.next(10))
    print(obj.next(3))
    print(obj.next(5))
