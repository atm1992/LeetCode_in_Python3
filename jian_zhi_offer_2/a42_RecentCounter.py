# -*- coding: UTF-8 -*-
"""
title: 最近请求次数
写一个 RecentCounter 类来计算特定时间范围内最近的请求。
请实现 RecentCounter 类：
    RecentCounter() 初始化计数器，请求数为 0 。
    int ping(int t) 在时间 t 添加一个新请求，其中 t 表示以毫秒为单位的某个时间，并返回过去 3000 毫秒内发生的所有请求数（包括新请求）。确切地说，返回在 [t-3000, t] 内发生的请求数。
保证 每次对 ping 的调用都使用比之前更大的 t 值。


示例：
输入：
inputs = ["RecentCounter", "ping", "ping", "ping", "ping"]
inputs = [[], [1], [100], [3001], [3002]]
输出：
[null, 1, 2, 3, 3]
解释：
RecentCounter recentCounter = new RecentCounter();
recentCounter.ping(1);     // requests = [1]，范围是 [-2999,1]，返回 1
recentCounter.ping(100);   // requests = [1, 100]，范围是 [-2900,100]，返回 2
recentCounter.ping(3001);  // requests = [1, 100, 3001]，范围是 [1,3001]，返回 3
recentCounter.ping(3002);  // requests = [1, 100, 3001, 3002]，范围是 [2,3002]，返回 3


提示：
1 <= t <= 10^9
保证每次对 ping 调用所使用的 t 值都 严格递增
至多调用 ping 方法 10^4 次
"""
from collections import deque


class RecentCounter:
    """
    二分查找。因为至多调用 ping 方法 10^4 次，所以最多存储 10^4 个元素。
    还可以用循环队列，只需3000个存储空间即可
    """

    def __init__(self):
        self.ts = []
        self.min_idx = 0
        self.size = 0

    def ping(self, t: int) -> int:
        self.ts.append(t)
        self.size += 1
        left, right = self.min_idx, self.size - 1
        target = t - 3000
        while left < right:
            mid = left + (right - left) // 2
            if self.ts[mid] >= target:
                right = mid
            else:
                left = mid + 1
        self.min_idx = left
        return self.size - left


class RecentCounter2:
    """双端队列"""

    def __init__(self):
        self.queue = deque()

    def ping(self, t: int) -> int:
        self.queue.append(t)
        while self.queue[0] < t - 3000:
            self.queue.popleft()
        return len(self.queue)


if __name__ == '__main__':
    obj = RecentCounter()
    print(obj.ping(1))
    print(obj.ping(100))
    print(obj.ping(3001))
    print(obj.ping(3002))
