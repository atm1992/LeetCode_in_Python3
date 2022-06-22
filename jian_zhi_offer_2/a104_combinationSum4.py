# -*- coding: UTF-8 -*-
"""
title: 排列的数目
给定一个由 不同 正整数组成的数组 nums ，和一个目标整数 target 。请从 nums 中找出并返回总和为 target 的元素组合的个数。数组中的数字可以在一次排列中出现任意次，但是顺序不同的序列被视作不同的组合。
题目数据保证答案符合 32 位整数范围。


示例 1：
输入：nums = [1,2,3], target = 4
输出：7
解释：
所有可能的组合为：
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)
请注意，顺序不同的序列被视作不同的组合。

示例 2：
输入：nums = [9], target = 3
输出：0


提示：
1 <= nums.length <= 200
1 <= nums[i] <= 1000
nums 中的所有元素 互不相同
1 <= target <= 1000

进阶：如果给定的数组中含有负数会发生什么？问题会产生何种变化？如果允许负数出现，需要向题目中添加哪些限制条件？
answer：如果给定的数组中含有负数，则会导致出现无限长度的排列。因为只要存在一个总和为0的组合，那么这个组合可以在所有的排列中重复任意次。
如果允许负数出现，则必须限制排列的最大长度，避免出现无限长度的排列，这样才能计算出排列数。
"""
from typing import List


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        """
        动态规划
        因为顺序不同的序列被视作不同的组合，所以其实是个排列问题。
        dp[i] 表示组合总和为i的不同组合个数，最终要计算的是 dp[target]
        状态转移方程：如果存在一种排列，其元素之和等于 i，则该排列的最后一个元素一定是数组nums中的一个元素。假设该排列的最后一个元素是num，
        则一定有 num <= i，对于元素之和等于 i−num 的每一种排列，在最后添加 num 之后，即可得到一个元素之和等于 i 的排列，
        所以 dp[i] = sum(dp[i-num])，遍历nums中所有小于等于i的num
        边界条件：dp[0] = 1，不选取任何元素时，组合总和为0
        """
        nums.sort()
        dp = [1] + [0] * target
        for i in range(1, target + 1):
            for num in nums:
                if num > i:
                    break
                dp[i] += dp[i - num]
        return dp[-1]


if __name__ == '__main__':
    print(Solution().combinationSum4(nums=[1, 2, 3], target=4))
