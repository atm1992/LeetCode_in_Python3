# -*- coding: UTF-8 -*-
"""
title: 最长递增子序列的个数
Given an integer array nums, return the number of longest increasing subsequences.
Notice that the sequence has to be strictly increasing.


Example 1:
Input: nums = [1,3,5,4,7]
Output: 2
Explanation: The two longest increasing subsequences are [1, 3, 4, 7] and [1, 3, 5, 7].

Example 2:
Input: nums = [2,2,2,2,2]
Output: 5
Explanation: The length of the longest increasing subsequence is 1, and there are 5 increasing subsequences of length 1, so output 5.


Constraints:
1 <= nums.length <= 2000
-10^6 <= nums[i] <= 10^6
"""
from typing import List


class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        """
        动态规划。LeetCode题300方法一的进阶
        dp[i] 表示以nums[i]结尾的最长递增子序列(必须包含nums[i])的长度。
        状态转移方程：dp[i] = max(dp[j]) + 1 其中，0 <= j < i 且 nums[j] < nums[i]
        cnt[i] 表示以nums[i]结尾的最长递增子序列(必须包含nums[i])的个数。
        状态转移方程：cnt[i] = 所有满足dp[j] + 1 == dp[i]的cnt[j]之和
        """
        n = len(nums)
        dp, cnt = [0] * n, [0] * n
        max_len, res = 0, 0
        for i, num in enumerate(nums):
            dp[i] = 1
            cnt[i] = 1
            for j in range(i - 1, -1, -1):
                # 因为长度dp[j] <= j + 1，所以 dp[j] + 1 <= j + 2 < dp[i] 时，不会再出现dp[j] + 1 >= dp[i]的情况
                if j + 2 < dp[i]:
                    break
                if nums[j] < num:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        cnt[i] = cnt[j]
                    elif dp[j] + 1 == dp[i]:
                        cnt[i] += cnt[j]
            if dp[i] > max_len:
                max_len = dp[i]
                res = cnt[i]
            elif dp[i] == max_len:
                res += cnt[i]
        return res

    def findNumberOfLIS_2(self, nums: List[int]) -> int:
        """
        贪心 + 二分查找 + 前缀和。执行速度远快于上面。LeetCode题300方法二的进阶
        将数组d扩展为二维数组，其中d[i]是一个一维数组，d[i]中包含所有长度为i的最长递增子序列的末尾元素值，可以发现，d[i]是单调递减的，
        因为从前往后遍历nums的过程中，如果某个num大于d[i][j]，那么这个num就不会作为长度为i的最长递增子序列的末尾元素值，
        而是会作为长度为i + 1的最长递增子序列的末尾元素值，即 append到d[i+1]数组中。所以只有小于等于d[i][j]的num，才有可能会append到d[i]数组。
        因此，对于当前num，可通过二分查找的方式，在二维数组d中找到第一个满足末尾元素大于等于当前num的子数组d[i]，即 d[i-1][-1] < num <= d[i][-1]，
        然后在d[i-1]中通过二分查找第一个小于当前num的元素下标k，即 d[i-1][k] ~ d[i-1][-1] 中的所有元素都小于当前num，
        这些元素中的每一个都可以和当前num组成长度为i的最长递增子序列。
        由上可知，二维数组d中的所有子数组，它们的末尾元素满足严格单调递增；而每个子数组内部，又满足单调递减。
        类似的，再定义一个对应的二维数组cnt，cnt[i][j]记录了以d[i][j]结尾的最长递增子序列的个数。
        对于上面所有小于当前num(d[i][j])的d[i-1][k] ~ d[i-1][-1]，它们对应的cnt[i-1][k] ~ cnt[i-1][-1]累加，就得到了cnt[i][j]。
        为方便计算cnt[i-1][k] ~ cnt[i-1][-1]的累加和，可将cnt改为前缀和，即 二维数组cnt中的每一个子数组都是前缀和数组，每个前缀和数组的开头元素均为0
        这样一来，最终返回结果就是 cnt[-1][-1]
        对于nums中的每个元素，至多执行两次二分查找，所以时间复杂度为O(nlogn)
        """
        d, cnt = [], []
        for num in nums:
            if not d:
                d.append([num])
                # cnt中的各个子数组的开头元素均为0
                cnt.append([0, 1])
            elif d[-1][-1] < num:
                left, right = 0, len(d[-1]) - 1
                # 在单调递减数组d[-1]中，二分查找第一个小于当前num的元素下标k。已知，d[-1][-1] < num，所以k一定存在
                while left < right:
                    mid = (left + right) // 2
                    if d[-1][mid] < num:
                        right = mid
                    else:
                        left = mid + 1
                # 二维数组d的长度与二维数组cnt的长度相等，不过，cnt中的各个子数组长度都比d中对应的各个子数组长度大1，
                # 因为cnt中的各个子数组都在开头添加了一个0，为了方便计算前缀和
                c = cnt[-1][-1] - cnt[-1][left]
                d.append([num])
                cnt.append([0, c])
            else:
                left, right = 0, len(d) - 1
                # 二维数组d中的所有子数组，它们的末尾元素满足严格单调递增，二分查找第一个满足末尾元素大于等于当前num的子数组下标i
                # 已知，d[-1][-1] >= num，所以i一定存在
                while left < right:
                    mid = (left + right) // 2
                    if d[mid][-1] >= num:
                        right = mid
                    else:
                        left = mid + 1
                i = left
                c = 1
                if i > 0:
                    # 在单调递减数组d[i-1]中，二分查找第一个小于当前num的元素下标k。已知，d[i-1][-1] < num，所以k一定存在
                    left, right = 0, len(d[i - 1]) - 1
                    while left < right:
                        mid = (left + right) // 2
                        if d[i - 1][mid] < num:
                            right = mid
                        else:
                            left = mid + 1
                    c = cnt[i - 1][-1] - cnt[i - 1][left]
                d[i].append(num)
                # 注意：二维数组cnt中的每一个子数组都是前缀和数组，所以这里append的是cnt[i][-1] + c，而不是c
                cnt[i].append(cnt[i][-1] + c)
        return cnt[-1][-1]


if __name__ == '__main__':
    print(Solution().findNumberOfLIS_2(nums=[3, 1, 2]))
