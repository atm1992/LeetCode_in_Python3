# -*- coding: UTF-8 -*-
import heapq
from typing import List


class Solution:
    def maximumProduct(self, nums: List[int], k: int) -> int:
        """优先增大较小的元素。使用优先队列"""
        if len(nums) == 1:
            return nums[0] + k

        heapq.heapify(nums)
        for _ in range(k):
            heapq.heappush(nums, heapq.heappop(nums) + 1)

        if nums[0] == 0:
            return 0

        res = 1
        mod = 10 ** 9 + 7
        for num in nums:
            res *= num
            res %= mod

        return res


if __name__ == '__main__':
    print(Solution().maximumProduct([0, 4], k=5))
