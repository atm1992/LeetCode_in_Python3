# -*- coding: UTF-8 -*-
"""
title: 寻找两个正序数组的中位数
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
The overall run time complexity should be O(log (m+n)).


Example 1:
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

Example 2:
Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

Example 3:
Input: nums1 = [0,0], nums2 = [0,0]
Output: 0.00000

Example 4:
Input: nums1 = [], nums2 = [1]
Output: 1.00000

Example 5:
Input: nums1 = [2], nums2 = []
Output: 2.00000
 

Constraints:
nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-10^6 <= nums1[i], nums2[i] <= 10^6
"""
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """顺序扫描。虽然空间复杂度为O(1)，但时间复杂度为O(m+n)，因此不符合题目要求。"""
        m, n = len(nums1), len(nums2)
        p1 = p2 = 0
        pre = cur = 0
        for _ in range((m + n) // 2 + 1):
            pre = cur
            if p1 < m and p2 < n:
                if nums1[p1] <= nums2[p2]:
                    cur = nums1[p1]
                    p1 += 1
                else:
                    cur = nums2[p2]
                    p2 += 1
            elif p1 < m:
                cur = nums1[p1]
                p1 += 1
            else:
                cur = nums2[p2]
                p2 += 1
        return cur if (m + n) & 1 else (pre + cur) / 2

    def findMedianSortedArrays_2(self, nums1: List[int], nums2: List[int]) -> float:
        """
        二分查找
        题目要求时间复杂度为O(log(m+n))，看到有log，并且是有序数组，首先就应想到使用二分查找。
        找到nums1与nums2之间的较短数组，对其进行二分查找，确定了一个数组的下标，自然也就确定了另一个数组的下标，因为中位数的下标是确定的。
        用i与j分别去划分数组nums1与nums2，划分为左半边（[0, i) + [0, j)）和右半边（[i, m) + [j, n)）。
        若m+n为偶数，则 i + j == m-i + n-j，即 i + j == (m+n)/2；此时的中位数为左半边的最大值与右半边的最小值相加后除以2
        若m+n为奇数，则 i + j == m-i + n-j + 1 (多出的那个元素放到左半边)，即 i + j == (m+n+1)/2；此时的中位数就是左半边的最大值(也就是左半边多出的那个元素)
        对于m+n为偶数来说，(m+n)/2 等价于 (m+n+1)//2；对于m+n为奇数来说，(m+n+1)/2 也等价于 (m+n+1)//2；所以，无论m+n是偶数还是奇数，都有 i + j == (m+n+1)//2。
        i 的取值范围：[0, m]。i取0时，[0, i)为空数组，即 将整个nums1划分到右半边；i取m时，[i, m)为空数组，即 将整个nums1划分到左半边。初始时，i 可取0与m之间的中间位置。
        时间复杂度为 O(log min(m, n))。
        """
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays_2(nums2, nums1)
        m, n = len(nums1), len(nums2)
        median_idx = (m + n + 1) // 2
        # 分别记录 左半边的最大值、右半边的最小值
        max_left = min_right = 0
        left, right = 0, m
        while left <= right:
            i = (left + right) // 2
            j = median_idx - i
            nums1_left = float('-inf') if i == 0 else nums1[i - 1]
            nums1_right = float('inf') if i == m else nums1[i]
            nums2_left = float('-inf') if j == 0 else nums2[j - 1]
            nums2_right = float('inf') if j == n else nums2[j]
            if nums1_left <= nums2_right:
                max_left, min_right = max(nums1_left, nums2_left), min(nums1_right, nums2_right)
                # i 向右移，逐渐增大nums1_left、nums1_right
                left = i + 1
            else:
                # i 向左移，逐渐减小nums1_left、nums1_right
                right = i - 1
        return max_left if (m + n) & 1 else (max_left + min_right) / 2


if __name__ == '__main__':
    print(Solution().findMedianSortedArrays_2([2], []))
