# -*- coding: UTF-8 -*-
"""
title: 全 0 子数组的数目
Given an integer array nums, return the number of subarrays filled with 0.
A subarray is a contiguous non-empty sequence of elements within an array.


Example 1:
Input: nums = [1,3,0,0,2,0,0,4]
Output: 6
Explanation:
There are 4 occurrences of [0] as a subarray.
There are 2 occurrences of [0,0] as a subarray.
There is no occurrence of a subarray with a size more than 2 filled with 0. Therefore, we return 6.

Example 2:
Input: nums = [0,0,0,2,0,0]
Output: 9
Explanation:
There are 5 occurrences of [0] as a subarray.
There are 3 occurrences of [0,0] as a subarray.
There is 1 occurrence of [0,0,0] as a subarray.
There is no occurrence of a subarray with a size more than 3 filled with 0. Therefore, we return 9.

Example 3:
Input: nums = [2,10,2019]
Output: 0
Explanation: There is no subarray filled with 0. Therefore, we return 0.


Constraints:
1 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9
"""
from typing import List


class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        """动态规划。dp[i] 表示以元素i结尾的全0子数组的个数。若元素i不等于0，则当前全0子数组的个数为0"""
        res = pre = 0
        for num in nums:
            if num == 0:
                pre += 1
                res += pre
            else:
                pre = 0
        return res


if __name__ == '__main__':
    print(Solution().zeroFilledSubarray(nums=[0, 0, 0, 2, 0, 0]))
