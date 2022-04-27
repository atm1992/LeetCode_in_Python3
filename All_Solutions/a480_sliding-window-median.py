# -*- coding: UTF-8 -*-
"""
title: 滑动窗口中位数
The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle values.
    For examples, if arr = [2,3,4], the median is 3.
    For examples, if arr = [1,2,3,4], the median is (2 + 3) / 2 = 2.5.
You are given an integer array nums and an integer k. There is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.
Return the median array for each window in the original array. Answers within 10^-5 of the actual value will be accepted.


Example 1:
Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [1.00000,-1.00000,-1.00000,3.00000,5.00000,6.00000]
Explanation:
Window position                Median
---------------                -----
[1  3  -1] -3  5  3  6  7        1
 1 [3  -1  -3] 5  3  6  7       -1
 1  3 [-1  -3  5] 3  6  7       -1
 1  3  -1 [-3  5  3] 6  7        3
 1  3  -1  -3 [5  3  6] 7        5
 1  3  -1  -3  5 [3  6  7]       6

Example 2:
Input: nums = [1,2,3,4,2,3,1,4,2], k = 3
Output: [2.00000,3.00000,3.00000,3.00000,2.00000,3.00000,2.00000]


Constraints:
1 <= k <= nums.length <= 10^5
-2^31 <= nums[i] <= 2^31 - 1
"""
import heapq
from collections import defaultdict
from typing import List


class Solution:
    def __init__(self):
        self.left_heap = []
        self.right_heap = []

    def get_median(self, k: int) -> float:
        return float(-self.left_heap[0]) if k & 1 else (-self.left_heap[0] + self.right_heap[0]) / 2

    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        """双优先队列 + 延迟删除"""
        res = []
        for idx in range(k):
            heapq.heappush(self.left_heap, -nums[idx])
        # 若k为奇数，则left_heap比right_heap多一个；若k为偶数，则left_heap与right_heap个数相等。for循环结束后，达到平衡态，balance = 0
        for _ in range(k // 2):
            heapq.heappush(self.right_heap, -heapq.heappop(self.left_heap))
        res.append(self.get_median(k))
        # balance 指的是 left_heap中处于滑动窗口中的元素个数 与 right_heap中处于滑动窗口中的元素个数 之间的大小关系。
        # 在平衡态的基础上，若left_heap更多，则balance为正数
        balance = 0
        # 需延迟删除的元素及其次数
        delayed = defaultdict(int)
        for idx in range(k, len(nums)):
            left_num, right_num = nums[idx - k], nums[idx]
            delayed[left_num] += 1
            # 滑动窗口左侧出去一个元素
            if left_num <= -self.left_heap[0]:
                # 若是需要从left_heap出去，则left_heap更少了，所以balance减1
                balance -= 1
            else:
                # 若是需要从right_heap出去，则left_heap更多了，所以balance加1
                balance += 1

            # 滑动窗口右侧进来一个元素
            if right_num <= -self.left_heap[0]:
                # 若是进入到left_heap，则left_heap更多了，所以balance加1
                heapq.heappush(self.left_heap, -right_num)
                balance += 1
            else:
                # 若是进入到right_heap，则left_heap更少了，所以balance减1
                heapq.heappush(self.right_heap, right_num)
                balance -= 1

            # 对于等于 -self.left_heap[0] 的元素，优先会进入left_heap，所以删除也应该优先从left_heap删除
            while self.left_heap and delayed[-self.left_heap[0]]:
                delayed[-self.left_heap[0]] -= 1
                heapq.heappop(self.left_heap)
            while self.right_heap and delayed[self.right_heap[0]]:
                delayed[self.right_heap[0]] -= 1
                heapq.heappop(self.right_heap)

            # 上面一出一进，balance的结果有3种可能：0 (-1+1 或 +1-1)、-2 (-1-1)、+2 (+1+1)
            if balance > 0:
                # 此时left_heap比right_heap多2，所以需要从left_heap移出一个到right_heap
                heapq.heappush(self.right_heap, -heapq.heappop(self.left_heap))
                balance -= 2
            elif balance < 0:
                # 此时left_heap比right_heap少2，所以需要从right_heap移出一个到left_heap
                heapq.heappush(self.left_heap, -heapq.heappop(self.right_heap))
                balance += 2

            # 对于等于 -self.left_heap[0] 的元素，优先会进入left_heap，所以删除也应该优先从left_heap删除
            while self.left_heap and delayed[-self.left_heap[0]]:
                delayed[-self.left_heap[0]] -= 1
                heapq.heappop(self.left_heap)
            while self.right_heap and delayed[self.right_heap[0]]:
                delayed[self.right_heap[0]] -= 1
                heapq.heappop(self.right_heap)
            res.append(self.get_median(k))
        return res


if __name__ == '__main__':
    print(Solution().medianSlidingWindow(nums=[7, 8, 8, 3, 8, 1, 5, 3, 5, 4], k=3))
