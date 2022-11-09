# -*- coding: UTF-8 -*-
"""
title: 找出第 K 小的数对距离
The distance of a pair of integers a and b is defined as the absolute difference between a and b.
Given an integer array nums and an integer k, return the kth smallest distance among all the pairs nums[i] and nums[j] where 0 <= i < j < nums.length.


Example 1:
Input: nums = [1,3,1], k = 1
Output: 0
Explanation: Here are all the pairs:
(1,3) -> 2
(1,1) -> 0
(3,1) -> 2
Then the 1st smallest distance pair is (1,1), and its distance is 0.

Example 2:
Input: nums = [1,1,1], k = 2
Output: 0

Example 3:
Input: nums = [1,6,1], k = 3
Output: 5


Constraints:
n == nums.length
2 <= n <= 10^4
0 <= nums[i] <= 10^6
1 <= k <= n * (n-1)/2
"""
from typing import List


class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        """排序 + 二分查找 + 双指针"""

        def check(dist: int) -> int:
            """使用双指针统计距离小于等于dist的数对数量"""
            cnt = i = 0
            for j, num in enumerate(nums):
                # 退出此while循环时，num - nums[i] <= dist
                while num - nums[i] > dist:
                    i += 1
                # 下标范围[i, j]内的数对数量为 j - i，为避免重复统计，每次都是固定数对的右端点下标j，因为每次for循环，j都会加1，即 每次for循环中的j都是不同的，从而保证了不重复
                # (nums[i], nums[j])、(nums[i+1], nums[j])、……、(nums[j-1], nums[j])。
                cnt += j - i
            return cnt

        nums.sort()
        left, right = 0, nums[-1] - nums[0]
        # 第 K 小的数对距离一定在 [left, right] 范围内
        while left < right:
            mid = (left + right) >> 1
            if check(mid) >= k:
                right = mid
            else:
                left = mid + 1
        return left


if __name__ == '__main__':
    print(Solution().smallestDistancePair(nums=[1, 6, 1], k=3))
