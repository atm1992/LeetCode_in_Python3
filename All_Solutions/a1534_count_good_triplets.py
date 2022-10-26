# -*- coding: UTF-8 -*-
"""
title: 统计好三元组
Given an array of integers arr, and three integers a, b and c. You need to find the number of good triplets.
A triplet (arr[i], arr[j], arr[k]) is good if the following conditions are true:
    0 <= i < j < k < arr.length
    |arr[i] - arr[j]| <= a
    |arr[j] - arr[k]| <= b
    |arr[i] - arr[k]| <= c
Where |x| denotes the absolute value of x.
Return the number of good triplets.


Example 1:
Input: arr = [3,0,1,1,9,7], a = 7, b = 2, c = 3
Output: 4
Explanation: There are 4 good triplets: [(3,0,1), (3,0,1), (3,1,1), (0,1,1)].

Example 2:
Input: arr = [1,1,2,2,3], a = 0, b = 0, c = 1
Output: 0
Explanation: No triplet satisfies all conditions.


Constraints:
3 <= arr.length <= 100
0 <= arr[i] <= 1000
0 <= a, b, c <= 1000
"""
from typing import List


class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        """三重循环暴力枚举"""
        n = len(arr)
        res = 0
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                if abs(arr[i] - arr[j]) <= a:
                    for k in range(j + 1, n):
                        if abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
                            res += 1
        return res

    def countGoodTriplets_2(self, arr: List[int], a: int, b: int, c: int) -> int:
        """
        优化成二重循环枚举 + 前缀和
        由 abs(arr[i] - arr[j]) <= a 可知，arr[i]的取值范围：arr[j] - a <= arr[i] <= arr[j] + a，因为已知a是非负数
        由 abs(arr[i] - arr[k]) <= c 可知，arr[i]的取值范围：arr[k] - c <= arr[i] <= arr[k] + c，因为已知c是非负数
        综上，arr[i]必须在上面那两个取值范围的交集内，即 max(0, arr[j] - a, arr[k] - c) <= arr[i] <= min(1000, arr[j] + a, arr[k] + c)，因为0 <= arr[i] <= 1000
        因此，可以只枚举j、k，在枚举j、k的过程中，统计 arr[0] ~ arr[j-1] 中符合上述条件的arr[i]的个数。
        """
        n = len(arr)
        res = 0
        # 前缀和数组，因为0 <= arr[i] <= 1000，所以pre_sum的下标i的范围：[0, 1000]，pre_sum[i] 表示arr中值小于等于i的元素个数
        # 因此，符合l_num <= arr[i] <= r_num条件的arr[i]的个数为：pre_sum[r_num] - pre_sum[l_num - 1]
        pre_sum = [0] * 1001
        for j in range(n - 1):
            for k in range(j + 1, n):
                if abs(arr[j] - arr[k]) <= b:
                    l_num = max(0, arr[j] - a, arr[k] - c)
                    r_num = min(1000, arr[j] + a, arr[k] + c)
                    if l_num <= r_num:
                        res += pre_sum[r_num] - (0 if l_num == 0 else pre_sum[l_num - 1])
            # 这里其实可以使用线段树/树状数组做进一步优化
            for num in range(arr[j], 1001):
                pre_sum[num] += 1
        return res


if __name__ == '__main__':
    print(Solution().countGoodTriplets_2(arr=[3, 0, 1, 1, 9, 7], a=7, b=2, c=3))
