# -*- coding: UTF-8 -*-
"""
title: 最大子序和
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
A subarray is a contiguous part of an array.


Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Example 2:
Input: nums = [1]
Output: 1

Example 3:
Input: nums = [5,4,-1,7,8]
Output: 23


Constraints:
1 <= nums.length <= 10^5
-10^4 <= nums[i] <= 10^4
 

Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
"""
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """贪心算法"""
        res = -10 ** 4
        tmp_sum = 0
        for num in nums:
            tmp_sum += num
            res = max(res, tmp_sum)
            tmp_sum = max(tmp_sum, 0)
        return res

    def maxSubArray_2(self, nums: List[int]) -> int:
        """动态规划"""
        res = -10 ** 4
        # pre_sum 表示当前num之前的子数组最大和
        pre_sum = 0
        for num in nums:
            # 当前num是否需要加上之前的最大和
            pre_sum = max(pre_sum + num, num)
            res = max(res, pre_sum)
        return res


class Solution_2:
    class Status:
        def __init__(self, l_sum, r_sum, m_sum, i_sum):
            self.l_sum = l_sum
            self.r_sum = r_sum
            self.m_sum = m_sum
            self.i_sum = i_sum

    def maxSubArray(self, nums: List[int]) -> int:
        """分治法。线段树，可以在 O(log n) 的时间内求解出任意区间内的答案，适用于大规模查询的情况。
        对于每个区间 [l,r]，维护4个变量：
        1、l_sum 表示 [l,r] 内以 l 为左端点的最大子段和；
        2、r_sum 表示 [l,r] 内以 r 为右端点的最大子段和；
        3、m_sum 表示 [l,r] 内的最大子段和，它始终是这4个变量中最大的；
        4、i_sum 表示 [l,r] 区间的总和。
        对于长度为 1 的区间，这4个变量的值都为nums[0]。"""
        return self.divide(nums, 0, len(nums) - 1).m_sum

    def divide(self, nums: List[int], l: int, r: int) -> Status:
        """向下分解"""
        if l == r:
            return self.Status(nums[l], nums[l], nums[l], nums[l])
        m = (l + r) // 2
        # l_sub、r_sub 分别是左子区间、右子区间。每个子区间也都是一个区间，也都有l_sum, r_sum, m_sum, i_sum这4个变量
        l_sub = self.divide(nums, l, m)
        r_sub = self.divide(nums, m + 1, r)
        return self.conquer(l_sub, r_sub)

    def conquer(self, l_sub: Status, r_sub: Status) -> Status:
        """向上合并"""
        i_sum = l_sub.i_sum + r_sub.i_sum
        l_sum = max(l_sub.l_sum, l_sub.i_sum + r_sub.l_sum)
        r_sum = max(r_sub.r_sum, r_sub.i_sum + l_sub.r_sum)
        m_sum = max(l_sub.m_sum, r_sub.m_sum, l_sub.r_sum + r_sub.l_sum)
        return self.Status(l_sum, r_sum, m_sum, i_sum)


if __name__ == '__main__':
    print(Solution_2().maxSubArray([5, 4, -1, 7, 8]))
