# -*- coding: UTF-8 -*-
"""
title: 最接近的三数之和
Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.
Return the sum of the three integers.
You may assume that each input would have exactly one solution.


Example 1:
Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

Example 2:
Input: nums = [0,0,0], target = 1
Output: 0


Constraints:
3 <= nums.length <= 1000
-1000 <= nums[i] <= 1000
-10^4 <= target <= 10^4
"""
from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        min_gap = target - sum(nums[:3])
        n = len(nums)
        nums.sort()
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            j, k = i + 1, n - 1
            while j < k:
                tmp = nums[i] + nums[j] + nums[k]
                if tmp == target:
                    return target
                if abs(target - tmp) < abs(min_gap):
                    min_gap = target - tmp
                if tmp < target:
                    # 指针j向右移，跳过相等的元素
                    j0 = j + 1
                    while j0 < k and nums[j0] == nums[j]:
                        j0 += 1
                    j = j0
                else:
                    # 指针k向左移，跳过相等的元素
                    k0 = k - 1
                    while k0 > j and nums[k0] == nums[k]:
                        k0 -= 1
                    k = k0
        return target - min_gap


if __name__ == '__main__':
    print(Solution().threeSumClosest([0, 0, 0], 1))
