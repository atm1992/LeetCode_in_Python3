# -*- coding: UTF-8 -*-
"""
title: Range 模块
A Range Module is a module that tracks ranges of numbers. Design a data structure to track the ranges represented as half-open intervals and query about them.
A half-open interval [left, right) denotes all the real numbers x where left <= x < right.
Implement the RangeModule class:
    RangeModule() Initializes the object of the data structure.
    void addRange(int left, int right) Adds the half-open interval [left, right), tracking every real number in that interval. Adding an interval that partially overlaps with currently tracked numbers should add any numbers in the interval [left, right) that are not already tracked.
    boolean queryRange(int left, int right) Returns true if every real number in the interval [left, right) is currently being tracked, and false otherwise.
    void removeRange(int left, int right) Stops tracking every real number currently being tracked in the half-open interval [left, right).


Example 1:
Input
["RangeModule", "addRange", "removeRange", "queryRange", "queryRange", "queryRange"]
[[], [10, 20], [14, 16], [10, 14], [13, 15], [16, 17]]
Output
[null, null, null, true, false, true]
Explanation
RangeModule rangeModule = new RangeModule();
rangeModule.addRange(10, 20);
rangeModule.removeRange(14, 16);
rangeModule.queryRange(10, 14); // return True,(Every number in [10, 14) is being tracked)
rangeModule.queryRange(13, 15); // return False,(Numbers like 14, 14.03, 14.17 in [13, 15) are not being tracked)
rangeModule.queryRange(16, 17); // return True, (The number 16 in [16, 17) is still being tracked, despite the remove operation)


Constraints:
1 <= left < right <= 10^9
At most 10^4 calls will be made to addRange, queryRange, and removeRange.
"""


class RangeModule:
    """有序字典 + 二分查找"""

    def __init__(self):
        from sortedcontainers import SortedDict
        self.intervals = SortedDict()

    def addRange(self, left: int, right: int) -> None:
        # bisect_left 左侧严格小于查找值，即 all(val < x for val in a[lo:i]) and all(val >= x for val in a[i:hi])，大于等于查找值的第一个下标
        # bisect_right 查找值严格小于右侧，即 all(val <= x for val in a[lo:i]) and all(val > x for val in a[i:hi])，大于查找值的第一个下标
        # bisect 默认为 bisect_right
        idx = self.intervals.bisect_right(left)
        if idx > 0:
            start = idx - 1
            cur_left, cur_right = self.intervals.keys()[start], self.intervals.values()[start]
            # [left, right) 完全属于 [cur_left, cur_right)，因此无需任何操作
            if cur_right >= right:
                return
            # [cur_left, cur_right)的右半部分属于[left, right)，所以将[cur_left, cur_right) 与 [left, right) 合并
            if cur_right >= left:
                left = cur_left
                self.intervals.popitem(start)
                # 因为start位于idx前面，前面的start被pop掉了，所以idx要向前移1位
                idx -= 1
        # 从idx开始向后遍历，若[self.intervals.keys()[idx], self.intervals.values()[idx]) 与 [left, right) 存在交集，则进行合并
        # 合并过程中，不断pop掉当前idx，所以idx的值保持不变，但len(self.intervals)会逐渐减1，相当于后面的区间会不断前移
        while idx < len(self.intervals) and self.intervals.keys()[idx] <= right:
            right = max(right, self.intervals.values()[idx])
            self.intervals.popitem(idx)
        # 将最终确定的left、right，作为一个区间[left, right)，加入到self.intervals
        self.intervals[left] = right

    def queryRange(self, left: int, right: int) -> bool:
        idx = self.intervals.bisect_right(left)
        if idx == 0:
            return False
        return right <= self.intervals.values()[idx - 1]

    def removeRange(self, left: int, right: int) -> None:
        idx = self.intervals.bisect_right(left)
        if idx > 0:
            start = idx - 1
            cur_left, cur_right = self.intervals.keys()[start], self.intervals.values()[start]
            # 若当前区间[cur_left, cur_right)完全包含[left, right)，则只需对[cur_left, cur_right)进行处理，与其它区间无关，处理完[cur_left, cur_right)，就可直接return
            if cur_right >= right:
                if cur_left == left:
                    self.intervals.popitem(start)
                else:
                    self.intervals[cur_left] = left
                if cur_right > right:
                    self.intervals[right] = cur_right
                return
            # 若当前区间[cur_left, cur_right)中的一部分属于[left, right)，则需把[cur_left, cur_right)中的这部分删除掉
            elif cur_right > left:
                if cur_left == left:
                    self.intervals.popitem(start)
                    idx -= 1
                else:
                    self.intervals[cur_left] = left
        # 从idx开始向后遍历，若[self.intervals.keys()[idx], self.intervals.values()[idx]) 与 [left, right) 存在交集，则需把相交的部分删除掉。
        # 删除过程中，不断pop掉当前idx，所以idx的值保持不变，但len(self.intervals)会逐渐减1，相当于后面的区间会不断前移
        while idx < len(self.intervals) and self.intervals.keys()[idx] < right:
            # [self.intervals.keys()[idx], self.intervals.values()[idx]) 完全属于 [left, right)
            if self.intervals.values()[idx] <= right:
                self.intervals.popitem(idx)
            # [self.intervals.keys()[idx], self.intervals.values()[idx])中的左半部分属于[left, right)，
            # 之后的区间都不会与[left, right)存在交集，所以可以break退出
            else:
                self.intervals[right] = self.intervals.values()[idx]
                self.intervals.popitem(idx)
                break


if __name__ == '__main__':
    obj = RangeModule()
    obj.addRange(10, 20)
    obj.removeRange(14, 16)
    print(obj.queryRange(10, 14))
    print(obj.queryRange(13, 15))
    print(obj.queryRange(16, 17))
