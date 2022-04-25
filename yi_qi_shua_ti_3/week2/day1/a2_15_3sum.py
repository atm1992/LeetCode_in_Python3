# -*- coding: UTF-8 -*-
"""
title: 三数之和。
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.


Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]

Example 2:
Input: nums = []
Output: []

Example 3:
Input: nums = [0]
Output: []


Constraints:
0 <= nums.length <= 3000
-10^5 <= nums[i] <= 10^5
"""
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """暴力破解。运行超时"""
        n = len(nums)
        if n < 3:
            return []
        res = set()
        for i in range(1, n):
            for j in range(i):
                target = 0 - nums[i] - nums[j]
                if target in (nums[:j] + nums[j + 1:i] + nums[i + 1:]):
                    res.add(tuple(sorted([target, nums[i], nums[j]])))
        return [list(item) for item in res]

    def threeSum_2(self, nums: List[int]) -> List[List[int]]:
        """排序 + 双指针"""
        n = len(nums)
        if n < 3:
            return []
        # list的sort方法是对已有列表直接操作，无返回值；而内建函数sorted方法会返回一个新的list，避免直接修改已有列表。默认升序
        nums = sorted(nums)
        res = []
        for i in range(n):
            # 若当前值等于上一次循环的值，则跳过。因为不能重复
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            j = i + 1
            k = n - 1
            target = -nums[i]
            while j < k:
                if j > i + 1 and nums[j] == nums[j - 1]:
                    j += 1
                    continue
                # 这里退出while循环只有两种情况：j==k 或 nums[j] + nums[k] <= target
                while j < k and nums[j] + nums[k] > target:
                    k -= 1
                if j < k and nums[j] + nums[k] == target:
                    res.append([nums[i], nums[j], nums[k]])
                j += 1
        return res


if __name__ == '__main__':
    print(Solution().threeSum([-1, 0, 1, 2, -1, -4]))
