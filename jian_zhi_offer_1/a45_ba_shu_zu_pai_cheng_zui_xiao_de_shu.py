# -*- coding: UTF-8 -*-
"""
title: 把数组排成最小的数
输入一个非负整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。


示例 1:
输入: [10,2]
输出: "102"

示例 2:
输入: [3,30,34,5,9]
输出: "3033459"


提示:
0 < nums.length <= 100
说明:
输出结果可能非常大，所以你需要返回一个字符串而不是整数
拼接起来的数字可能会有前导 0，最后结果不需要去掉前导 0
"""
from functools import cmp_to_key
from typing import List


class Solution:
    def minNumber(self, nums: List[int]) -> str:
        """使用内置排序函数"""
        nums_str = [str(num) for num in nums]

        def cmp(a: str, b: str) -> int:
            x, y = a + b, b + a
            if x > y:
                return 1
            elif x < y:
                return -1
            else:
                return 0

        nums_str.sort(key=cmp_to_key(cmp))
        return ''.join(nums_str)

    def minNumber_2(self, nums: List[int]) -> str:
        """快速排序。最终要升序"""
        nums_str = [str(num) for num in nums]

        def quick_sort(nums: List[str], left: int, right: int) -> None:
            # 少于两个元素时，直接不用排
            if left >= right:
                return
            i, j = left, right
            # 退出循环时，i == j
            while i < j:
                while i < j and nums[j] + nums[left] > nums[left] + nums[j]:
                    j -= 1
                while i < j and nums[i] + nums[left] <= nums[left] + nums[i]:
                    i += 1
                # 这里判不判断其实无所谓，因为这里要么 i < j，要么 i == j。i == j时，交换了等于没交换
                if i < j:
                    nums[i], nums[j] = nums[j], nums[i]
            nums[i], nums[left] = nums[left], nums[i]
            quick_sort(nums, left, i - 1)
            quick_sort(nums, i + 1, right)

        quick_sort(nums_str, 0, len(nums_str) - 1)
        return ''.join(nums_str)


if __name__ == '__main__':
    print(Solution().minNumber_2([3, 30, 34, 5, 9]))
