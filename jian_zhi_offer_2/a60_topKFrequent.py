# -*- coding: UTF-8 -*-
"""
title: 出现频率最高的 k 个数字
给定一个整数数组 nums 和一个整数 k ，请返回其中出现频率前 k 高的元素。可以按 任意顺序 返回答案。


示例 1:
输入: nums = [1,1,1,2,2,3], k = 2
输出: [1,2]

示例 2:
输入: nums = [1], k = 1
输出: [1]


提示：
1 <= nums.length <= 10^5
k 的取值范围是 [1, 数组中不相同的元素的个数]
题目数据保证答案唯一，换句话说，数组中前 k 个高频元素的集合是唯一的

进阶：所设计算法的时间复杂度 必须 优于O(nlogn) ，其中 n 是数组大小。
"""
from collections import Counter
from typing import List
import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        时间复杂度 必须 优于O(nlogn)，就意味着不能用排序。
        """
        n = len(nums)
        # nums 中任何数的出现次数都不可能大于len(nums)
        cnts = [[] for _ in range(n)]
        for num, cnt in Counter(nums).items():
            cnts[cnt - 1].append(num)
        res = []
        for i in range(n - 1, -1, -1):
            if cnts[i]:
                res.extend(cnts[i])
                # 题目数据保证答案唯一，换句话说，数组中前 k 个高频元素的集合是唯一的
                if len(res) == k:
                    break
        return res

    def topKFrequent_2(self, nums: List[int], k: int) -> List[int]:
        """最小堆"""
        min_heap = []
        size = 0
        for num, cnt in Counter(nums).items():
            if size == k:
                if min_heap[0][0] < cnt:
                    heapq.heappop(min_heap)
                    heapq.heappush(min_heap, (cnt, num))
            else:
                heapq.heappush(min_heap, (cnt, num))
                size += 1
        return [num for _, num in min_heap]


if __name__ == '__main__':
    print(Solution().topKFrequent(nums=[1], k=1))
