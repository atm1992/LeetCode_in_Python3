# -*- coding: UTF-8 -*-
"""
title: 分割等和子集
给定一个非空的正整数数组 nums ，请判断能否将这些数字分成元素和相等的两部分。


示例 1：
输入：nums = [1,5,11,5]
输出：true
解释：nums 可以分割成 [1, 5, 5] 和 [11] 。

示例 2：
输入：nums = [1,2,3,5]
输出：false
解释：nums 不可以分为和相等的两部分


提示：
1 <= nums.length <= 200
1 <= nums[i] <= 100
"""
from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        """
        动态规划
        dp[i][j] 表示能否从nums中的前i+1个(i为元素下标)元素中选取若干个(可以是0个)元素组成子集，这个子集的和为j。j的取值范围：[0, target]
        对于当前元素i而言，可分为两种情况：
        选取：则 dp[i][j] 的值取决于 dp[i-1][j-nums[i]]
        不选取：则 dp[i][j] 的值取决于 dp[i-1][j]
        由于j-nums[i]需要大于等于0，所以只有在nums[i]<=j时，才允许选取当前元素i，此时的 dp[i][j] = dp[i-1][j-nums[i]] or dp[i-1][j]
        边界条件：
        在任意情况下，都可以选取0个元素，即 所有的dp[i][0]都为True
        初始值dp[0]：
        不选取nums[0]时，此时的子集和为0，即 dp[0][0] = True；选取nums[0]时，此时的子集和为nums[0]，即 dp[0][nums[0]] = True。其余情况下的dp[0]均为False
        """
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
        dp = [[True] + [False] * target for _ in range(n)]
        # 所有num 均小于 target
        dp[0][nums[0]] = True
        for i in range(1, n):
            # 所有的dp[i][0]都为True，无需计算
            for j in range(1, target + 1):
                if nums[i] <= j:
                    dp[i][j] = dp[i - 1][j - nums[i]] or dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j]
        return dp[n - 1][target]

    def canPartition_2(self, nums: List[int]) -> bool:
        """
        动态规划。优化方法一
        dp[i][j] 仅与 dp[i - 1][j - nums[i]]、dp[i - 1][j] 有关，可使用滚动数组的思想降低空间复杂度
        逆序遍历j，当 j >= nums[i] 时，dp[i][j] = dp[i - 1][j - nums[i]] or dp[i - 1][j] 可简写为 dp[j] = dp[j - nums[i]] or dp[j]，
        可进一步简写为 dp[j] |= dp[j - nums[i]]。
        当 j < nums[i] 时，dp[i][j] = dp[i - 1][j] 可简写为 dp[j] = dp[j]
        由上可知，当 j < nums[i] 时，其实可以不用继续计算了，逆序遍历j还能进一步降低运行时间，不过时间复杂度不变
        """
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
        dp = [True] + [False] * target
        dp[nums[0]] = True
        for num in nums[1:]:
            # 题目已知 1 <= nums[i]，即 num - 1 >= 0
            for j in range(target, num - 1, -1):
                dp[j] |= dp[j - num]
        return dp[target]


if __name__ == '__main__':
    print(Solution().canPartition_2([1, 5, 11, 5]))
