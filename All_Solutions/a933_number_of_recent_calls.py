# -*- coding: UTF-8 -*-
"""
title: 最近的请求次数
You have a RecentCounter class which counts the number of recent requests within a certain time frame.
Implement the RecentCounter class:
    RecentCounter() Initializes the counter with zero recent requests.
    int ping(int t) Adds a new request at time t, where t represents some time in milliseconds, and returns the number of requests that has happened in the past 3000 milliseconds (including the new request). Specifically, return the number of requests that have happened in the inclusive range [t - 3000, t].
It is guaranteed that every call to ping uses a strictly larger value of t than the previous call.


Example 1:
Input
["RecentCounter", "ping", "ping", "ping", "ping"]
[[], [1], [100], [3001], [3002]]
Output
[null, 1, 2, 3, 3]
Explanation
RecentCounter recentCounter = new RecentCounter();
recentCounter.ping(1);     // requests = [1], range is [-2999,1], return 1
recentCounter.ping(100);   // requests = [1, 100], range is [-2900,100], return 2
recentCounter.ping(3001);  // requests = [1, 100, 3001], range is [1,3001], return 3
recentCounter.ping(3002);  // requests = [1, 100, 3001, 3002], range is [2,3002], return 3


Constraints:
1 <= t <= 10^9
Each test case will call ping with strictly increasing values of t.
At most 10^4 calls will be made to ping.
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
