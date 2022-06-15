# -*- coding: UTF-8 -*-
"""
title: 数组中的第 k 大的数字
给定整数数组 nums 和整数 k，请返回数组中第 k 个最大的元素。
请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。


示例 1:
输入: [3,2,1,5,6,4] 和 k = 2
输出: 5

示例 2:
输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
输出: 4


提示：
1 <= k <= nums.length <= 10^4
-10^4 <= nums[i] <= 10^4
"""
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        # 1 <= k <= nums.length
        return nums[-k]

    def findKthLargest_2(self, nums: List[int], k: int) -> int:
        """堆排序。大根堆"""

        def max_heap(nums: List[int], heap_size: int) -> None:
            # 少于两个元素，不用排了
            if heap_size < 2:
                return
                # 下标从0开始，end表示最后一个非叶子节点的下标
            end = heap_size // 2 - 1
            # 若heap_size == len(nums)，则表示此次构建堆是初始化，所以需要从最后一个非叶子节点开始调整；如果不是初始化，则只需从根节点开始调整
            start = end if heap_size == len(nums) else 0
            while start >= 0:
                i = start
                while i <= end:
                    # 当前节点的左右孩子节点的下标
                    l = 2 * i + 1
                    r = 2 * i + 2
                    # 因为i <= end，所以当前节点i一定至少存在左孩子节点。获取两个孩子节点中，值更大的那个下标
                    max_idx = r if r < heap_size and nums[r] >= nums[l] else l
                    if nums[i] >= nums[max_idx]:
                        break
                    nums[i], nums[max_idx] = nums[max_idx], nums[i]
                    i = max_idx
                start -= 1

        n = len(nums)
        # 先初始化大根堆
        max_heap(nums, n)
        # 循环k-1次
        for heap_size in range(n - 1, n - k, -1):
            nums[0], nums[heap_size] = nums[heap_size], nums[0]
            max_heap(nums, heap_size)
        return nums[0]
