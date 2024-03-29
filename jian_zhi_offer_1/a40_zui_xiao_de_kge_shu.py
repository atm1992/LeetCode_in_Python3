# -*- coding: UTF-8 -*-
"""
title: 最小的k个数
输入整数数组 arr ，找出其中最小的 k 个数。例如，输入4、5、1、6、2、7、3、8这8个数字，则最小的4个数字是1、2、3、4。


示例 1：
输入：arr = [3,2,1], k = 2
输出：[1,2] 或者 [2,1]

示例 2：
输入：arr = [0,1,2,1], k = 1
输出：[0]


限制：
0 <= k <= arr.length <= 10000
0 <= arr[i] <= 10000
"""
import heapq
from typing import List


class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        """排序"""
        n = len(arr)
        if n == 0 or k == 0:
            return []
        arr.sort()
        return arr[:k]

    def getLeastNumbers_2(self, arr: List[int], k: int) -> List[int]:
        """大根堆"""
        n = len(arr)
        if n == 0 or k == 0:
            return []
        # 因为Python中的heapq默认为小根堆
        heap = [-num for num in arr[:k]]
        heapq.heapify(heap)
        for num in arr[k:]:
            if num < -heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, -num)
        return [-num for num in heap]


if __name__ == '__main__':
    print(Solution().getLeastNumbers_2(arr=[3, 2, 1], k=2))
