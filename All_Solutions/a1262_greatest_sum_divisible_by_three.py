# -*- coding: UTF-8 -*-
"""
title: 可被三整除的最大和
Given an array nums of integers, we need to find the maximum possible sum of elements of the array such that it is divisible by three.


Example 1:
Input: nums = [3,6,5,1,8]
Output: 18
Explanation: Pick numbers 3, 6, 1 and 8 their sum is 18 (maximum sum divisible by 3).

Example 2:
Input: nums = [4]
Output: 0
Explanation: Since 4 is not divisible by 3, do not pick any number.

Example 3:
Input: nums = [1,2,3,4,4]
Output: 12
Explanation: Pick numbers 1, 3, 4 and 4 their sum is 12 (maximum sum divisible by 3).


Constraints:
1 <= nums.length <= 4 * 10^4
1 <= nums[i] <= 10^4
"""
from typing import List


class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        """
        动态规划
        dp[i][j] 表示nums中的前i个(下标为i-1)元素中，余数为j的最大和。本题中的余数j可为0、1、2
        状态转移方程：若当前元素nums[i] % 3 == 1，则
        dp[i+1][0] = max(dp[i][0], dp[i][2] + nums[i])
        dp[i+1][1] = max(dp[i][1], dp[i][0] + nums[i])
        dp[i+1][2] = max(dp[i][2], dp[i][1] + nums[i])
        边界条件：
        dp[0] 表示没有选择任何元素，所以此时的最大和为0，0 % 3 == 0，所以 dp[0][0] = 0，dp[0][1] = dp[0][2] = float('-inf')
        从上面的状态转移方程可知，dp[i+1] 仅与 dp[i] 有关，所以可使用滚动数组的思想来降低空间复杂度
        """
        # 对于其它语言，float('-inf') 替换为 INT_MIN
        dp = [0, float('-inf'), float('-inf')]
        for num in nums:
            pre_0, pre_1, pre_2 = dp[0] + num, dp[1] + num, dp[2] + num
            if num % 3 == 0:
                dp[0] = max(dp[0], pre_0)
                dp[1] = max(dp[1], pre_1)
                dp[2] = max(dp[2], pre_2)
            elif num % 3 == 1:
                dp[0] = max(dp[0], pre_2)
                dp[1] = max(dp[1], pre_0)
                dp[2] = max(dp[2], pre_1)
            else:
                dp[0] = max(dp[0], pre_1)
                dp[1] = max(dp[1], pre_2)
                dp[2] = max(dp[2], pre_0)
        return dp[0]

    def maxSumDivThree_2(self, nums: List[int]) -> int:
        """
        动态规划。优化方法一
        方法一是根据num % 3的余数，来决定pre_0、pre_1、pre_2分别应该去dp[0]、dp[1]、dp[2]中的哪一个，
        对于每个元素num，pre_0、pre_1、pre_2 与 dp[0]、dp[1]、dp[2] 都是一对一的。

        其实还可根据pre_0 % 3、pre_1 % 3、pre_2 % 3的余数，自己决定应该去dp[0]、dp[1]、dp[2]中的哪一个，
        区别在于此时的pre_0、pre_1、pre_2 与 dp[0]、dp[1]、dp[2] 并不是一对一的。
        例如：对于nums中的第一个元素a，假设 a % 3 = 1，则：
        pre_0, pre_1, pre_2 = 0 + a, 0 + a, 0 + a
        此时，pre_0 % 3 = pre_1 % 3 = pre_2 % 3 = a % 3 = 1
        所以此时 pre_0、pre_1、pre_2 对应的都是dp[1]，此时并不会去更新dp[0]、dp[2]
        只有当之后pre_0、pre_1、pre_2中的某个或某几个的余数为2时，才会去更新dp[2]，在此之前，dp[2]始终是初始值0
        """
        # 注意：这里的dp初始值与方法一中的dp初始值不一样
        dp = [0] * 3
        for num in nums:
            pre_0, pre_1, pre_2 = dp[0] + num, dp[1] + num, dp[2] + num
            dp[pre_0 % 3] = max(dp[pre_0 % 3], pre_0)
            dp[pre_1 % 3] = max(dp[pre_1 % 3], pre_1)
            dp[pre_2 % 3] = max(dp[pre_2 % 3], pre_2)
        return dp[0]

    def maxSumDivThree_3(self, nums: List[int]) -> int:
        """
        动态规划。方法二的通用写法
        """
        k = 3
        dp = [0] * k
        tmp = [0] * k
        for num in nums:
            # 循环过程中，不能修改dp数组，避免取出的不是pre值，而是更新后的cur值
            for pre in dp:
                cur = pre + num
                # max() 中的之所以是tmp[cur % k]，而不是dp[cur % k]。是因为可能多个pre(pre_0、pre_1、pre_2)都对应的是tmp[cur % k]，
                # 即 pre_0 % k == pre_1 % k == pre_2 % k，但是 pre_0、pre_1、pre_2 并不相等，
                # 假设 pre_0 + num > pre_2 + num > 初始的tmp[cur % k]（即 dp[cur % k]），
                # 执行pre_0后，tmp[cur % k] = pre_0 + num
                # 若max() 中写的是dp[cur % k]，则执行pre_2后，tmp[cur % k] = (dp[cur % k], pre_2 + num) = pre_2 + num < pre_0 + num
                # 相当于执行pre_0后，tmp[cur % k] 变大了，但执行pre_2后，又变小了
                # 例如：nums = [3, 5], k = 3。
                # 若tmp[cur % k] = max(tmp[cur % k], cur)，则第一轮之后的dp结果：[3, 0, 0]，第二轮之后的dp结果：[3, 0, 8]
                # 若tmp[cur % k] = max(dp[cur % k], cur)，则第一轮之后的dp结果：[3, 0, 0]，第二轮之后的dp结果：[3, 0, 5]
                # 分析第一轮到第二轮的过程：
                # pre_0 = dp[0] = 3, 3 + 5 = 8 ——> dp[2]
                # pre_1 = dp[1] = 0, 0 + 5 = 5 ——> dp[2]
                # pre_2 = dp[2] = 0, 0 + 5 = 5 ——> dp[2]
                tmp[cur % k] = max(tmp[cur % k], cur)
            # 这样写，dp、tmp的id()始终是初始时的，不会新建数组
            dp[:] = tmp[:]
        return dp[0]


if __name__ == '__main__':
    print(Solution().maxSumDivThree_3([3, 5]))
