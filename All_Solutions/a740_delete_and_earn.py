# -*- coding: UTF-8 -*-
"""
title: 删除并获得点数
You are given an integer array nums. You want to maximize the number of points you get by performing the following operation any number of times:
    Pick any nums[i] and delete it to earn nums[i] points. Afterwards, you must delete every element equal to nums[i] - 1 and every element equal to nums[i] + 1.
Return the maximum number of points you can earn by applying the above operation some number of times.


Example 1:
Input: nums = [3,4,2]
Output: 6
Explanation: You can perform the following operations:
- Delete 4 to earn 4 points. Consequently, 3 is also deleted. nums = [2].
- Delete 2 to earn 2 points. nums = [].
You earn a total of 6 points.

Example 2:
Input: nums = [2,2,3,3,3,4]
Output: 9
Explanation: You can perform the following operations:
- Delete a 3 to earn 3 points. All 2's and 4's are also deleted. nums = [3,3].
- Delete a 3 again to earn 3 points. nums = [3].
- Delete a 3 once more to earn 3 points. nums = [].
You earn a total of 9 points.


Constraints:
1 <= nums.length <= 2 * 10^4
1 <= nums[i] <= 10^4
"""
from collections import Counter
from typing import List


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        """
        动态规划。参考LeetCode题198
        根据题意，选择了值为x的元素后，就需要删除所有等于x-1和x+1的元素，若x出现a次，则可直接获取点数a*x，
        因为第一次获取点数a时，就会把所有的x-1和x+1都删除，之后获取点数x*(a-1)时，无需再删除x-1和x+1了。
        可以先使用一个数组num2sum来按顺序统计所有值的出现累加和，然后基于数组num2sum进行动态规划
        dp[i] 表示删除前i个值所能获得的最大点数，状态转移方程：dp[i] = max(dp[i-2] + num2sum[i], dp[i-1])
        边界条件：dp[0] = num2sum[0], dp[1] = max(num2sum[0], num2sum[1])
        """
        num2sum = [0] * (max(nums) + 1)
        for num in nums:
            num2sum[num] += num
        # 基于数组num2sum进行动态规划
        pre_2, pre_1 = 0, num2sum[0]
        for i in range(1, len(num2sum)):
            pre_2, pre_1 = pre_1, max(pre_2 + num2sum[i], pre_1)
        return pre_1

    def deleteAndEarn_2(self, nums: List[int]) -> int:
        """
        排序 + 动态规划
        方法一的数组num2sum中可能存在大量sum为0的元素
        """
        num2cnt = Counter(nums)
        sorted_keys = sorted(num2cnt.keys())
        # 基于数组sorted_keys进行动态规划
        pre_2, pre_1 = 0, sorted_keys[0] * num2cnt[sorted_keys[0]]
        for i in range(1, len(sorted_keys)):
            if sorted_keys[i] - sorted_keys[i - 1] == 1:
                pre_2, pre_1 = pre_1, max(pre_2 + sorted_keys[i] * num2cnt[sorted_keys[i]], pre_1)
            else:
                pre_2, pre_1 = pre_1, pre_1 + sorted_keys[i] * num2cnt[sorted_keys[i]]
        return pre_1


if __name__ == '__main__':
    print(Solution().deleteAndEarn_2([2, 2, 3, 3, 3, 4]))
