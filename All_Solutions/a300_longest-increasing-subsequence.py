# -*- coding: UTF-8 -*-
"""
title: 最长递增子序列
Given an integer array nums, return the length of the longest strictly increasing subsequence.
A subsequence is a sequence that can be derived from an array by deleting some or no elements without changing the order of the remaining elements. For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].
subsequence 中的元素在原数组中不一定连续；而 subarray 中的元素在原数组中是连续的。

Example 1:
Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

Example 2:
Input: nums = [0,1,0,3,2,3]
Output: 4

Example 3:
Input: nums = [7,7,7,7,7,7,7]
Output: 1


Constraints:
1 <= nums.length <= 2500
-10^4 <= nums[i] <= 10^4

Follow up: Can you come up with an algorithm that runs in O(n log(n)) time complexity?
"""
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        动态规划。dp[i] 表示以第 i 个数字结尾的最长上升子序列(必须包含nums[i])的长度。
        状态转移方程：dp[i] = max(dp[j]) + 1 其中，0 <= j < i 且 nums[j] < nums[i]
        """
        dp = []
        for i in range(len(nums)):
            tmp_res = 0
            num_i = nums[i]
            for j in range(i - 1, -1, -1):
                if j + 1 <= tmp_res:
                    break
                if nums[j] < num_i:
                    tmp_res = max(tmp_res, dp[j])
            dp.append(tmp_res + 1)
        return max(dp)

    def lengthOfLIS_2(self, nums: List[int]) -> int:
        """
        贪心 + 二分查找。执行速度远快于上面。
        要使上升子序列尽可能的长，则需让序列上升得尽可能慢，因此希望每次在上升子序列最后加上的那个数尽可能的小。
        维护一个数组d，d[i] 是所有长度为i的上升子序列中，值最小的元素。
        在从前往后遍历nums的过程中，在升序的数组d中查找第一个大于等于当前num的下标i，假设数组d的长度为m，
        若下标i为0，则表示替换数组d中的第一个元素，此时数组d的长度不变；
        若下标i为m-1，则表示替换数组d中的最后一个元素，此时数组d的长度不变；
        若下标i为m，则表示在数组d的最后添加一个元素，此时数组d的长度加1。
        最后数组d的长度就是所求结果。
        注意：数组d并不是nums的最长递增子序列！只是在遍历过程中，通过替换元素的方式来尽量减小d[i]，使得数组d可以多增加元素。
        """
        d = []
        for num in nums:
            if not d or d[-1] < num:
                d.append(num)
                continue
            left, right = 0, len(d) - 1
            while left < right:
                mid = (left + right) >> 1
                # 查找第一个大于等于当前num的下标i
                if d[mid] >= num:
                    right = mid
                else:
                    left = mid + 1
            d[left] = num
        return len(d)


if __name__ == '__main__':
    print(Solution().lengthOfLIS_2([10, 9, 2, 5, 3, 7, 101, 18]))
