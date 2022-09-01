# -*- coding: UTF-8 -*-
"""
title: 最大频率栈
Design a stack-like data structure to push elements to the stack and pop the most frequent element from the stack.
Implement the FreqStack class:
    FreqStack() constructs an empty frequency stack.
    void push(int val) pushes an integer val onto the top of the stack.
    int pop() removes and returns the most frequent element in the stack.
        If there is a tie for the most frequent element, the element closest to the stack's top is removed and returned.


Example 1:
Input
["FreqStack", "push", "push", "push", "push", "push", "push", "pop", "pop", "pop", "pop"]
[[], [5], [7], [5], [7], [4], [5], [], [], [], []]
Output
[null, null, null, null, null, null, null, 5, 7, 5, 4]
Explanation
FreqStack freqStack = new FreqStack();
freqStack.push(5); // The stack is [5]
freqStack.push(7); // The stack is [5,7]
freqStack.push(5); // The stack is [5,7,5]
freqStack.push(7); // The stack is [5,7,5,7]
freqStack.push(4); // The stack is [5,7,5,7,4]
freqStack.push(5); // The stack is [5,7,5,7,4,5]
freqStack.pop();   // return 5, as 5 is the most frequent. The stack becomes [5,7,5,7,4].
freqStack.pop();   // return 7, as 5 and 7 is the most frequent, but 7 is closest to the top. The stack becomes [5,7,5,4].
freqStack.pop();   // return 5, as 5 is the most frequent. The stack becomes [5,7,4].
freqStack.pop();   // return 4, as 4, 5 and 7 is the most frequent, but 4 is closest to the top. The stack becomes [5,7].


Constraints:
0 <= val <= 10^9
At most 2 * 10^4 calls will be made to push and pop.
It is guaranteed that there will be at least one element in the stack before calling pop.
"""
import heapq
from collections import defaultdict


class FreqStack:
    """优先队列(最大堆) + 哈希表"""

    def __init__(self):
        self.idx = 0
        self.nums = []
        self.num2freq = defaultdict(int)

    def push(self, val: int) -> None:
        self.num2freq[val] += 1
        self.idx += 1
        heapq.heappush(self.nums, (-self.num2freq[val], -self.idx, val))

    def pop(self) -> int:
        _, _, num = heapq.heappop(self.nums)
        self.num2freq[num] -= 1
        return num


class FreqStack2:
    """栈 + 哈希表"""

    def __init__(self):
        self.num2freq = defaultdict(int)
        self.freq2nums = defaultdict(list)
        self.max_freq = 0

    def push(self, val: int) -> None:
        self.num2freq[val] += 1
        if self.num2freq[val] > self.max_freq:
            self.max_freq = self.num2freq[val]
        self.freq2nums[self.num2freq[val]].append(val)

    def pop(self) -> int:
        num = self.freq2nums[self.max_freq].pop()
        self.num2freq[num] -= 1
        if not self.freq2nums[self.max_freq]:
            # 因为max_freq是一步步涨上去的，所以减也是一步步减
            self.max_freq -= 1
        return num


if __name__ == '__main__':
    obj = FreqStack()
    obj.push(5)
    obj.push(7)
    obj.push(5)
    obj.push(7)
    obj.push(4)
    obj.push(5)
    print(obj.pop())
    print(obj.pop())
    print(obj.pop())
    print(obj.pop())
