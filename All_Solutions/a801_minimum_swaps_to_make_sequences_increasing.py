# -*- coding: UTF-8 -*-
"""
title: 使序列递增的最小交换次数
You are given two integer arrays of the same length nums1 and nums2. In one operation, you are allowed to swap nums1[i] with nums2[i].
    For example, if nums1 = [1,2,3,8], and nums2 = [5,6,7,4], you can swap the element at i = 3 to obtain nums1 = [1,2,3,4] and nums2 = [5,6,7,8].
Return the minimum number of needed operations to make nums1 and nums2 strictly increasing. The test cases are generated so that the given input always makes it possible.
An array arr is strictly increasing if and only if arr[0] < arr[1] < arr[2] < ... < arr[arr.length - 1].


Example 1:
Input: nums1 = [1,3,5,4], nums2 = [1,2,3,7]
Output: 1
Explanation:
Swap nums1[3] and nums2[3]. Then the sequences are:
nums1 = [1, 3, 5, 7] and nums2 = [1, 2, 3, 4]
which are both strictly increasing.

Example 2:
Input: nums1 = [0,3,5,8,9], nums2 = [2,1,4,6,9]
Output: 1


Constraints:
2 <= nums1.length <= 10^5
nums2.length == nums1.length
0 <= nums1[i], nums2[i] <= 2 * 10^5
"""
from typing import List


class Solution:
    def minSwap(self, nums1: List[int], nums2: List[int]) -> int:
        """
        动态规划
        设dp[i][0]表示不交换位置i的元素，使得序列递增的最小交换次数；dp[i][1]表示交换位置i的元素，使得序列递增的最小交换次数。
        相同位置的两个元素至少满足以下两种情况之一，因为题目保证了所有用例都可实现操作
        1、nums1[i] > nums1[i-1] and nums2[i] > nums2[i-1]
        2、nums1[i] > nums2[i-1] and nums2[i] > nums1[i-1]
        状态转移方程：
        1、若只满足情况1，而不满足情况2，则位置i的交换情况需要和位置i-1的交换情况一致。因此，dp[i][0] = dp[i-1][0]；dp[i][1] = dp[i-1][1] + 1
        2、若只满足情况2，而不满足情况1，则位置i的交换情况需要和位置i-1的交换情况相反。因此，dp[i][0] = dp[i-1][1]；dp[i][1] = dp[i-1][0] + 1
        3、若同时满足情况1和情况2，此时既可选择交换位置i，也可选择不交换位置i。因此，dp[i][0] = min(dp[i-1][0], dp[i-1][1])；dp[i][1] = min(dp[i-1][0], dp[i-1][1]) + 1
        初始值：
        对于第一个位置上的两个元素，既可选择交换位置，也可选择不交换位置。因此，dp[0][0] = 0；dp[0][1] = 1
        可以发现，dp[i]只与dp[i-1]有关，因此可用滚动数组来优化空间复杂度
        """
        dp_0, dp_1 = 0, 1
        for i in range(1, len(nums1)):
            if nums1[i] > max(nums1[i - 1], nums2[i - 1]) and nums2[i] > max(nums1[i - 1], nums2[i - 1]):
                dp_0, dp_1 = min(dp_0, dp_1), min(dp_0, dp_1) + 1
            elif nums1[i] > nums1[i - 1] and nums2[i] > nums2[i - 1]:
                dp_1 += 1
            else:
                dp_0, dp_1 = dp_1, dp_0 + 1
        return min(dp_0, dp_1)


if __name__ == '__main__':
    print(Solution().minSwap(nums1=[0, 3, 5, 8, 9], nums2=[2, 1, 4, 6, 9]))
