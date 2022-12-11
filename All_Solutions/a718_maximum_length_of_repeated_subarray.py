# -*- coding: UTF-8 -*-
"""
title: 最长重复子数组
Given two integer arrays nums1 and nums2, return the maximum length of a subarray that appears in both arrays.


Example 1:
Input: nums1 = [1,2,3,2,1], nums2 = [3,2,1,4,7]
Output: 3
Explanation: The repeated subarray with maximum length is [3,2,1].

Example 2:
Input: nums1 = [0,0,0,0,0], nums2 = [0,0,0,0,0]
Output: 5
Explanation: The repeated subarray with maximum length is [0,0,0,0,0].


Constraints:
1 <= nums1.length, nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 100
"""
from typing import List


class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        """
        动态规划
        dp[i][j] 表示nums1[i:]和nums2[j:]的公共前缀的长度，公共前缀必须包含nums1[i]、nums2[j]。
        状态转移方程：
        1、若nums1[i] == nums2[j]，则 dp[i][j] = dp[i+1][j+1] + 1
        2、若nums1[i] != nums2[j]，则 dp[i][j] = 0
        """
        res = 0
        n1, n2 = len(nums1), len(nums2)
        dp = [0] * (n2 + 1)
        for i in range(n1 - 1, -1, -1):
            for j in range(n2):
                dp[j] = dp[j + 1] + 1 if nums1[i] == nums2[j] else 0
                res = max(res, dp[j])
        return res

    def findLength_2(self, nums1: List[int], nums2: List[int]) -> int:
        """
        滑动窗口
        1、固定nums1，逐个滑动nums2，然后对比nums1原数组与nums2子数组中相同下标的元素，记录其中的最大长度
        2、固定nums2，逐个滑动nums1，然后对比nums1子数组与nums2原数组中相同下标的元素，记录其中的最大长度
        """

        def get_max_len(base1: int, base2: int, size: int) -> int:
            max_len, k = 0, 0
            for i in range(size):
                if nums1[base1 + i] == nums2[base2 + i]:
                    k += 1
                    max_len = max(max_len, k)
                else:
                    k = 0
            return max_len

        res = 0
        n1, n2 = len(nums1), len(nums2)
        for i in range(n1):
            # 固定nums2，逐个滑动nums1
            size = min(n1 - i, n2)
            # 若剩余的公共长度小于等于res，则无需再比较了，因为比较的结果不可能大于res了
            if size <= res:
                break
            # nums1从下标i开始形成一个子数组，nums2从下标0开始形成一个子数组(即 nums2本身)，比较这两个子数组中相同下标的元素
            res = max(res, get_max_len(i, 0, size))
        for i in range(n2):
            size = min(n1, n2 - i)
            if size <= res:
                break
            res = max(res, get_max_len(0, i, size))
        return res


if __name__ == '__main__':
    print(Solution().findLength_2(nums1=[1, 2, 3, 2, 1], nums2=[3, 2, 1, 4, 7]))
