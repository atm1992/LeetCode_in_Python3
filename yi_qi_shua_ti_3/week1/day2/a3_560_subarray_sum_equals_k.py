# -*- coding: UTF-8 -*-
"""
title: 和为 K 的子数组
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.
A subarray is a contiguous part of an array.

Example 1:
Input: nums = [1,1,1], k = 2
Output: 2

Example 2:
Input: nums = [1,2,3], k = 3
Output: 2


Constraints:
1 <= nums.length <= 2 * 10^4
-1000 <= nums[i] <= 1000
-10^7 <= k <= 10^7
"""
from collections import defaultdict
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """枚举。超时"""
        res = 0
        for i in range(len(nums)):
            total = 0
            # 对于每个i，倒序枚举所有的j来判断是否符合条件
            for j in range(i, -1, -1):
                total += nums[j]
                if total == k:
                    res += 1
        return res

    def subarraySum_2(self, nums: List[int], k: int) -> int:
        """前缀和 + 哈希表优化"""
        res = 0
        # 记录当前i之前的前缀和，0 ~ i-1
        pre_sum = 0
        pre2cnt = defaultdict(int)
        # 初始化。表示从0~i的前缀和恰好等于k，需要把这种情况算入res
        pre2cnt[0] = 1
        # 因为i是从前往后遍历，所以只需在pre2cnt中记录等于某个pre_sum的个数，而无需记录等于某个pre_sum的所有下标，因为这些下标一定都是小于i的
        for i in range(len(nums)):
            pre_sum += nums[i]
            res += pre2cnt[pre_sum - k]
            pre2cnt[pre_sum] += 1
        return res


if __name__ == '__main__':
    print(Solution().subarraySum_2(nums=[1, 2, 3], k=3))
