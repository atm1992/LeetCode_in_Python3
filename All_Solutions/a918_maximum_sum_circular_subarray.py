# -*- coding: UTF-8 -*-
"""
title: 环形子数组的最大和
Given a circular integer array nums of length n, return the maximum possible sum of a non-empty subarray of nums.
A circular array means the end of the array connects to the beginning of the array. Formally, the next element of nums[i] is nums[(i + 1) % n] and the previous element of nums[i] is nums[(i - 1 + n) % n].
A subarray may only include each element of the fixed buffer nums at most once. Formally, for a subarray nums[i], nums[i + 1], ..., nums[j], there does not exist i <= k1, k2 <= j with k1 % n == k2 % n.


Example 1:
Input: nums = [1,-2,3,-2]
Output: 3
Explanation: Subarray [3] has maximum sum 3.

Example 2:
Input: nums = [5,-3,5]
Output: 10
Explanation: Subarray [5,5] has maximum sum 5 + 5 = 10.

Example 3:
Input: nums = [-3,-2,-3]
Output: -2
Explanation: Subarray [-2] has maximum sum -2.


Constraints:
n == nums.length
1 <= n <= 3 * 10^4
-3 * 10^4 <= nums[i] <= 3 * 10^4
"""
from typing import List


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        """
        贪心
        可将原问题分为两种情况：
        1、子数组不是环状的，即 首尾不相连，按正常的贪心思路找出最大子数组的和
        2、子数组是环状的，一部分在首部、一部分在尾部，即 去除了中间的某部分，此时子数组的最大和 = 数组总和 - 中间那部分(最小子数组)的和
        """
        # total - 数组总和；max_sum - 最大子数组的和；cur_max_sum - 包含当前元素的最大子数组的和；
        # min_sum - 最小子数组的和；cur_min_sum - 包含当前元素的最小子数组的和
        total = max_sum = cur_max_sum = min_sum = cur_min_sum = nums[0]
        for num in nums[1:]:
            total += num
            cur_max_sum = max(cur_max_sum + num, num)
            max_sum = max(max_sum, cur_max_sum)
            cur_min_sum = min(cur_min_sum + num, num)
            min_sum = min(min_sum, cur_min_sum)
        # 考虑特殊情况：所有元素均为负数，此时的最小子数组就是原数组本身，total - min_sum = 0，max_sum = max(nums)
        # 若max_sum > 0，则说明存在正数
        return max(max_sum, total - min_sum) if max_sum > 0 else max_sum


if __name__ == '__main__':
    print(Solution().maxSubarraySumCircular(nums=[-3, -2, -3]))
