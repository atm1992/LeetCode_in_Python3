# -*- coding: UTF-8 -*-
"""
title: 最大连续 1 的个数
Given a binary array nums, return the maximum number of consecutive 1's in the array.


Example 1:
Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.

Example 2:
Input: nums = [1,0,1,1,0,1]
Output: 2


Constraints:
1 <= nums.length <= 10^5
nums[i] is either 0 or 1.
"""
from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        """贪心"""
        res = tmp = 0
        for num in nums:
            tmp = tmp + 1 if num else 0
            res = max(res, tmp)
        return res


if __name__ == '__main__':
    print(Solution().findMaxConsecutiveOnes(nums=[1, 0, 1, 1, 0, 1]))
