# -*- coding: UTF-8 -*-
"""
title: 排序数组中只出现一次的数字
给定一个只包含整数的有序数组 nums ，每个元素都会出现两次，唯有一个数只会出现一次，请找出这个唯一的数字。


示例 1:
输入: nums = [1,1,2,3,3,4,4,8,8]
输出: 2

示例 2:
输入: nums =  [3,3,7,7,10,11,11]
输出: 10


提示:
1 <= nums.length <= 10^5
0 <= nums[i] <= 10^5

进阶: 采用的方案可以在 O(log n) 时间复杂度和 O(1) 空间复杂度中运行吗？
"""
from typing import List


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        """
        全数组的二分查找。
        假设只出现一次的那个数字的下标为i，则i之前的所有元素都满足：nums[j] == nums[j+1], j % 2 == 0；
        i之后的所有元素都满足：nums[j] == nums[j+1], j % 2 == 1。并且可以肯定的是 i % 2 == 0
        对于i左侧的j：
        j 为偶数时，判断nums[j] 与 nums[j+1]是否相等；j 为奇数时，判断nums[j-1] 与 nums[j]是否相等。
        j 为偶数时，j ^ 1 == j+1；j 为奇数时，j ^ 1 == j-1。
        所以，可简单判断 nums[j] 与 nums[j^1]是否相等，若相等，则left = mid + 1，向右继续查找。
        """
        left, right = 0, len(nums) - 1
        while left < right:
            # 因为循环条件为left < right，所以mid不可能等于right，也就意味着mid不可能等于len(nums) - 1
            # mid为0时，mid ^ 1 == 1，所以不用担心下标越界的问题
            mid = left + (right - left) // 2
            if nums[mid] == nums[mid ^ 1]:
                left = mid + 1
            else:
                right = mid
        return nums[left]

    def singleNonDuplicate_2(self, nums: List[int]) -> int:
        """
        偶数下标的二分查找。
        根据上面的论述，可以知道i一定是偶数，len(nums)一定是奇数。所以只需在[0, len(nums)-1]中的所有偶数中查找即可，因为i就在这些偶数中
        """
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            # 保证mid始终为偶数
            mid = (mid // 2) * 2
            if nums[mid] == nums[mid + 1]:
                # 保证left始终为偶数
                left = mid + 2
            else:
                # 保证right始终为偶数
                right = mid
        return nums[left]


if __name__ == '__main__':
    print(Solution().singleNonDuplicate(nums=[3, 3, 7, 7, 10, 11, 11]))
