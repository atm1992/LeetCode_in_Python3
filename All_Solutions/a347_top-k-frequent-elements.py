# -*- coding: UTF-8 -*-
"""
title: 前 K 个高频元素
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.


Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:
Input: nums = [1], k = 1
Output: [1]


Constraints:
1 <= nums.length <= 10^5
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.

Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
"""
from collections import Counter
from typing import List
import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        n = len(nums)
        # nums 中任何数的出现次数都不可能大于len(nums)
        cnts = [[] for _ in range(n)]
        for num, cnt in Counter(nums).items():
            cnts[cnt - 1].append(num)
        for i in range(n - 1, -1, -1):
            if cnts[i]:
                res.extend(cnts[i])
                if len(res) >= k:
                    break
        return res[:k]

    def topKFrequent_2(self, nums: List[int], k: int) -> List[int]:
        """最小堆"""
        size = 0
        min_heap = []
        for num, cnt in Counter(nums).items():
            if size == k:
                if cnt > min_heap[0][0]:
                    heapq.heappop(min_heap)
                    heapq.heappush(min_heap, (cnt, num))
            else:
                heapq.heappush(min_heap, (cnt, num))
                size += 1
        return [item[1] for item in min_heap]


if __name__ == '__main__':
    print(Solution().topKFrequent_2(nums=[4,1,-1,2,-1,2,3], k=2))
