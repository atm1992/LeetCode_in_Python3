# -*- coding: UTF-8 -*-
"""
title: 最大连续1的个数 III
Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.


Example 1:
Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

Example 2:
Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.


Constraints:
1 <= nums.length <= 10^5
nums[i] is either 0 or 1.
0 <= k <= nums.length
"""
from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        """
        前缀和 + 二分查找
        对于任意可能的right(每一小段1中的最后一个1)，找到最小的left，使得 [left, right] 区间内0的个数 <= k，
        所有[left, right]区间的长度的最大值就是最终结果
        为方便对区间内的0计数，可考虑将原始数组nums中的1变成0、0变成1，这样就可通过前缀和来快速求解某个区间内0的个数了。
        前缀和数组是单调递增的，所以可使用二分查找来降低时间复杂度
        """
        pre_sum = [0]
        for num in nums:
            # 1 - num 可以让原来的1变成0、0变成1
            pre_sum.append(pre_sum[-1] + (1 - num))
        res = 0
        for right in range(len(nums)):
            if pre_sum[right + 1] <= k:
                left = 0
            else:
                # 在pre_sum[1:right+2]中二分查找nums中最小的left
                # 注意：这里的low、high、mid都是pre_sum中的下标，pre_sum中的下标减1就是nums中对应的下标
                low, high = 1, right + 1
                while low < high:
                    mid = (low + high) // 2
                    # pre_sum[right + 1] - pre_sum[mid] <= k，则说明pre_sum中[mid+1, right+1]区间内0的个数 <= k
                    # 即 nums中[mid, right]区间内0的个数 <= k
                    if pre_sum[right + 1] - pre_sum[mid] <= k:
                        high = mid
                    else:
                        low = mid + 1
                # [left, right]区间内0的个数 <= k。当left等于right + 1时，则说明是个空区间，该区间的长度为0
                left = low
            res = max(res, right - left + 1)
        return res

    def longestOnes_2(self, nums: List[int], k: int) -> int:
        """
        滑动窗口。
        上个方法中，已知前缀和数组是单调递增的，其实在向右移动right的过程中，为满足区间内0的个数 <= k，left也是递增的向右移动，
        所以，可使用一个滑动窗口来维持区间内0的个数 <= k
        区间内0的个数依旧使用前缀和进行计算，但并不需要显式的保存一个前缀和数组，使用两个变量l_sum、r_sum分别维护区间[0,left]、区间[0,right]内0的个数
        """
        left = l_sum = r_sum = 0
        res = 0
        for right in range(len(nums)):
            r_sum += 1 - nums[right]
            while r_sum - l_sum > k:
                l_sum += 1 - nums[left]
                left += 1
            res = max(res, right - left + 1)
        return res

    def longestOnes_3(self, nums: List[int], k: int) -> int:
        """
        滑动窗口。参考LeetCode题424
        滑动窗口的长度要么保持(记录曾经的最大长度)，要么加1(k >= 0时)。
        最后一个滑动窗口的长度就是最终返回结果。注意：最后一个滑动窗口内未必是全1。
        """
        n = len(nums)
        left = 0
        for right in range(n):
            if nums[right] == 0:
                k -= 1
            # 当k < 0时，left跟随right右移一位，维持曾经的最大长度；当k >= 0时，left不移动，在曾经的最大长度的基础上加1
            if k < 0:
                if nums[left] == 0:
                    k += 1
                left += 1
        return n - left


if __name__ == '__main__':
    print(Solution().longestOnes_3(nums = [0,0,0,0], k = 0))
