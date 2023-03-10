# -*- coding: UTF-8 -*-
"""
title: 使数组和能被 P 整除
Given an array of positive integers nums, remove the smallest subarray (possibly empty) such that the sum of the remaining elements is divisible by p. It is not allowed to remove the whole array.
Return the length of the smallest subarray that you need to remove, or -1 if it's impossible.
A subarray is defined as a contiguous block of elements in the array.


Example 1:
Input: nums = [3,1,4,2], p = 6
Output: 1
Explanation: The sum of the elements in nums is 10, which is not divisible by 6. We can remove the subarray [4], and the sum of the remaining elements is 6, which is divisible by 6.

Example 2:
Input: nums = [6,3,5,2], p = 9
Output: 2
Explanation: We cannot remove a single element to get a sum divisible by 9. The best way is to remove the subarray [5,2], leaving us with [6,3] with sum 9.

Example 3:
Input: nums = [1,2,3], p = 3
Output: 0
Explanation: Here the sum is 6. which is already divisible by 3. Thus we do not need to remove anything.


Constraints:
1 <= nums.length <= 10^5
1 <= nums[i] <= 10^9
1 <= p <= 10^9
"""
from typing import List


class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        """前缀和 + 哈希表"""
        remain = sum(nums) % p
        if remain == 0:
            return 0
        # 找到满足以下条件的最短子数组：sum(子数组) % p == remain
        # sum(子数组) = pre_sum[j] - pre_sum[i]，pre_sum[j]就是当前前缀和，pre_sum[i]是之前计算过的前缀和，现在要从哈希表中查找是否存在想要的pre_sum[i]
        # (pre_sum[j] - pre_sum[i]) % p == remain  ——>  (pre_sum[j] - remain) % p == pre_sum[i]
        # 因此，哈希表中存储的所有pre_sum都需要先对p取余。为避免pre_sum[j] - remain为负数，大多数编程语言中的负数取余的结果都是负数，Python例外
        # 为统一各种语言，所以Python这里也用 (pre_sum[j] - remain + p) % p == pre_sum[i]
        res = len(nums)
        sum2idx = {0: -1}
        cur_sum = 0
        for i, num in enumerate(nums):
            cur_sum = (cur_sum + num) % p
            need_sum = (cur_sum - remain + p) % p
            if need_sum in sum2idx:
                res = min(res, i - sum2idx[need_sum])
                if res == 1:
                    break
            sum2idx[cur_sum] = i
        return res if res < len(nums) else -1


if __name__ == '__main__':
    print(Solution().minSubarray(nums=[6, 3, 5, 2], p=9))
