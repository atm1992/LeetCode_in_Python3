# -*- coding: UTF-8 -*-
"""
title: 将 x 减到 0 的最小操作数
You are given an integer array nums and an integer x. In one operation, you can either remove the leftmost or the rightmost element from the array nums and subtract its value from x. Note that this modifies the array for future operations.
Return the minimum number of operations to reduce x to exactly 0 if it is possible, otherwise, return -1.


Example 1:
Input: nums = [1,1,4,2,3], x = 5
Output: 2
Explanation: The optimal solution is to remove the last two elements to reduce x to zero.

Example 2:
Input: nums = [5,6,7,8,9], x = 4
Output: -1

Example 3:
Input: nums = [3,2,20,1,1,3], x = 10
Output: 5
Explanation: The optimal solution is to remove the last three elements and the first two elements (5 operations in total) to reduce x to zero.


Constraints:
1 <= nums.length <= 10^5
1 <= nums[i] <= 10^4
1 <= x <= 10^9
"""
from typing import List


class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        """前缀和 + 哈希表"""
        n = len(nums)
        sum2idx = {}
        res, l_sum, r_sum = n + 1, 0, 0
        for i in range(n):
            l_sum += nums[i]
            if l_sum >= x:
                if l_sum == x:
                    res = min(res, i + 1)
                break
            # 因为1 <= nums[i]，所以l_sum是单调递增的
            sum2idx[l_sum] = i + 1
        if l_sum < x:
            return -1
        for i in range(n - 1, -1, -1):
            r_sum += nums[i]
            if r_sum >= x:
                if r_sum == x:
                    res = min(res, n - i)
                break
            if x - r_sum in sum2idx:
                res = min(res, n - i + sum2idx[x - r_sum])
        return res if res < n + 1 else -1

    def minOperations_2(self, nums: List[int], x: int) -> int:
        """逆向思维 + 双指针。从nums中移除一个最长的子数组，使得剩余元素的和为x"""
        n = len(nums)
        target = sum(nums) - x
        if target < 0:
            return -1
        elif target == 0:
            return n
        res = -1
        left, sub_sum = 0, 0
        for right, num in enumerate(nums):
            sub_sum += num
            while sub_sum > target:
                sub_sum -= nums[left]
                left += 1
            if sub_sum == target:
                res = max(res, right - left + 1)
        return -1 if res == -1 else n - res


if __name__ == '__main__':
    print(Solution().minOperations(nums=[3, 2, 20, 1, 1, 3], x=10))
