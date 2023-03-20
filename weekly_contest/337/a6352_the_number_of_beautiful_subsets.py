# -*- coding: UTF-8 -*-
"""
title: 美丽子集的数目
You are given an array nums of positive integers and a positive integer k.
A subset of nums is beautiful if it does not contain two integers with an absolute difference equal to k.
Return the number of non-empty beautiful subsets of the array nums.
A subset of nums is an array that can be obtained by deleting some (possibly none) elements from nums. Two subsets are different if and only if the chosen indices to delete are different.


Example 1:
Input: nums = [2,4,6], k = 2
Output: 4
Explanation: The beautiful subsets of the array nums are: [2], [4], [6], [2, 6].
It can be proved that there are only 4 beautiful subsets in the array [2,4,6].

Example 2:
Input: nums = [1], k = 1
Output: 1
Explanation: The beautiful subset of the array nums is [1].
It can be proved that there is only 1 beautiful subset in the array [1].


Constraints:
1 <= nums.length <= 20
1 <= nums[i], k <= 1000
"""
from collections import defaultdict, Counter
from typing import List


class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        """回溯。时间复杂度为 O(2^n)"""
        # 去掉空集的情况
        res = -1
        n = len(nums)
        # 注意：这里不能用set，因为nums中可能存在值相同的元素，之后在恢复现场时，set.remove() 会报错
        num2cnt = defaultdict(int)

        def dfs(i: int) -> None:
            if i == n:
                nonlocal res
                res += 1
                return
            # 跳过当前元素
            dfs(i + 1)
            # 若满足条件，则可选择当前元素
            num = nums[i]
            # 注意：不能写成 num-k not in num2cnt，因为恢复现场时，可能会把num2cnt[num-k]减到0，但此时num-k仍在num2cnt中
            if num2cnt[num - k] == 0 and num2cnt[num + k] == 0:
                num2cnt[num] += 1
                dfs(i + 1)
                # 恢复现场
                num2cnt[num] -= 1

        dfs(0)
        return res

    def beautifulSubsets_2(self, nums: List[int], k: int) -> int:
        """
        分组动态规划。时间复杂度为 O(nlogn)，主要是因为排序。类似于LeetCode题198-打家劫舍
        只有当两个元素对k取余的结果相同时，这两个元素才有可能相差k。因此可以根据余数进行分组，不同组之间互不影响，所以不同组的结果可以使用乘法原理
        对于同一组内，先进行升序，这样一来，只有相邻的两个元素之间才有可能会相差k
        令dp[i]表示同余数组内前i个元素所组成的美丽子集的数目
        状态转移方程：
        1、若nums[i] - nums[i-1] = k，则nums[i]与nums[i-1]不能同时选
            1.1、若选择nums[i]，则有 2^cnt[i] - 1 种选法(去掉了一个都不选的情况)，此时的 dp[i] = (2^cnt[i] - 1) * dp[i-2]
            1.2、若选择nums[i-1]，则对应的是nums[i]一个都不选的情况，此时的 dp[i] = 1 * dp[i-1]
            所以此时的 dp[i] = (2^cnt[i] - 1) * dp[i-2] + dp[i-1]
        2、若nums[i] - nums[i-1] != k，则nums[i]与nums[i-1]可以同时选，此时的nums[i]有 2^cnt[i] 种选法(包括一个都不选的情况)，此时的 dp[i] = 2^cnt[i] * dp[i-1]
        综上，可以发现，dp[i] 只和 dp[i-1]、dp[i-2] 相关，因此可以只使用两个变量来存储，而无需使用数组
        """
        groups = defaultdict(Counter)
        for num in nums:
            groups[num % k][num] += 1
        # 因为不同组之间需要使用乘法原理，所以初始值设为1
        res = 1
        for num2cnt in groups.values():
            pre_2, pre_1 = 1, 1
            items = sorted(num2cnt.items())
            for i, (num, cnt) in enumerate(items):
                if i > 0 and num - items[i - 1][0] == k:
                    cur = ((1 << cnt) - 1) * pre_2 + pre_1
                else:
                    cur = (1 << cnt) * pre_1
                pre_2, pre_1 = pre_1, cur
            res *= pre_1
        # 去掉空集的情况
        return res - 1


if __name__ == '__main__':
    print(Solution().beautifulSubsets_2(nums=[10, 4, 5, 7, 2, 1], k=3))
