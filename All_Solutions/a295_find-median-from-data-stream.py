# -*- coding: UTF-8 -*-
"""
title: 数据流的中位数
The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value and the median is the mean of the two middle values.
    For example, for arr = [2,3,4], the median is 3.
    For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
Implement the MedianFinder class:
    MedianFinder() initializes the MedianFinder object.
    void addNum(int num) adds the integer num from the data stream to the data structure.
    double findMedian() returns the median of all elements so far. Answers within 10^-5 of the actual answer will be accepted.


Example 1:
Input
["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
[[], [1], [2], [], [3], []]
Output
[null, null, null, 1.5, null, 2.0]
Explanation
MedianFinder medianFinder = new MedianFinder();
medianFinder.addNum(1);    // arr = [1]
medianFinder.addNum(2);    // arr = [1, 2]
medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
medianFinder.addNum(3);    // arr[1, 2, 3]
medianFinder.findMedian(); // return 2.0


Constraints:
-10^5 <= num <= 10^5
There will be at least one element in the data structure before calling findMedian.
At most 5 * 10^4 calls will be made to addNum and findMedian.

Follow up:
If all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?
If 99% of all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?
"""
import heapq


class MedianFinder:
    """优先队列"""

    def __init__(self):
        # left 为最大堆，right 为最小堆
        self.left = []
        self.right = []
        self.left_cnt = 0
        self.right_cnt = 0

    def addNum(self, num: int) -> None:
        if self.left_cnt <= self.right_cnt:
            if self.right and num > self.right[0]:
                heapq.heappush(self.right, num)
                num = heapq.heappop(self.right)
            # 由于heapq默认为最小堆，所以left中的元素需要先加个负号，再存入
            heapq.heappush(self.left, -num)
            self.left_cnt += 1
        else:
            # 存入right时，left中肯定已经有了元素，所以无需判断left是否不为空
            if num < -self.left[0]:
                heapq.heappush(self.left, -num)
                num = -heapq.heappop(self.left)
            heapq.heappush(self.right, num)
            self.right_cnt += 1

    def findMedian(self) -> float:
        if self.left_cnt == self.right_cnt:
            return (-self.left[0] + self.right[0]) / 2
        else:
            return -self.left[0]


class MedianFinder_2:
    """有序集合。执行速度不如上面"""

    def __init__(self):
        from sortedcontainers import SortedList

        self.nums = SortedList()

    def addNum(self, num: int) -> None:
        self.nums.add(num)

    def findMedian(self) -> float:
        n = len(self.nums)
        mid = n >> 1
        return self.nums[mid] if n & 1 else (self.nums[mid] + self.nums[mid - 1]) / 2


if __name__ == '__main__':
    medianFinder = MedianFinder()
    medianFinder.addNum(1)
    medianFinder.addNum(2)
    print(medianFinder.findMedian())
    medianFinder.addNum(3)
    print(medianFinder.findMedian())
