# -*- coding: UTF-8 -*-
"""
title: 递增的三元子序列
Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.


Example 1:
Input: nums = [1,2,3,4,5]
Output: true
Explanation: Any triplet where i < j < k is valid.

Example 2:
Input: nums = [5,4,3,2,1]
Output: false
Explanation: No triplet exists.

Example 3:
Input: nums = [2,1,5,0,4,6]
Output: true
Explanation: The triplet (3, 4, 5) is valid because nums[3] == 0 < nums[4] == 4 < nums[5] == 6.


Constraints:
1 <= nums.length <= 5 * 10^5
-2^31 <= nums[i] <= 2^31 - 1

Follow up: Could you implement a solution that runs in O(n) time complexity and O(1) space complexity?
"""
from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        """双向遍历。使用两个数组left_min、right_max分别记录从左侧到当前下标的最小值 以及 从右侧到当前下标的最大值"""
        n = len(nums)
        if n < 3:
            return False
        left_min, right_max = nums.copy(), nums.copy()
        for i in range(1, n):
            left_min[i] = min(left_min[i - 1:i + 1])
            right_max[n - i - 1] = max(right_max[n - i - 1:n - i + 1])
        for i in range(1, n - 1):
            if left_min[i - 1] < nums[i] < right_max[i + 1]:
                return True
        return False

    def increasingTriplet_2(self, nums: List[int]) -> bool:
        """贪心。题300是此题的升级版"""
        n = len(nums)
        if n < 3:
            return False
        first, second = nums[0], float('inf')
        for i in range(1, n):
            num = nums[i]
            # 尽可能的让first、second越小，这样才更有可能在后面遇到满足 first < second < num 的num
            # 注意：return True 时的first、second，虽然满足nums[i] < nums[j]，但不一定满足i < j
            # 以 [2,5,0,6] 为例：first 初始时为2，然后second更新为5，接着first被更新为0，遇到6时，return True
            # 虽然5的下标为1，0的下标为2，但是我们知道之前存在过下标小于1的某个数，满足小于5的条件
            if num < first:
                first = num
            elif first < num < second:
                second = num
            elif second < num:
                return True
        return False


if __name__ == '__main__':
    print(Solution().increasingTriplet(nums=[1, 2, 3, 4, 5]))
