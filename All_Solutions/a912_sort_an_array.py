# -*- coding: UTF-8 -*-
"""
title: 排序数组
Given an array of integers nums, sort the array in ascending order and return it.
You must solve the problem without using any built-in functions in O(nlog(n)) time complexity and with the smallest space complexity possible.


Example 1:
Input: nums = [5,2,3,1]
Output: [1,2,3,5]
Explanation: After sorting the array, the positions of some numbers are not changed (for example, 2 and 3), while the positions of other numbers are changed (for example, 1 and 5).

Example 2:
Input: nums = [5,1,1,2,0,0]
Output: [0,0,1,1,2,5]
Explanation: Note that the values of nums are not necessairly unique.


Constraints:
1 <= nums.length <= 5 * 10^4
-5 * 10^4 <= nums[i] <= 5 * 10^4
"""
from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        """堆(最大堆)排序。用时 1264 ms"""
        for heap_size in range(len(nums), 1, -1):
            self.max_heap(nums, heap_size)
            nums[0], nums[heap_size - 1] = nums[heap_size - 1], nums[0]
        return nums

    def max_heap(self, nums: List[int], heap_size: int) -> None:
        # 最后一个非叶节点的下标
        end = heap_size // 2 - 1
        # 若heap_size == len(nums)，则表示是初始化最大堆，其余情况为更新最大堆
        start = end if heap_size == len(nums) else 0
        while start >= 0:
            i = start
            while i <= end:
                l, r = 2 * i + 1, 2 * i + 2
                max_idx = r if r < heap_size and nums[r] >= nums[l] else l
                if nums[i] >= nums[max_idx]:
                    break
                nums[i], nums[max_idx] = nums[max_idx], nums[i]
                i = max_idx
            start -= 1

    def sortArray_2(self, nums: List[int]) -> List[int]:
        """快速排序。运行超时"""
        import random
        if len(nums) < 2:
            return nums
        # 固定使用nums[0]作为分界值pivot。通过 11/18 个测试用例
        # mid_num = nums[0]
        # 随机确定分界值pivot。通过 17/18 个测试用例
        mid_idx = random.randrange(0, len(nums))
        mid_num = nums[mid_idx]
        left = self.sortArray_2([num for idx, num in enumerate(nums) if num <= mid_num and idx != mid_idx])
        right = self.sortArray_2([num for idx, num in enumerate(nums) if num > mid_num and idx != mid_idx])
        return left + [mid_num] + right

    def sortArray_3(self, nums: List[int]) -> List[int]:
        """归并排序。用时 952 ms"""
        self.merge_sort(nums, 0, len(nums) - 1)
        return nums

    def merge_sort(self, nums: List[int], l: int, r: int) -> None:
        if l >= r:
            return
        mid = (l + r) // 2
        self.merge_sort(nums, l, mid)
        self.merge_sort(nums, mid + 1, r)
        tmp = []
        i, j = l, mid + 1
        while i <= mid or j <= r:
            if i > mid or (j <= r and nums[i] > nums[j]):
                tmp.append(nums[j])
                j += 1
            else:
                tmp.append(nums[i])
                i += 1
        nums[l:r + 1] = tmp


if __name__ == '__main__':
    print(Solution().sortArray_2([5, 2, 3, 1]))
