# -*- coding: utf-8 -*-
# @date: 2023/4/10
# @author: liuquan
"""
title: 等值距离和
You are given a 0-indexed integer array nums. There exists an array arr of length nums.length, where arr[i] is the sum of |i - j| over all j such that nums[j] == nums[i] and j != i. If there is no such j, set arr[i] to be 0.
Return the array arr.


Example 1:
Input: nums = [1,3,1,1,2]
Output: [5,0,3,4,0]
Explanation:
When i = 0, nums[0] == nums[2] and nums[0] == nums[3]. Therefore, arr[0] = |0 - 2| + |0 - 3| = 5.
When i = 1, arr[1] = 0 because there is no other index with value 3.
When i = 2, nums[2] == nums[0] and nums[2] == nums[3]. Therefore, arr[2] = |2 - 0| + |2 - 3| = 3.
When i = 3, nums[3] == nums[0] and nums[3] == nums[2]. Therefore, arr[3] = |3 - 0| + |3 - 2| = 4.
When i = 4, arr[4] = 0 because there is no other index with value 2.

Example 2:
Input: nums = [0,5,3]
Output: [0,0,0]
Explanation: Since each element in nums is distinct, arr[i] = 0 for all i.


Constraints:
1 <= nums.length <= 10^5
0 <= nums[i] <= 10^9
"""
from collections import defaultdict
from itertools import accumulate
from typing import List


class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        """
        分组 + 前缀和优化。直接枚举各个分组会超时
        """
        res = [0] * len(nums)
        num2idxs = defaultdict(list)
        for i, num in enumerate(nums):
            num2idxs[num].append(i)
        for idxs in num2idxs.values():
            n = len(idxs)
            if n < 2:
                continue
            pre_sum = list(accumulate(idxs, initial=0))
            for j, idx in enumerate(idxs):
                # 将idx左边的所有idx通过加1操作都变成idx，可参考LeetCode题2602. 使数组元素全部相等的最少操作次数
                # 左边有j个下标，这j个下标之和为pre_sum[j]，因此差值为 idx * j - pre_sum[j]
                left = idx * j - pre_sum[j]
                right = pre_sum[n] - pre_sum[j] - idx * (n - j)
                res[idx] = left + right
        return res


if __name__ == '__main__':
    print(Solution().distance(nums=[1, 3, 1, 1, 2]))
