# -*- coding: UTF-8 -*-
"""
title: 队列的最大值
请定义一个队列并实现函数 max_value 得到队列里的最大值，要求函数max_value、push_back 和 pop_front 的均摊时间复杂度都是O(1)。
若队列为空，pop_front 和 max_value 需要返回 -1


示例 1：
输入:
["MaxQueue","push_back","push_back","max_value","pop_front","max_value"]
[[],[1],[2],[],[],[]]
输出: [null,null,null,2,1,2]

示例 2：
输入:
["MaxQueue","pop_front","max_value"]
[[],[],[]]
输出: [null,-1,-1]


限制：
1 <= push_back,pop_front,max_value的总操作数 <= 10000
1 <= value <= 10^5
"""
from collections import deque


class MaxQueue:

    def __init__(self):
        self.all_val = deque()
        # 维持单调递减，注意：并不是严格地单调递减
        self.max_val = deque()

    def max_value(self) -> int:
        return self.max_val[0] if self.max_val else -1

    def push_back(self, value: int) -> None:
        # 等于value的值，不pop
        while self.max_val and self.max_val[-1] < value:
            self.max_val.pop()
        self.max_val.append(value)
        self.all_val.append(value)

    def pop_front(self) -> int:
        if not self.all_val:
            return -1
        res = self.all_val.popleft()
        if res == self.max_val[0]:
            self.max_val.popleft()
        return res

# Your MaxQueue object will be instantiated and called as such:
# obj = MaxQueue()
# param_1 = obj.max_value()
# obj.push_back(value)
# param_3 = obj.pop_front()
