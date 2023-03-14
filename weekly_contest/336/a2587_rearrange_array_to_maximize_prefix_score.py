# -*- coding: UTF-8 -*-
"""
title: 重排数组以得到最大前缀分数
You are given a 0-indexed integer array nums. You can rearrange the elements of nums to any order (including the given order).
Let prefix be the array containing the prefix sums of nums after rearranging it. In other words, prefix[i] is the sum of the elements from 0 to i in nums after rearranging it. The score of nums is the number of positive integers in the array prefix.
Return the maximum score you can achieve.


Example 1:
Input: nums = [2,-1,0,1,-3,3,-3]
Output: 6
Explanation: We can rearrange the array into nums = [2,3,1,-1,-3,0,-3].
prefix = [2,5,6,5,2,2,-1], so the score is 6.
It can be shown that 6 is the maximum score we can obtain.

Example 2:
Input: nums = [-2,-3,0]
Output: 0
Explanation: Any rearrangement of the array will result in a score of 0.


Constraints:
1 <= nums.length <= 10^5
-10^6 <= nums[i] <= 10^6
"""
from typing import List


class Solution:
    def maxScore(self, nums: List[int]) -> int:
        """排序 + 贪心"""
        nums.sort(reverse=True)
        res, pre_sum = 0, 0
        for num in nums:
            pre_sum += num
            if pre_sum > 0:
                res += 1
            else:
                break
        return res


if __name__ == '__main__':
    print(Solution().maxScore(nums=[2, -1, 0, 1, -3, 3, -3]))
