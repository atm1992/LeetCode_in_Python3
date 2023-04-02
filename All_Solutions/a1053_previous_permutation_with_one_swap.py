# -*- coding: utf-8 -*-
# @date: 2023/4/3
# @author: liuquan
"""
title: 交换一次的先前排列
Given an array of positive integers arr (not necessarily distinct), return the lexicographically largest permutation that is smaller than arr, that can be made with exactly one swap. If it cannot be done, then return the same array.
Note that a swap exchanges the positions of two numbers arr[i] and arr[j]


Example 1:
Input: arr = [3,2,1]
Output: [3,1,2]
Explanation: Swapping 2 and 1.

Example 2:
Input: arr = [1,1,5]
Output: [1,1,5]
Explanation: This is already the smallest permutation.

Example 3:
Input: arr = [1,9,4,6,7]
Output: [1,7,4,6,9]
Explanation: Swapping 9 and 7.


Constraints:
1 <= arr.length <= 10^4
1 <= arr[i] <= 10^4
"""
from typing import List


class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        """单调栈"""
        n = len(arr)
        stack = []
        for i in range(n - 1, -1, -1):
            j = n
            while stack and arr[i] > arr[stack[-1]]:
                j = stack.pop()
            if j < n:
                arr[i], arr[j] = arr[j], arr[i]
                break
            if stack and arr[i] == arr[stack[-1]]:
                stack.pop()
            stack.append(i)
        return arr

    def prevPermOpt1_2(self, arr: List[int]) -> List[int]:
        """贪心"""
        n = len(arr)
        for i in range(n - 2, -1, -1):
            if arr[i] > arr[i + 1]:
                j = n - 1
                while arr[j] >= arr[i] or arr[j] == arr[j - 1]:
                    j -= 1
                arr[i], arr[j] = arr[j], arr[i]
                break
        return arr


if __name__ == '__main__':
    print(Solution().prevPermOpt1(arr=[1, 9, 4, 6, 7]))
