# -*- coding: UTF-8 -*-
"""
title: 长度最小的子数组
Given an array of positive integers nums and a positive integer target, return the minimal length of a contiguous subarray [numsl, numsl+1, ..., numsr-1, numsr] of which the sum is greater than or equal to target. If there is no such subarray, return 0 instead.


Example 1:
Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.

Example 2:
Input: target = 4, nums = [1,4,4]
Output: 1

Example 3:
Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0


Constraints:
1 <= target <= 10^9
1 <= nums.length <= 10^5
1 <= nums[i] <= 10^5

Follow up: If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(nlogn).
"""
from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """滑动窗口。时间复杂度为 O(n) """
        n = len(nums)
        res = n + 1
        start, end = 0, 0
        total = 0
        while end < n:
            total += nums[end]
            while total >= target:
                res = min(res, end - start + 1)
                total -= nums[start]
                start += 1
            end += 1
        # res 最大只能为 n
        return 0 if res > n else res

    def minSubArrayLen_2(self, target: int, nums: List[int]) -> int:
        """前缀和 + 二分查找。时间复杂度为 O(nlogn)
        额外创建一个数组 sums 用来存储数组 nums 的前缀和，其中 sums[i] 表示从 nums[0] 到 nums[i-1] 这前i个元素的总和。
        得到前缀和之后，对于每个开始下标 start，可通过二分查找得到大于或等于 target 的第一个下标 end，使得 sums[end] - sums[start - 1] ≥ target，
        并更新子数组的最小长度（此时子数组的长度为 end - (start - 1)）。
        因为题目保证了数组中每个元素都为正，所以前缀和一定是递增的，从而确保可以使用二分查找
        """

        def binary_search(nums: List[int], target: int) -> int:
            n = len(nums)
            left, right = 0, n - 1
            while left <= right:
                mid = (right - left) // 2 + left
                if nums[mid] >= target:
                    right = mid - 1
                else:
                    left = mid + 1
            return left

        n = len(nums)
        res = n + 1
        sums = [0] * (n + 1)
        for i in range(1, n + 1):
            sums[i] = sums[i - 1] + nums[i - 1]

        for i in range(1, n + 1):
            the_sum = target + sums[i - 1]
            # 在数组sums中二分查找第一个大于等于the_sum的元素下标
            end = binary_search(sums, the_sum)
            if end < len(sums):
                res = min(res, end - (i - 1))
        return 0 if res > n else res


if __name__ == '__main__':
    print(Solution().minSubArrayLen_2(target=15, nums=[1, 2, 3, 4, 5]))
