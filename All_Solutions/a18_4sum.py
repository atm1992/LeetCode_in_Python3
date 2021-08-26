# -*- coding: UTF-8 -*-
"""
title: 四数之和。
Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:
0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.


Example 1:
Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

Example 2:
Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]


Constraints:
1 <= nums.length <= 200
-10^9 <= nums[i] <= 10^9
-10^9 <= target <= 10^9
"""
from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        """排序 + 双指针"""
        n = len(nums)
        if n < 4:
            return []
        nums.sort()
        res = []
        for a in range(n - 3):
            if a > 0 and nums[a] == nums[a - 1]:
                continue
            if nums[a] + nums[a + 1] + nums[a + 2] + nums[a + 3] > target:
                break
            if nums[a] + nums[n - 3] + nums[n - 2] + nums[n - 1] < target:
                continue
            for b in range(a + 1, n - 2):
                if b > a + 1 and nums[b] == nums[b - 1]:
                    continue
                target_ab = target - nums[a] - nums[b]
                if nums[b + 1] + nums[b + 2] > target_ab:
                    break
                if nums[n - 2] + nums[n - 1] < target_ab:
                    continue
                c, d = b + 1, n - 1
                while c < d:
                    if nums[c] + nums[d] == target_ab:
                        res.append([nums[a], nums[b], nums[c], nums[d]])
                    if nums[c] + nums[d] <= target_ab:
                        c0 = c + 1
                        while c0 < d and nums[c0] == nums[c]:
                            c0 += 1
                        c = c0
                    else:
                        d0 = d - 1
                        while c < d0 and nums[d0] == nums[d]:
                            d0 -= 1
                        d = d0
        return res


if __name__ == '__main__':
    nums = [1, 0, -1, 0, -2, 2]
    target = 0
    print(Solution().fourSum(nums, target))
