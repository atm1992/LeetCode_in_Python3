# -*- coding: UTF-8 -*-
"""
title: 调整数组顺序使奇数位于偶数前面
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有奇数在数组的前半部分，所有偶数在数组的后半部分。


示例：
输入：nums = [1,2,3,4]
输出：[1,3,2,4]
注：[3,1,2,4] 也是正确的答案之一。


提示：
0 <= nums.length <= 50000
0 <= nums[i] <= 10000
"""
from typing import List


class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        """双指针"""
        left, right = 0, len(nums) - 1
        while left < right:
            while left < right and not nums[right] & 1:
                right -= 1
            while left < right and nums[left] & 1:
                left += 1
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        return nums


if __name__ == '__main__':
    print(Solution().exchange([1, 2, 3, 4]))
