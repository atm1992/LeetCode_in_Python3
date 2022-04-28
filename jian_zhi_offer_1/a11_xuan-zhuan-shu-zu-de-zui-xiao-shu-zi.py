# -*- coding: UTF-8 -*-
"""
title: 旋转数组的最小数字
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
给你一个可能存在 重复 元素值的数组 numbers ，它原来是一个升序排列的数组，并按上述情形进行了一次旋转。请返回旋转数组的最小元素。例如，数组 [3,4,5,1,2] 为 [1,2,3,4,5] 的一次旋转，该数组的最小值为 1。  
注意，数组 [a[0], a[1], a[2], ..., a[n-1]] 旋转一次 的结果为数组 [a[n-1], a[0], a[1], a[2], ..., a[n-2]] 。


示例 1：
输入：numbers = [3,4,5,1,2]
输出：1

示例 2：
输入：numbers = [2,2,2,0,1]
输出：0


提示：
n == numbers.length
1 <= n <= 5000
-5000 <= numbers[i] <= 5000
numbers 原来是一个升序排序的数组，并进行了 1 至 n 次旋转
"""
from typing import List


class Solution:
    def minArray(self, numbers: List[int]) -> int:
        return min(numbers)

    def minArray_2(self, numbers: List[int]) -> int:
        """二分查找"""
        left, right = 0, len(numbers) - 1
        while left < right:
            mid = (left + right) >> 1
            if numbers[mid] > numbers[right]:
                left = mid + 1
            elif numbers[mid] < numbers[right]:
                right = mid
            else:
                # 这里不能写成 right = mid，例如：[3,3,1,3]
                right -= 1
        return numbers[left]


if __name__ == '__main__':
    print(Solution().minArray([2, 2, 2, 0, 1]))
