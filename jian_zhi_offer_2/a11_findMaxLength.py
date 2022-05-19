# -*- coding: UTF-8 -*-
"""
title: 0 和 1 个数相同的子数组
给定一个二进制数组 nums , 找到含有相同数量的 0 和 1 的最长连续子数组，并返回该子数组的长度。


示例 1：
输入: nums = [0,1]
输出: 2
说明: [0, 1] 是具有相同数量 0 和 1 的最长连续子数组。

示例 2：
输入: nums = [0,1,0]
输出: 2
说明: [0, 1] (或 [1, 0]) 是具有相同数量 0 和 1 的最长连续子数组。


提示：
1 <= nums.length <= 10^5
nums[i] 不是 0 就是 1
"""
from collections import defaultdict
from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        """前缀和 + 哈希表。将数组中的0视作-1，从而将原问题转换为求元素和为0的最长连续子数组"""
        res = 0
        pre_sum = 0
        # 存储各个不同pre_sum第一次出现时的下标
        pre2idx = defaultdict(int)
        pre2idx[0] = -1
        for idx, num in enumerate(nums):
            pre_sum += 1 if num == 1 else -1
            if pre_sum in pre2idx:
                res = max(res, idx - pre2idx[pre_sum])
            else:
                pre2idx[pre_sum] = idx
        return res


if __name__ == '__main__':
    print(Solution().findMaxLength(nums=[0, 1, 1, 1, 0, 0]))
