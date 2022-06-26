# -*- coding: UTF-8 -*-
"""
title: 最长连续序列
给定一个未排序的整数数组 nums ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。


示例 1：
输入：nums = [100,4,200,1,3,2]
输出：4
解释：最长数字连续序列是 [1, 2, 3, 4]。它的长度为 4。

示例 2：
输入：nums = [0,3,7,2,5,8,4,6,0,1]
输出：9


提示：
0 <= nums.length <= 10^4
-10^9 <= nums[i] <= 10^9

进阶：可以设计并实现时间复杂度为 O(n) 的解决方案吗？
"""
from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """哈希表"""
        res = 0
        num_set = set(nums)
        n = len(nums)
        # 每个元素最多被访问2次，因此时间复杂度为O(2n)，也属于O(n)
        # 特例：[3,7,2,5,8,4,6,1,0]，除了0，其余元素都会被访问2次
        for num in num_set:
            if num - 1 not in num_set:
                tmp_res = 1
                while num + 1 in num_set:
                    tmp_res += 1
                    num += 1
                res = max(res, tmp_res)
                # 剪枝。若某个连续序列的长度超过原始序列长度的一半，则不可能还会有比它更长的连续序列了。
                if res >= (n + 1) // 2:
                    break
        return res


if __name__ == '__main__':
    print(Solution().longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))
