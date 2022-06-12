# -*- coding: UTF-8 -*-
"""
title: 统计得分小于 K 的子数组数目
The score of an array is defined as the product of its sum and its length.
    For example, the score of [1, 2, 3, 4, 5] is (1 + 2 + 3 + 4 + 5) * 5 = 75.
Given a positive integer array nums and an integer k, return the number of non-empty subarrays of nums whose score is strictly less than k.
A subarray is a contiguous sequence of elements within an array.


Example 1:
Input: nums = [2,1,4,3,5], k = 10
Output: 6
Explanation:
The 6 subarrays having scores less than 10 are:
- [2] with score 2 * 1 = 2.
- [1] with score 1 * 1 = 1.
- [4] with score 4 * 1 = 4.
- [3] with score 3 * 1 = 3.
- [5] with score 5 * 1 = 5.
- [2,1] with score (2 + 1) * 2 = 6.
Note that subarrays such as [1,4] and [4,3,5] are not considered because their scores are 10 and 36 respectively, while we need scores strictly less than 10.

Example 2:
Input: nums = [1,1,1], k = 5
Output: 5
Explanation:
Every subarray except [1,1,1] has a score less than 5.
[1,1,1] has a score (1 + 1 + 1) * 3 = 9, which is greater than 5.
Thus, there are 5 subarrays having scores less than 5.


Constraints:
1 <= nums.length <= 10^5
1 <= nums[i] <= 10^5
1 <= k <= 10^15
"""
from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        """前缀和 + 二分查找"""
        pre_sum = [0]
        for num in nums:
            pre_sum.append(pre_sum[-1] + num)
        res = 0
        for i in range(1, len(pre_sum)):
            left, right = 0, i
            while left < right:
                mid = (left + right) // 2
                diff = (pre_sum[i] - pre_sum[mid]) * (i - mid)
                if diff < k:
                    right = mid
                else:
                    left = mid + 1
            res += i - left
        return res

    def countSubarrays_2(self, nums: List[int], k: int) -> int:
        """双指针。空间复杂度为O(1)"""
        res = total = left = 0
        for right, num in enumerate(nums):
            total += num
            # 因为所有num均为正数，所以total是单调递增的
            while total * (right - left + 1) >= k:
                total -= nums[left]
                left += 1
            res += right - left + 1
        return res


if __name__ == '__main__':
    print(Solution().countSubarrays(nums=[1, 1, 1], k=5))
