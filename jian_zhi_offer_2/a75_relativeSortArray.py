# -*- coding: UTF-8 -*-
"""
title: 数组相对排序
给定两个数组，arr1 和 arr2，
    arr2 中的元素各不相同
    arr2 中的每个元素都出现在 arr1 中
对 arr1 中的元素进行排序，使 arr1 中项的相对顺序和 arr2 中的相对顺序相同。未在 arr2 中出现过的元素需要按照升序放在 arr1 的末尾。


示例：
输入：arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
输出：[2,2,2,1,4,3,3,9,6,7,19]


提示：
1 <= arr1.length, arr2.length <= 1000
0 <= arr1[i], arr2[i] <= 1000
arr2 中的元素 arr2[i] 各不相同
arr2 中的每个元素 arr2[i] 都出现在 arr1 中
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
