# -*- coding: UTF-8 -*-
"""
title: 寻找两个正序数组的中位数。
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
    # 这种解法虽然空间复杂度为O(1)，但时间复杂度为O(m+n)，因此不符合要求。
    # 时间复杂度要求为O(log (m+n))，看到有log，并且是有序数组，第一想法就应该是二分查找。
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        len1, len2 = len(nums1), len(nums2)
        p1, p2 = 0, 0
        n1, n2 = 0, 0
        while p1 + p2 <= int((len1 + len2) / 2):
            n1 = n2
            if p1 < len1 and p2 < len2:
                if nums1[p1] <= nums2[p2]:
                    n2 = nums1[p1]
                    p1 += 1
                else:
                    n2 = nums2[p2]
                    p2 += 1
            elif p1 < len1:
                n2 = nums1[p1]
                p1 += 1
            else:
                n2 = nums2[p2]
                p2 += 1
        return n2 if (len1 + len2) % 2 == 1 else (n1 + n2) / 2

    def findMedianSortedArrays_2(self, nums1: List[int], nums2: List[int]) -> float:
        """找到nums1与nums2之间的较短数组，对其进行二分查找，确定了一个数组的下标，自然也就确定了另一个数组的下标，因为中位数的下标是确定的"""
        m, n = len(nums1), len(nums2)
        if m > n:
            return self.findMedianSortedArrays_2(nums2, nums1)
        # -10^6 <= nums1[i], nums2[i] <= 10^6
        infinity = 10 ** 6 + 1
        left, right = 0, m
        # 分别表示 左边的最大值与右边的最小值
        max_left, min_right = 0, 0
        # 跳出循环时，left = right + 1
        while left <= right:
            """
            用i与j分别去划分数组nums1与nums2，划分为 [0 ~ i-1] [i ~ m-1] 以及 [0 ~ j-1] [j ~ n-1]。
            若m+n为偶数，则 i-1-0 + j-1-0 == m-1-i + n-1-j，即 i + j == (m+n)/2；此时的中位数为左边的最大值与右边的最小值相加后除以2
            若m+n为奇数，则 i-1-0 + j-1-0 == m-1-i + n-1-j + 1 (多的那一个元素放到左边)，即 i + j == (m+n+1)/2；此时的中位数就是左边的最大值(也就是左边多出来的那一个元素)
            对于m+n为偶数来说，(m+n)/2 等价于 (m+n+1)//2；对于m+n为奇数来说，(m+n+1)/2 也等价于 (m+n+1)//2；
            因此，无论m+n是偶数还是奇数，都有 i + j == (m+n+1)//2。
            i 可以取值 0 ~ m，取值0表示将整个数组划到右边；取值m表示将整个数组划到左边。所以刚开始时，i 取 0与m 之间的中间位置。
            时间复杂度为 O(log min(m, n))。
            """
            # 这里 // 2 的目的是避免i为小数
            i = (left + right) // 2
            j = (m + n + 1) // 2 - i
            nums_i_1 = -infinity if i == 0 else nums1[i-1]
            nums_i = infinity if i == m else nums1[i]
            nums_j_1 = -infinity if j == 0 else nums2[j-1]
            nums_j = infinity if j == n else nums2[j]
            if nums_i_1 <= nums_j:
                max_left, min_right = max(nums_i_1, nums_j_1), min(nums_i, nums_j)
                left = i + 1
            else:
                right = i - 1
        return (max_left + min_right) / 2 if (m+n) % 2 == 0 else max_left


if __name__ == '__main__':
    nums1 = [2]
    nums2 = []
    print(Solution().findMedianSortedArrays_2(nums1, nums2))
