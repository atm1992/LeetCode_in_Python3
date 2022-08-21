# -*- coding: UTF-8 -*-
"""
title: 和等于 k 的最长子数组长度
Given an integer array nums and an integer k, return the maximum length of a subarray that sums to k. If there is not one, return 0 instead.


Example 1:
Input: nums = [1,-1,5,-2,3], k = 3
Output: 4
Explanation: The subarray [1, -1, 5, -2] sums to 3 and is the longest.

Example 2:
Input: nums = [-2,-1,2,1], k = 1
Output: 2
Explanation: The subarray [-1, 2] sums to 1 and is the longest.


Constraints:
1 <= nums.length <= 2 * 10^5
-10^4 <= nums[i] <= 10^4
-10^9 <= k <= 10^9
"""
from typing import List


class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        """前缀和 + 哈希表"""
        sum2idx = {0: 0}
        res = pre = 0
        for idx, num in enumerate(nums, 1):
            pre += num
            if pre - k in sum2idx:
                res = max(res, idx - sum2idx[pre - k])
            if pre not in sum2idx:
                sum2idx[pre] = idx
        return res


if __name__ == '__main__':
    print(Solution().maxSubArrayLen(nums=[1, -1, 5, -2, 3], k=3))
