# -*- coding: UTF-8 -*-
"""
title: 乘积小于 K 的子数组
给定一个正整数数组 nums和整数 k ，请找出该数组内乘积小于 k 的连续的子数组的个数。


示例 1:
输入: nums = [10,5,2,6], k = 100
输出: 8
解释: 8 个乘积小于 100 的子数组分别为: [10], [5], [2], [6], [10,5], [5,2], [2,6], [5,2,6]。
需要注意的是 [10,5,2] 并不是乘积小于100的子数组。

示例 2:
输入: nums = [1,2,3], k = 0
输出: 0


提示: 
1 <= nums.length <= 3 * 10^4
1 <= nums[i] <= 1000
0 <= k <= 10^6
"""
from typing import List


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        """滑动窗口"""
        if k in [0, 1]:
            return 0
        res, start, product = 0, 0, 1
        # 不断遍历子数组的结尾元素end
        for end, num in enumerate(nums):
            product *= num
            # 这里不用判断start <= end，因为start == end+1时，product == 1，此时不会再进入while循环，因为k > 1
            while product >= k:
                product //= nums[start]
                start += 1
            # 上面退出while循环时，要么是 start == end+1，此时product == 1；要么是start <= end，且product < k
            # end - start + 1 表示以end结尾的所有子数组个数，因为既然以start起始的所有元素乘积都小于k，那么start ~ end之间的任一元素均可作为起始元素
            res += end - start + 1
        return res


if __name__ == '__main__':
    print(Solution().numSubarrayProductLessThanK(nums=[10, 5, 2, 6], k=100))
