# -*- coding: UTF-8 -*-
"""
title:
You are given two integer arrays nums1 and nums2 both of the same length. The advantage of nums1 with respect to nums2 is the number of indices i for which nums1[i] > nums2[i].
Return any permutation of nums1 that maximizes its advantage with respect to nums2.


Example 1:
Input: nums1 = [2,7,11,15], nums2 = [1,10,4,11]
Output: [2,11,7,15]

Example 2:
Input: nums1 = [12,24,8,32], nums2 = [13,25,32,11]
Output: [24,32,8,12]


Constraints:
1 <= nums1.length <= 10^5
nums2.length == nums1.length
0 <= nums1[i], nums2[i] <= 10^9
"""
from typing import List


class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        排序 + 贪心 + 双指针。
        对nums1升序，根据nums2中的元素值对nums2的下标序列升序
        类似于田忌赛马，若nums1中的当前最小值min1小于等于nums2中的当前最小值min2，则拿min1去匹配nums2中的当前最大值
        """
        n = len(nums1)
        res = [0] * n
        nums1.sort()
        idxs2 = sorted(range(n), key=lambda i: nums2[i])
        # 使用双指针填充res数组
        left, right = 0, n - 1
        for num in nums1:
            if num > nums2[idxs2[left]]:
                res[idxs2[left]] = num
                left += 1
            else:
                res[idxs2[right]] = num
                right -= 1
        return res


if __name__ == '__main__':
    print(Solution().advantageCount(nums1=[2, 7, 11, 15], nums2=[1, 10, 4, 11]))
