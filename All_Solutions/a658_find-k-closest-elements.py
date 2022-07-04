# -*- coding: UTF-8 -*-
"""
title: 找到 K 个最接近的元素
Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array. The result should also be sorted in ascending order.
An integer a is closer to x than an integer b if:
    |a - x| < |b - x|, or
    |a - x| == |b - x| and a < b


Example 1:
Input: arr = [1,2,3,4,5], k = 4, x = 3
Output: [1,2,3,4]

Example 2:
Input: arr = [1,2,3,4,5], k = 4, x = -1
Output: [1,2,3,4]


Constraints:
1 <= k <= arr.length
1 <= arr.length <= 10^4
arr is sorted in ascending order.
-10^4 <= arr[i], x <= 10^4
"""
from typing import List


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        """二分查找 + 双指针"""
        n = len(arr)
        if x <= arr[0]:
            return arr[:k]
        elif x >= arr[n - 1]:
            return arr[n - k:]
        else:
            left, right = 0, n - 1
            # 二分查找第一个大于等于x的元素下标
            while left < right:
                mid = (left + right) // 2
                if arr[mid] >= x:
                    right = mid
                else:
                    left = mid + 1
            # arr中最接近x的元素下标idx
            idx = left - 1 if arr[left] - x >= x - arr[left - 1] else left
            # 从两侧向中心idx收缩
            low, high = max(0, idx - k + 1), min(n - 1, idx + k - 1)
            while high - low >= k:
                if x - arr[low] <= arr[high] - x:
                    high -= 1
                else:
                    low += 1
            return arr[low:high + 1]

    def findClosestElements_2(self, arr: List[int], k: int, x: int) -> List[int]:
        """
        滑动窗口 + 二分查找
        把最终结果数组看作是arr上的一个固定长度的滑动窗口，然后使用二分查找最终结果的左边界low，因为滑动窗口内的元素个数需要为k，
        所以low一定位于[0, n - k]之内
        """
        left, right = 0, len(arr) - k
        while left < right:
            mid = (left + right) // 2
            # 因为mid取不到right，所以 mid + k < right + k = len(arr)
            if x - arr[mid] > arr[mid + k] - x:
                # 表示arr[mid]不适合加入到最终结果，因为arr[mid+k]比它更接近x
                # 如果arr[mid]不适合，那么arr[mid]左边的那些元素更不适合，因为那些元素离x更远，所以滑动窗口右移
                left = mid + 1
            else:
                # 表示arr[mid+k]不适合加入到最终结果，因为arr[mid]比它更接近x
                # 如果arr[mid+k]不适合，那么arr[mid+k]右边的那些元素更不适合，因为那些元素离x更远，所以滑动窗口左移
                right = mid
        return arr[left:left + k]


if __name__ == '__main__':
    print(Solution().findClosestElements(arr=[1, 2, 3, 4, 5], k=4, x=3))
