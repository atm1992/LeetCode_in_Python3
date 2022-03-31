# -*- coding: UTF-8 -*-
"""
title: 最大间距
Given an integer array nums, return the maximum difference between two successive elements in its sorted form. If the array contains less than two elements, return 0.
You must write an algorithm that runs in linear time and uses linear extra space.


Example 1:
Input: nums = [3,6,9,1]
Output: 3
Explanation: The sorted form of the array is [1,3,6,9], either (3,6) or (6,9) has the maximum difference 3.

Example 2:
Input: nums = [10]
Output: 0
Explanation: The array contains less than 2 elements, therefore return 0.


Constraints:
1 <= nums.length <= 10^5
0 <= nums[i] <= 10^9
"""
from typing import List


class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        """
        要求时间复杂度为O(n)，也就意味着不能用传统的基于比较的排序算法，而应该使用非比较型排序：基数排序、计数排序、桶排序。
        因为传统的基于比较的排序算法，它们的时间复杂度下限为O(nlogn)。又因为数据的范围较大(0 ~ 10^9)，所以排除计数排序。
        所以选择使用基数排序 和 桶排序。
        方法一：基于桶排序的基数排序。10^9 最多10位(1后面9个0)
        """
        n = len(nums)
        if n < 2:
            return 0
        # 基数为10，因为是10进制
        RADIX = 10
        exp = 1
        max_val = max(nums)
        while exp <= max_val:
            buckets = [[] for _ in range(RADIX)]
            for num in nums:
                # 放入第几个桶
                idx = (num // exp) % RADIX
                buckets[idx].append(num)
            nums.clear()
            # max_val最多10位，bucket个数为10，所以看着是3重循环，实际上时间复杂度依旧为O(n)
            # 虽然是O(n)，但在通常情况下，O(100n)是要慢于O(nlogn)的，因为n通常远小于2^100 = 1267650600228229401496703205376
            for bucket in buckets:
                for num in bucket:
                    # 在原nums中越靠前的元素，在各个bucket中也越靠前，所以是稳定的
                    nums.append(num)
            exp *= RADIX
        res = 0
        for i in range(n - 1):
            res = max(res, nums[i + 1] - nums[i])
        return res

    def maximumGap_2(self, nums: List[int]) -> int:
        """
        方法二：基于计数排序的基数排序
        """
        n = len(nums)
        if n < 2:
            return 0
        # 基数为10，因为是10进制
        RADIX = 10
        exp = 1
        max_val = max(nums)
        buf = [0] * n
        while exp <= max_val:
            cnt = [0] * RADIX
            for num in nums:
                # 当前位的数字
                digit = (num // exp) % RADIX
                cnt[digit] += 1
            for i in range(1, RADIX):
                cnt[i] += cnt[i - 1]
            for i in range(n - 1, -1, -1):
                digit = (nums[i] // exp) % RADIX
                # nums数组中，第exp分位上的数字小于等于digit的，有cnt[digit]个
                buf[cnt[digit] - 1] = nums[i]
                cnt[digit] -= 1
            nums = buf.copy()
            exp *= RADIX
        res = 0
        for i in range(n - 1):
            res = max(res, nums[i + 1] - nums[i])
        return res


if __name__ == '__main__':
    print(Solution().maximumGap_2([3, 6, 9, 1]))
