# -*- coding: UTF-8 -*-
"""
title: 最大宽度坡
A ramp in an integer array nums is a pair (i, j) for which i < j and nums[i] <= nums[j]. The width of such a ramp is j - i.
Given an integer array nums, return the maximum width of a ramp in nums. If there is no ramp in nums, return 0.


Example 1:
Input: nums = [6,0,8,2,1,5]
Output: 4
Explanation: The maximum width ramp is achieved at (i, j) = (1, 5): nums[1] = 0 and nums[5] = 5.

Example 2:
Input: nums = [9,8,1,0,1,9,4,0,4,1]
Output: 7
Explanation: The maximum width ramp is achieved at (i, j) = (2, 9): nums[2] = 1 and nums[9] = 1.


Constraints:
2 <= nums.length <= 5 * 10^4
0 <= nums[i] <= 5 * 10^4
"""
from typing import List


class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        """排序"""
        n = min_idx = len(nums)
        res = 0
        # 对元素下标0 ~ n-1排序，根据元素值nums[i]升序
        for i in sorted(range(n), key=lambda i: nums[i]):
            res = max(res, i - min_idx)
            # 记录当前最小的下标，for循环遍历过程中，元素值nums[i]是逐渐增大的，所以元素值的大小关系肯定是符合要求的，因此只需让下标之差尽量大
            min_idx = min(min_idx, i)
        return res


if __name__ == '__main__':
    print(Solution().maxWidthRamp([9, 8, 1, 0, 1, 9, 4, 0, 4, 1]))
