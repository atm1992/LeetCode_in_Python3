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
        """前缀和 + 哈希表优化"""
        res = 0
        # pre_sum 初始化为0，此时未累加任何元素
        pre_sum = 0
        pre2cnt = defaultdict(int)
        # 初始化。表示从头开始累加到当前元素的前缀和恰好等于k的这种情况
        pre2cnt[0] = 1
        # 因为是从前往后遍历nums，所以只需在pre2cnt中记录等于某个pre_sum的个数，而无需记录等于某个pre_sum的有哪些下标，因为那些下标一定都小于当前元素的下标
        for num in nums:
            pre_sum += num
            res += pre2cnt[pre_sum - k]
            pre2cnt[pre_sum] += 1
        return res


if __name__ == '__main__':
    print(Solution().subarraySum(nums=[1, 2, 3], k=3))
