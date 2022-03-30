# -*- coding: UTF-8 -*-
"""
title: 乘积最大子数组
Given an integer array nums, find a contiguous non-empty subarray within the array that has the largest product, and return the product.
The test cases are generated so that the answer will fit in a 32-bit integer.
A subarray is a contiguous subsequence of the array.


Example 1:
Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.

Example 2:
Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.


Constraints:
1 <= nums.length <= 2 * 10^4
-10 <= nums[i] <= 10
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
"""
from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        """
        动态规划。
        假设f_max(i) 表示以第 i 个元素结尾的乘积最大子数组的乘积。则状态转移方程为 f_max(i) = max{f_max(i-1)*num_i, num_i}，
        不过，如果当前值num_i为负数，那么此时希望f(i-1)是一个尽可能小的负数，才能使得f(i-1) * num_i 尽可能大。
        因此需要分正负数进行讨论，除了记录以位置i-1结尾的最大值f_max(i-1)，还需要记录以位置i-1结尾的最小值f_min(i-1)，
        状态转移方程为：
        f_max(i) = max{f_max(i-1)*num_i, f_min(i-1)*num_i, num_i}
        f_min(i) = min{f_max(i-1)*num_i, f_min(i-1)*num_i, num_i}
        因为当前位置的状态只和前一个位置的状态有关，所以可以不用dp数组，而只用两个变量
        """
        # f_max 记录前一个位置的最大值，f_min 记录前一个位置的最小值
        res = f_min = f_max = nums[0]
        for num in nums[1:]:
            f_min, f_max = min(f_max * num, f_min * num, num), max(f_max * num, f_min * num, num)
            # 这里的res表示历史最大值，f_max表示当前位置最大值
            res = max(res, f_max)
        return res


if __name__ == '__main__':
    print(Solution().maxProduct([2,3,-2,4]))