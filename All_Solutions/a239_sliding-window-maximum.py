# -*- coding: UTF-8 -*-
"""
title: 滑动窗口最大值
You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.
Return the max sliding window.


Example 1:
Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation:
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7

Example 2:
Input: nums = [1], k = 1
Output: [1]


Constraints:
1 <= nums.length <= 10^5
-10^4 <= nums[i] <= 10^4
1 <= k <= nums.length
"""
import heapq
from collections import deque
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """暴力。超时"""
        res = []
        # 总共有 len(nums) - k + 1 个滑动窗口
        for i in range(len(nums) - k + 1):
            res.append(max(nums[i:i + k]))
        return res

    def maxSlidingWindow_2(self, nums: List[int], k: int) -> List[int]:
        """优先队列(大根堆)"""
        res = []
        queue = []
        for i in range(len(nums)):
            # heapq 默认是小根堆，升序
            heapq.heappush(queue, (-nums[i], i))
            while queue[0][1] <= i - k:
                heapq.heappop(queue)
            if i >= k - 1:
                res.append(-queue[0][0])
        return res

    def maxSlidingWindow_3(self, nums: List[int], k: int) -> List[int]:
        """
        单调递减的双端队列。若当前滑动窗口内存在i < j 且 nums[i] <= nums[j]，则在之后的滑动窗口中，只要i存在，j就一定存在，
        它两同时存在的情况下，i就永远不可能是滑动窗口内的最大值，所以当j出现在滑动窗口内时，i就可以直接从队列里删掉了。
        """
        res = []
        # queue中保存的是元素下标，这些下标所对应的元素是严格单调递减的
        queue = deque()
        for i in range(len(nums)):
            while queue and nums[i] >= nums[queue[-1]]:
                queue.pop()
            queue.append(i)
            while queue[0] <= i - k:
                queue.popleft()
            if i >= k - 1:
                res.append(nums[queue[0]])
        return res


if __name__ == '__main__':
    print(Solution().maxSlidingWindow_3(nums=[1, 3, -1, -3, 5, 3, 6, 7], k=3))
