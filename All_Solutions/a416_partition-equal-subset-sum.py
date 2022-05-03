# -*- coding: UTF-8 -*-
"""
title: 分割等和子集
Given a non-empty array nums containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.


Example 1:
Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].

Example 2:
Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.


Constraints:
1 <= nums.length <= 200
1 <= nums[i] <= 100
"""
from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        """动态规划"""
        n = len(nums)
        if n < 2:
            return False
        total = sum(nums)
        if total & 1:
            return False
        target = total >> 1
        max_num = max(nums)
        if max_num > target:
            return False
        elif max_num == target:
            return True
        # dp二维数组。dp[i][j] 表示能否从nums中的前i个元素中选取若干个元素(可以是0个)组成子集，该子集的和为j。
        # 初始值：选取0个元素，子集的和则为0，所以所有的 dp[i][0] 均为True；
        # 对于dp[0]，不选取当前元素，则子集的和为0，即 dp[0][0] = True；选取当前元素，则子集的和为nums[0]，即 dp[0][nums[0]] = True；其余情况均为False
        dp = [[False] * (target + 1) for _ in range(n)]
        # 因为max_num > target的情况，前面已经排除了，所以nums[0]不可能大于target
        dp[0][nums[0]] = True
        for i in range(n):
            dp[i][0] = True
        # 对于每个元素而言，都只有两种情况，选取 或 不选取。
        # 选取当前元素i，则 dp[i][j] = dp[i-1][j-nums[i]]
        # 不选取当前元素i，则 dp[i][j] = dp[i-1][j]
        # 另外，由于 j-nums[i] 必须大于等于0，所以在选取当前元素i时，需要判断j 与 nums[i]之间的大小关系
        # 若nums[i]<=j，则可以选取当前元素i；若nums[i]>j，则不能选取当前元素i
        for i in range(1, n):
            # 因为所有的 dp[i][0] 均为True，所以从1开始计算
            for j in range(1, target + 1):
                if nums[i] <= j:
                    dp[i][j] = dp[i - 1][j] | dp[i - 1][j - nums[i]]
                else:
                    dp[i][j] = dp[i - 1][j]
        return dp[n - 1][target]

    def canPartition_2(self, nums: List[int]) -> bool:
        """
        动态规划
        由上可知，dp[i] 仅与 dp[i-1] 有关，所以可将二维dp数组转化为一维数组。
        不过需要注意的是，j 需要从target计算到1，因为 j - nums[i] < j，若从1计算到target，则在计算dp[i][j]时使用的是dp[i][j - nums[i]]，而不是dp[i - 1][j - nums[i]]
        使用一维数组，有个好处就是，j 其实只需从target计算到nums[i]，因为只有在nums[i] <= j <= target的范围内，才会使用到dp[i - 1][j - nums[i]]，
        其余情况下，dp[i][j] 直接等于 dp[i - 1][j]，也就意味着无需计算了。
        而且使用一维数组的时候，不需要关心 i 了
        """
        n = len(nums)
        if n < 2:
            return False
        total = sum(nums)
        if total & 1:
            return False
        max_num = max(nums)
        target = total >> 1
        if max_num > target:
            return False
        elif max_num == target:
            return True
        dp = [False] * (target + 1)
        dp[0] = True
        dp[nums[0]] = True
        for num in nums[1:]:
            # 1 <= nums[i]，即 num - 1 >= 0
            for j in range(target, num - 1, -1):
                dp[j] |= dp[j - num]
        return dp[target]


if __name__ == '__main__':
    print(Solution().canPartition_2([1, 2, 3, 5]))
