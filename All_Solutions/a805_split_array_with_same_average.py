# -*- coding: UTF-8 -*-
"""
title: 数组的均值分割
You are given an integer array nums.
You should move each element of nums into one of the two arrays A and B such that A and B are non-empty, and average(A) == average(B).
Return true if it is possible to achieve that and false otherwise.
Note that for an array arr, average(arr) is the sum of all the elements of arr over the length of arr.


Example 1:
Input: nums = [1,2,3,4,5,6,7,8]
Output: true
Explanation: We can split the array into [1,4,5,8] and [2,3,6,7], and both of them have an average of 4.5.

Example 2:
Input: nums = [3,1]
Output: false


Constraints:
1 <= nums.length <= 30
0 <= nums[i] <= 10^4
"""
from collections import defaultdict
from typing import List


class Solution:
    def splitArraySameAverage(self, nums: List[int]) -> bool:
        """
        动态规划（0-1背包）
        假设从n个元素中选出k个元素作为数组A，另外n-k个元素作为数组B，因为题目要求这两个数组的均值相等，即
        sum(A) / k = sum(B) / (n-k) ==> sum(A) * (n-k) = sum(B) * k ==> sum(A) * n = (sum(A) + sum(B)) * k = sum(nums) * k
        ==> sum(A) / k = sum(nums) / n = avg(nums) ==> sum(A) = k * avg(nums)
        由上可知，原问题转化成了0-1背包问题，从n个元素中选出k个元素，这k个元素之和要求等于k * avg(nums)
        dp[i] 表示从已遍历过的nums元素中取出i个元素，这i个元素之和的可能取值有哪些
        状态转移方程：dp[i] = dp[i-1] + nums[i]，将dp[i-1]中的所有可能取值都加上nums[i]，即可得到dp[i]中的所有可能取值
        只要能从dp[i]的可能取值中找到一个等于 sum(nums) * i / n 的取值，即可直接返回True
        """
        n, total = len(nums), sum(nums)
        # 剪枝。数组A和数组B这两个子数组中，一定存在一个子数组的长度小于等于n // 2，只需考虑较短的那个子数组
        max_size = n // 2
        # 剪枝。因为nums中的所有元素都是int，所以元素之和也一定是int，因此 sum(nums) * i 一定是 n 的整数倍，即 sum(nums) * i % n == 0
        # 若在[1, max_size]中不存在满足条件的子数组长度，则说明不存在符合题目要求的子数组
        if all(total * i % n for i in range(1, max_size + 1)):
            return False
        dp = defaultdict(set)
        # 长度为0的子数组，其和只可能为0
        dp[0].add(0)
        # 从前往后遍历nums，因此在dp[i]的可能取值中不会出现重复累加的情况，每个元素都只使用于一个大循环
        for num in nums:
            # 注意：这里需要逆序，若从长度1到长度max_size，则会重复累加当前num
            for i in range(max_size, 0, -1):
                for pre in dp[i - 1]:
                    cur = pre + num
                    # 使用乘法代替除法，是为避免浮点数导致的误差
                    if cur * n == total * i:
                        return True
                    dp[i].add(cur)
        return False
