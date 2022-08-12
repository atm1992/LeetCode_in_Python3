# -*- coding: UTF-8 -*-
"""
title: 滑动窗口的最大值
给定一个数组 nums 和滑动窗口的大小 k，请找出所有滑动窗口里的最大值。


示例:
输入: nums = [1,3,-1,-3,5,3,6,7], 和 k = 3
输出: [3,3,5,5,6,7]
解释:
  滑动窗口的位置                最大值
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7


提示：
你可以假设 k 总是有效的，在输入数组不为空的情况下，1 ≤ k ≤ 输入数组的大小。
"""
import heapq
from typing import List
from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """优先队列(大根堆)"""
        res = []
        heap = []
        for idx, num in enumerate(nums):
            # heapq 默认是小根堆，升序
            heapq.heappush(heap, (-num, idx))
            if idx >= k - 1:
                while heap[0][1] < idx - k + 1:
                    heapq.heappop(heap)
                res.append(-heap[0][0])
        return res

    def maxSlidingWindow_2(self, nums: List[int], k: int) -> List[int]:
        """
        单调递减的双端队列。若当前滑动窗口内存在i < j 且 nums[i] <= nums[j]，则在之后的滑动窗口中，只要i存在，j就一定存在，
        它两同时存在的情况下，i就永远不可能是滑动窗口内的最大值，所以当j出现在滑动窗口内时，i就可以直接从队列里删掉了。
        """
        res = []
        queue = deque()
        for idx, num in enumerate(nums):
            while queue and queue[-1][0] <= num:
                queue.pop()
            queue.append((num, idx))
            if idx >= k - 1:
                while queue[0][1] < idx - k + 1:
                    queue.popleft()
                res.append(queue[0][0])
        return res


if __name__ == '__main__':
    print(Solution().maxSlidingWindow_2(nums=[1, 3, -1, -3, 5, 3, 6, 7], k=3))
