# -*- coding: UTF-8 -*-
"""
title: 戳气球
You are given n balloons, indexed from 0 to n - 1. Each balloon is painted with a number on it represented by an array nums. You are asked to burst all the balloons.
If you burst the ith balloon, you will get nums[i - 1] * nums[i] * nums[i + 1] coins. If i - 1 or i + 1 goes out of bounds of the array, then treat it as if there is a balloon with a 1 painted on it.
Return the maximum coins you can collect by bursting the balloons wisely.


Example 1:
Input: nums = [3,1,5,8]
Output: 167
Explanation:
nums = [3,1,5,8] --> [3,5,8] --> [3,8] --> [8] --> []
coins =  3*1*5    +   3*5*8   +  1*3*8  + 1*8*1 = 167

Example 2:
Input: nums = [1,5]
Output: 10


Constraints:
n == nums.length
1 <= n <= 300
0 <= nums[i] <= 100
"""
from functools import lru_cache
from typing import List


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        """
        自顶向下(从整体到局部)的记忆化搜索
        戳气球的操作会导致两个气球从不相邻变成相邻，使得后续操作难以处理。所以可以考虑反向操作，将整个过程看作是每次添加一个气球，
        正向操作戳破最后一个气球的情况是：(i, k, j)，i/j是边界值1，可理解为不可戳(不存在的)两个气球，也就是说最后只剩一个气球k, 最后这次操作可以获得的金币数为 1 * nums[k] * 1
        所以，反向操作就是刚开始只添加一个气球k到开区间(i, j)，i/j的默认值为1，开区间的意思就是不能选择(戳破)i/j，此时可以获得的金币数为 1 * nums[k] * 1
        正向操作的倒数第二步是戳破倒数第二个气球(假设为m)，即 (i, m, k, j)，戳破气球m可获得的金币数为 1 * nums[m] * nums[k]，正向操作最后两步能获得总金币数为 1 * nums[m] * nums[k] + 1 * nums[k] * 1
        反向操作的第二步就是添加第二个气球(假设为m)，即 (i, m, k, j)，添加气球m可获得的金币数为 1 * nums[m] * nums[k]，反向操作前两步能获得总金币数为 1 * nums[k] * 1 + 1 * nums[m] * nums[k]
        反向操作的第三步就是添加第三个气球(假设为n)，即 (i, m, k, n, j)，添加气球n可获得的金币数为 nums[k] * nums[n] * 1，反向操作前三步能获得总金币数为 1 * nums[k] * 1 + 1 * nums[m] * nums[k] + nums[k] * nums[n] * 1
        此时可认为是 开区间(i, k, j) + 开区间(i, m, k) + 开区间(k, n, j)，所以最后所求的最大金币数就可理解为 max((i,k) + 1 * nums[k] * 1 + (k,j))
        注意：m、k、n 之间的顺序需要符合对应数值在nums中的顺序
        """
        # 为了方便处理边界值i/j，避免数组下标越界
        vals = [1] + nums + [1]

        # @lru_cache(maxsize=None)
        # def helper(left: int, right: int) -> int:
        #     # 开区间
        #     if left + 1 >= right:
        #         return 0
        #     res = 0
        #     for i in range(left + 1, right):
        #         # 要求的是整体的res最大，并不单单是选择最大的vals[i]
        #         res = max(res, helper(left, i) + vals[left] * vals[i] * vals[right] + helper(i, right))
        #     return res
        #
        # return helper(0, len(vals) - 1)

        n = len(vals)
        cache = [[-1] * n for _ in range(n)]

        def helper(left: int, right: int) -> int:
            # 开区间
            if left + 1 >= right:
                return 0
            if cache[left][right] != -1:
                return cache[left][right]
            res = 0
            for i in range(left + 1, right):
                # 要求的是整体的res最大，并不单单是选择最大的vals[i]
                res = max(res, helper(left, i) + vals[left] * vals[i] * vals[right] + helper(i, right))
            cache[left][right] = res
            return res

        return helper(0, n - 1)

    def maxCoins_2(self, nums: List[int]) -> int:
        """
        自底向上(从局部到整体)的动态规划。优于上面的方法
        假设 dp[i][j] 表示填满开区间(i, j)所能获得的最大金币数，边界条件为 i + 1 >= j 时，dp[i][j] = 0
        因此，状态转移方程为 dp[i][j] = max(dp[i][k] + vals[i] * vals[k] * vals[j] + dp[k][j])
        最终结果为 dp[0][len(vals) - 1]
        """
        # 为了方便处理边界值i/j，避免数组下标越界
        vals = [1] + nums + [1]
        n = len(vals)
        dp = [[0] * n for _ in range(n)]
        # 原始nums中的元素在vals中的下标范围为：1 ~ n-2，所以k需要能够取到 1 ~ n-2
        # 有两种遍历方式：
        # 1、i 从n-3到0，j 从i+2到n-1 或 n-1到i+2，k 必须从i+1到j-1
        # 2、j 从2到n-1，i 从0到j-2 或 j-2到0，k 必须从j-1到i+1
        for i in range(n - 3, -1, -1):
            for j in range(i + 2, n):
                tmp = 0
                for k in range(i + 1, j):
                    tmp = max(tmp, dp[i][k] + vals[i] * vals[k] * vals[j] + dp[k][j])
                dp[i][j] = tmp
        return dp[0][n - 1]


if __name__ == '__main__':
    print(Solution().maxCoins([3, 1, 5, 8]))
