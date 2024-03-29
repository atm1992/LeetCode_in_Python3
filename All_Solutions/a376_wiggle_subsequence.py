# -*- coding: UTF-8 -*-
"""
title: 摆动序列
A wiggle sequence is a sequence where the differences between successive numbers strictly alternate between positive and negative. The first difference (if one exists) may be either positive or negative. A sequence with one element and a sequence with two non-equal elements are trivially wiggle sequences.
    For example, [1, 7, 4, 9, 2, 5] is a wiggle sequence because the differences (6, -3, 5, -7, 3) alternate between positive and negative.
    In contrast, [1, 4, 7, 2, 5] and [1, 7, 4, 5, 5] are not wiggle sequences. The first is not because its first two differences are positive, and the second is not because its last difference is zero.
A subsequence is obtained by deleting some elements (possibly zero) from the original sequence, leaving the remaining elements in their original order.
Given an integer array nums, return the length of the longest wiggle subsequence of nums.


Example 1:
Input: nums = [1,7,4,9,2,5]
Output: 6
Explanation: The entire sequence is a wiggle sequence with differences (6, -3, 5, -7, 3).

Example 2:
Input: nums = [1,17,5,10,13,15,10,5,16,8]
Output: 7
Explanation: There are several subsequences that achieve this length.
One is [1, 17, 10, 13, 10, 16, 8] with differences (16, -7, 3, -3, 6, -8).

Example 3:
Input: nums = [1,2,3,4,5,6,7,8,9]
Output: 2


Constraints:
1 <= nums.length <= 1000
0 <= nums[i] <= 1000

Follow up: Could you solve this in O(n) time?
"""
from typing import List


class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        """
        动态规划
        假设up[i]表示在前i个元素中，以某个元素结尾的最长上升摆动序列的长度；down[i]表示在前i个元素中，以某个元素结尾的最长下降摆动序列的长度。
        计算up[i+1]时，要么维持up[i]，要么满足down[i] + 1的条件。要想让down[i] + 1，down[i]表示最后一个是下降，所以加1就需要在后面拼接一个上升，即 nums[i] <  nums[i+1]。
        计算down[i+1]时，要么维持down[i]，要么满足up[i] + 1的条件。要想让up[i] + 1，up[i]表示最后一个是上升，所以加1就需要在后面拼接一个下降，即 nums[i] >  nums[i+1]。
        初始值：只有一个元素时，既可以表示上升，也可以表示下降，即 up[0] = down[0] = 1
        """
        up = down = 1
        for i in range(1, len(nums)):
            # 上升
            if nums[i - 1] < nums[i]:
                up = max(up, down + 1)
            # 下降
            elif nums[i - 1] > nums[i]:
                down = max(down, up + 1)
        return max(up, down)


if __name__ == '__main__':
    print(Solution().wiggleMaxLength([1, 17, 5, 10, 13, 15, 10, 5, 16, 8]))
