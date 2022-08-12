# -*- coding: UTF-8 -*-
"""
title: 数组中的第K个最大元素
Given an integer array nums and an integer k, return the kth largest element in the array.
Note that it is the kth largest element in the sorted order, not the kth distinct element.


Example 1:
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5

Example 2:
Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4


Constraints:
1 <= k <= nums.length <= 10^4
-10^4 <= nums[i] <= 10^4
"""
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort(reverse=True)
        # 因为题目说明了 k <= nums.length
        return nums[k - 1]

    def findKthLargest_2(self, nums: List[int], k: int) -> int:
        """使用堆排序，因为是求第K大，所以使用大根堆。
        将原始待排序数列中的n个元素构造为初始堆（大根堆），其中的最大值位于第一个位置。
        将第一个位置的元素（最大值）与最后一个位置的元素（不一定最小）进行交换，将这个过程重复K-1次，然后取nums[0]，即为结果"""

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
                    # 若当前节点i的值大于等于两个孩子节点的值，则说明当前节点i不需要调整
                    if nums[i] >= nums[max_idx]:
                        break
                    # 将当前节点i 与 值更大的那个孩子节点，交换两者的值。然后让值更大的那个孩子节点成为当前节点，继续循环
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


if __name__ == '__main__':
    print(Solution().findKthLargest_2(nums=[3, 2, 1, 5, 6, 4], k=2))
