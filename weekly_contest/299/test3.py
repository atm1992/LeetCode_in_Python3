# -*- coding: UTF-8 -*-
from typing import List


class Solution:
    def maximumsSplicedArray(self, nums1: List[int], nums2: List[int]) -> int:
        sum1, sum2 = sum(nums1), sum(nums2)
        max1 = max2 = 0
        tmp1 = tmp2 = 0
        for n1, n2 in zip(nums1, nums2):
            tmp1 = max(0, tmp1)
            tmp2 = max(0, tmp2)
            tmp1 += n2 - n1
            tmp2 += n1 - n2
            max1 = max(max1, tmp1)
            max2 = max(max2, tmp2)
        return max(sum1 + max1, sum2 + max2)


if __name__ == '__main__':
    print(Solution().maximumsSplicedArray(nums1 = [20,40,20,70,30], nums2 = [50,20,50,40,20]))
