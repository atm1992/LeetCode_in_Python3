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
    # 最优方法：递归版的三路随机快排，其次是归并排序
    def sortArray(self, nums: List[int]) -> List[int]:
        """堆(最大堆)排序。用时 1240 ms"""

        def max_heap(nums: List[int], heap_size: int) -> None:
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

        for heap_size in range(len(nums), 1, -1):
            max_heap(nums, heap_size)
            nums[0], nums[heap_size - 1] = nums[heap_size - 1], nums[0]
        return nums

    def sortArray_2(self, nums: List[int]) -> List[int]:
        """递归版的普通随机快排。运行超时"""
        import random
        if len(nums) < 2:
            return nums
        # 固定使用nums[0]作为分界值pivot。通过 11/20 个测试用例
        # mid_num = nums[0]
        # 随机确定分界值pivot。通过 17/20 个测试用例
        mid_idx = random.randrange(0, len(nums))
        mid_num = nums[mid_idx]
        left = self.sortArray_2([num for idx, num in enumerate(nums) if num <= mid_num and idx != mid_idx])
        right = self.sortArray_2([num for idx, num in enumerate(nums) if num > mid_num and idx != mid_idx])
        return left + [mid_num] + right

    def sortArray_2_2(self, nums: List[int]) -> List[int]:
        """递归版的三路随机快排。用时 752 ms"""
        import random
        n = len(nums)
        if n < 2:
            return nums
        mid_idx = random.randrange(0, n)
        mid_num = nums[mid_idx]
        left = self.sortArray_2_2([num for num in nums if num < mid_num])
        right = self.sortArray_2_2([num for num in nums if num > mid_num])
        return left + [mid_num] * (n - len(left) - len(right)) + right

    def sortArray_3(self, nums: List[int]) -> List[int]:
        """迭代版的普通随机快排。运行超时"""
        import random
        if len(nums) < 2:
            return nums
        stack = [(0, len(nums) - 1)]
        while stack:
            low, high = stack.pop()
            # 固定使用nums[high]作为分界值pivot。通过 11/20 个测试用例
            # pivot = nums[high]
            # 随机确定分界值pivot。通过 17/20 个测试用例
            p_idx = random.randrange(low, high + 1)
            nums[p_idx], nums[high] = nums[high], nums[p_idx]
            pivot = nums[high]
            i = low
            for j in range(low, high):
                if nums[j] <= pivot:
                    if j != i:
                        nums[i], nums[j] = nums[j], nums[i]
                    i += 1
            nums[i], nums[high] = nums[high], nums[i]
            if i - 1 > low:
                stack.append((low, i - 1))
            if high > i + 1:
                stack.append((i + 1, high))
        return nums

    def sortArray_3_2(self, nums: List[int]) -> List[int]:
        """迭代版的三路随机快排。用时 1244 ms"""
        import random
        if len(nums) < 2:
            return nums
        stack = [(0, len(nums) - 1)]
        while stack:
            low, high = stack.pop()
            p_idx = random.randrange(low, high + 1)
            nums[p_idx], nums[high] = nums[high], nums[p_idx]
            pivot = nums[high]
            lt, gt = low - 1, high
            i = low
            while i < gt:
                if nums[i] < pivot:
                    # lt指向小于pivot的最后一个元素，lt + 1指向大于等于pivot的第一个元素
                    nums[i], nums[lt + 1] = nums[lt + 1], nums[i]
                    lt += 1
                    i += 1
                elif nums[i] > pivot:
                    # gt指向大于pivot的第一个元素，gt - 1指向小于等于pivot的最后一个元素
                    nums[i], nums[gt - 1] = nums[gt - 1], nums[i]
                    # 注意：此时的i不变，因为之后需要再判断交换后的新nums[i]
                    gt -= 1
                else:
                    i += 1
            nums[high], nums[gt] = nums[gt], nums[high]
            if lt > low:
                stack.append((low, lt))
            if high > gt + 1:
                stack.append((gt + 1, high))
        return nums

    def sortArray_4(self, nums: List[int]) -> List[int]:
        """归并排序。用时 876 ms"""

        def merge_sort(nums: List[int], l: int, r: int) -> None:
            if l >= r:
                return
            mid = (l + r) // 2
            merge_sort(nums, l, mid)
            merge_sort(nums, mid + 1, r)
            tmp = []
            i, j = l, mid + 1
            while i <= mid and j <= r:
                if nums[i] > nums[j]:
                    tmp.append(nums[j])
                    j += 1
                else:
                    tmp.append(nums[i])
                    i += 1
            if i <= mid:
                tmp.extend(nums[i:mid + 1])
            elif j <= r:
                tmp.extend(nums[j:r + 1])
            nums[l:r + 1] = tmp

        merge_sort(nums, 0, len(nums) - 1)
        return nums


if __name__ == '__main__':
    print(Solution().sortArray_3_2([5, 1, 1, 2, 0, 0]))
