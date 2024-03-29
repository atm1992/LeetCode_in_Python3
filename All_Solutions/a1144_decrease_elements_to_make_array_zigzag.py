# -*- coding: UTF-8 -*-
"""
title: 递减元素使数组呈锯齿状
Given an array nums of integers, a move consists of choosing any element and decreasing it by 1.
An array A is a zigzag array if either:
    Every even-indexed element is greater than adjacent elements, ie. A[0] > A[1] < A[2] > A[3] < A[4] > ...
    OR, every odd-indexed element is greater than adjacent elements, ie. A[0] < A[1] > A[2] < A[3] > A[4] < ...
Return the minimum number of moves to transform the given array nums into a zigzag array.


Example 1:
Input: nums = [1,2,3]
Output: 2
Explanation: We can decrease 2 to 0 or 3 to 1.

Example 2:
Input: nums = [9,6,1,6,2]
Output: 4


Constraints:
1 <= nums.length <= 1000
1 <= nums[i] <= 1000
"""
from typing import List


class Solution:
    def movesToMakeZigzag(self, nums: List[int]) -> int:
        """
        贪心。分别计算转换为第一种情况的锯齿数组所需的最小操作次数 和 转换为第二种情况的锯齿数组所需的最小操作次数，两者取较小值即可
        只减小奇数位或只减小偶数位。若在减小奇数位的同时，又去减小偶数位，只会画蛇添足，使得操作次数变大，不可能是最小操作次数
        """

        def helper(start_idx: int) -> int:
            res, n = 0, len(nums)
            for i in range(start_idx, n, 2):
                diff = 0
                # 题目要求的是只能减小数字，所以只能通过减小nums[i]，使其满足 nums[i-1] > nums[i] < nums[i+1]
                if i - 1 >= 0:
                    diff = max(diff, nums[i] - nums[i - 1] + 1)
                if i + 1 < n:
                    diff = max(diff, nums[i] - nums[i + 1] + 1)
                res += diff
            return res

        return min(helper(0), helper(1))

    def movesToMakeZigzag_2(self, nums: List[int]) -> int:
        """贪心。一次遍历"""
        res, n = [0, 0], len(nums)
        for i, num in enumerate(nums):
            # 通过减小num，使其满足 left > nums[i] < right
            # 1 <= nums[i] <= 1000
            left = nums[i - 1] if i - 1 >= 0 else 1001
            right = nums[i + 1] if i + 1 < n else 1001
            res[i % 2] += max(0, num - min(left, right) + 1)
        return min(res)


if __name__ == '__main__':
    print(Solution().movesToMakeZigzag(nums=[9, 6, 1, 6, 2]))
