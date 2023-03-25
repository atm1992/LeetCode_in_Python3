# -*- coding: utf-8 -*-
# @date: 2023/3/25
# @author: liuquan
"""
title: 删除最短的子数组使剩余数组有序
Given an integer array arr, remove a subarray (can be empty) from arr such that the remaining elements in arr are non-decreasing.
Return the length of the shortest subarray to remove.
A subarray is a contiguous subsequence of the array.


Example 1:
Input: arr = [1,2,3,10,4,2,3,5]
Output: 3
Explanation: The shortest subarray we can remove is [10,4,2] of length 3. The remaining elements after that will be [1,2,3,3,5] which are sorted.
Another correct solution is to remove the subarray [3,10,4].

Example 2:
Input: arr = [5,4,3,2,1]
Output: 4
Explanation: Since the array is strictly decreasing, we can only keep a single element. Therefore, we need to remove a subarray of length 4, either [5,4,3,2] or [4,3,2,1].

Example 3:
Input: arr = [1,2,3]
Output: 0
Explanation: The array is already non-decreasing. We do not need to remove any elements.


Constraints:
1 <= arr.length <= 10^5
0 <= arr[i] <= 10^9
"""
from typing import List


class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        """双指针。被删除的子数组要么在左侧，要么在右侧，要么在中间。对比这3种情况，取最小值。"""
        n = len(arr)
        j = n - 1
        # 找到右侧最长的递增子数组，然后删除左侧的最短子数组。跳出while循环时，j指向递增子数组的第一个元素
        while j > 0 and arr[j - 1] <= arr[j]:
            j -= 1
        # 说明原始数组本身是递增的，无需删除任何元素
        if j == 0:
            return 0
        res = j
        # 删除中间的最短子数组 或 右侧的最短子数组
        # 左侧最长的递增子数组的最后一个元素的下标i一定会小于j。若大于等于j，则说明原始数组本身是递增的，那么前面就已经return 0了
        for i in range(j):
            # 当j==n时，而i还在继续增长时，此时计算的是左侧最长的递增子数组
            while j < n and arr[i] > arr[j]:
                j += 1
            res = min(res, j - i - 1)
            if arr[i] > arr[i + 1]:
                break
        return res


if __name__ == '__main__':
    print(Solution().findLengthOfShortestSubarray([5, 4, 3, 2, 1]))
