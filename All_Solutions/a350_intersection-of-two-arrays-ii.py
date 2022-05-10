# -*- coding: UTF-8 -*-
"""
title: 两个数组的交集 II
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.


Example 1:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]

Example 2:
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Explanation: [9,4] is also accepted.


Constraints:
1 <= nums1.length, nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 1000

Follow up:
What if the given array is already sorted? How would you optimize your algorithm?
答：若已排序，则使用方法二
What if nums1's size is small compared to nums2's size? Which algorithm is better?
答：若存在一个数组的长度明显小于另一个数组，则可使用方法一，先使用哈希表统计长度更小的那个数组的出现次数，然后遍历长度更大的那个数组
What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?
答：此时可使用方法一，先使用哈希表统计nums1的出现次数，然后每次从磁盘读取一部分nums2数据进行遍历
"""
from collections import Counter
from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2):
            return self.intersect(nums2, nums1)
        num2cnt = Counter(nums2)
        res = []
        for num in nums1:
            if num2cnt.get(num, 0) > 0:
                res.append(num)
                num2cnt[num] -= 1
                if num2cnt[num] == 0:
                    num2cnt.pop(num)
                    if len(num2cnt) == 0:
                        break
        return res

    def intersect_2(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        p1, p2 = 0, 0
        l1, l2 = len(nums1), len(nums2)
        res = []
        while p1 < l1 and p2 < l2:
            num1, num2 = nums1[p1], nums2[p2]
            if num1 > num2:
                p2 += 1
            elif num1 < num2:
                p1 += 1
            else:
                res.append(num1)
                p1 += 1
                p2 += 1
        return res
