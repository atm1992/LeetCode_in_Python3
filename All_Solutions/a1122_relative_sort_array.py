# -*- coding: UTF-8 -*-
"""
title: 数组的相对排序
Given two arrays arr1 and arr2, the elements of arr2 are distinct, and all elements in arr2 are also in arr1.
Sort the elements of arr1 such that the relative ordering of items in arr1 are the same as in arr2. Elements that do not appear in arr2 should be placed at the end of arr1 in ascending order.


Example 1:
Input: arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
Output: [2,2,2,1,4,3,3,9,6,7,19]

Example 2:
Input: arr1 = [28,6,22,8,44,17], arr2 = [22,28,8,6]
Output: [22,28,8,6,17,44]


Constraints:
1 <= arr1.length, arr2.length <= 1000
0 <= arr1[i], arr2[i] <= 1000
All the elements of arr2 are distinct.
Each arr2[i] is in arr1.
"""
from collections import Counter
from typing import List


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        res = []
        num2cnt = Counter(arr1)
        for num in arr2:
            cnt = num2cnt.pop(num)
            res.extend([num] * cnt)
        for num in sorted(num2cnt.keys()):
            cnt = num2cnt.pop(num)
            res.extend([num] * cnt)
        return res

    def relativeSortArray_2(self, arr1: List[int], arr2: List[int]) -> List[int]:
        """自定义排序的比较函数"""
        n = len(arr2)
        num2rank = {num: idx - n for idx, num in enumerate(arr2)}
        # 因为 0 <= arr1[i], arr2[i]
        # 存在于arr2中的num，其rank为负数(idx - n)；不在arr2中的num，其rank为正数(num本身)
        arr1.sort(key=lambda num: num2rank.get(num, num))
        return arr1
