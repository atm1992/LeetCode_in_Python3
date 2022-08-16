# -*- coding: UTF-8 -*-
"""
title: 不相交的线
You are given two integer arrays nums1 and nums2. We write the integers of nums1 and nums2 (in the order they are given) on two separate horizontal lines.
We may draw connecting lines: a straight line connecting two numbers nums1[i] and nums2[j] such that:
    nums1[i] == nums2[j], and
    the line we draw does not intersect any other connecting (non-horizontal) line.
Note that a connecting line cannot intersect even at the endpoints (i.e., each number can only belong to one connecting line).
Return the maximum number of connecting lines we can draw in this way.


Example 1:
Input: nums1 = [1,4,2], nums2 = [1,2,4]
Output: 2
Explanation: We can draw 2 uncrossed lines as in the diagram.
We cannot draw 3 uncrossed lines, because the line from nums1[1] = 4 to nums2[2] = 4 will intersect the line from nums1[2]=2 to nums2[1]=2.

Example 2:
Input: nums1 = [2,5,1,2,5], nums2 = [10,5,2,1,5,2]
Output: 3

Example 3:
Input: nums1 = [1,3,7,1,7,5], nums2 = [1,9,2,5,1]
Output: 2


Constraints:
1 <= nums1.length, nums2.length <= 500
1 <= nums1[i], nums2[j] <= 2000
"""
from typing import List


class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        """
        二维动态规划
        k条互不相交的连线会连接nums1和nums2的k对相等的元素，即 nums1中的k个元素与nums2中的k个元素，它们的相对顺序是一致的。
        因此，这k对相等的元素其实就是nums1和nums2的最长公共子序列，可使用二维动态规划来求解最长公共子序列问题，参考LeetCode题1143
        dp[i][j] 表示nums1中前i个元素(下标i-1)与nums2中前j个元素(下标j-1)之间最长公共子序列的长度。
        边界情况：空数组与任意数组之间最长公共子序列的长度均为0，所以 dp[0][*] = dp[*][0] = 0
        状态转移方程：若nums1[i-1] == nums2[j-1]，则 dp[i][j] = dp[i-1][j-1] + 1；
        若nums[i-1] != nums[j-1]，则 dp[i][j] = max(dp[i-1][j], dp[i][j-1])。
        相当于 用nums1中前i-1个元素与nums2中前j个元素去匹配 以及 用nums1中前i个元素与nums2中前j-1个元素去匹配
        """
        m, n = len(nums1), len(nums2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if nums1[i - 1] == nums2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp[-1][-1]


if __name__ == '__main__':
    print(Solution().maxUncrossedLines(nums1=[2, 5, 1, 2, 5], nums2=[10, 5, 2, 1, 5, 2]))
