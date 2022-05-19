# -*- coding: UTF-8 -*-
"""
title: 数组中和为 0 的三个数
给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a ，b ，c ，使得 a + b + c = 0 ？请找出所有和为 0 且 不重复 的三元组。


示例 1：
输入：nums = [-1,0,1,2,-1,-4]
输出：[[-1,-1,2],[-1,0,1]]

示例 2：
输入：nums = []
输出：[]

示例 3：
输入：nums = [0]
输出：[]


提示：
0 <= nums.length <= 3000
-10^5 <= nums[i] <= 10^5
"""
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """排序 + 双指针"""
        n = len(nums)
        res = []
        if n < 3:
            return res
        nums = sorted(nums)
        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            j = i + 1
            k = n - 1
            target = -nums[i]
            while j < k:
                if j > i + 1 and nums[j] == nums[j - 1]:
                    j += 1
                    continue
                while j < k and nums[j] + nums[k] > target:
                    k -= 1
                if j < k and nums[j] + nums[k] == target:
                    res.append([nums[i], nums[j], nums[k]])
                j += 1
        return res


if __name__ == '__main__':
    print(Solution().threeSum([-1, 0, 1, 2, -1, -4]))
