# -*- coding: UTF-8 -*-
"""
title: 构建乘积数组
给定一个数组 A[0,1,…,n-1]，请构建一个数组 B[0,1,…,n-1]，其中 B[i] 的值是数组 A 中除了下标 i 以外的元素的积, 即 B[i]=A[0]×A[1]×…×A[i-1]×A[i+1]×…×A[n-1]。不能使用除法。


示例:
输入: [1,2,3,4,5]
输出: [120,60,40,30,24]


提示：
所有元素乘积之和不会溢出 32 位整数
a.length <= 100000
"""
from typing import List


class Solution:
    def constructArr(self, a: List[int]) -> List[int]:
        """使用两个数组，分别存储左边所有数字的乘积 以及 右边所有数字的乘积。"""
        n = len(a)
        left_product, right_product = [1] * n, [1] * n
        for i in range(1, n):
            left_product[i] = a[i - 1] * left_product[i - 1]
            right_product[n - i - 1] = a[n - i] * right_product[n - i]
        res = []
        for i in range(n):
            res.append(left_product[i] * right_product[i])
        return res

    def constructArr_2(self, a: List[int]) -> List[int]:
        """为将空间复杂度降至O(1)，还可直接使用res来存储左边所有数字的乘积，然后使用一个变量right_product来跟踪右边元素的乘积"""
        n = len(a)
        res = [1] * n
        for i in range(1, n):
            res[i] = a[i - 1] * res[i - 1]
        right_product = 1
        for i in range(n - 2, -1, -1):
            right_product *= a[i + 1]
            res[i] *= right_product
        return res

    def constructArr_3(self, a: List[int]) -> List[int]:
        """还可再将时间复杂度从O(2n)降至O(n)"""
        n = len(a)
        res = [1] * n
        left_product = right_product = 1
        for i in range(1, n):
            left_product *= a[i - 1]
            right_product *= a[n - i]
            res[i] *= left_product
            res[n - i - 1] *= right_product
        return res


if __name__ == '__main__':
    print(Solution().constructArr_3([1, 2, 3, 4, 5]))
