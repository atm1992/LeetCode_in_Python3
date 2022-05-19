# -*- coding: UTF-8 -*-
"""
title: 排序数组中两个数字之和
给定一个已按照 升序排列  的整数数组 numbers ，请你从数组中找出两个数满足相加之和等于目标数 target 。
函数应该以长度为 2 的整数数组的形式返回这两个数的下标值。numbers 的下标 从 0 开始计数 ，所以答案数组应当满足 0 <= answer[0] < answer[1] < numbers.length 。
假设数组中存在且只存在一对符合条件的数字，同时一个数字不能使用两次。


示例 1：
输入：numbers = [1,2,4,6,10], target = 8
输出：[1,3]
解释：2 与 6 之和等于目标数 8 。因此 index1 = 1, index2 = 3 。

示例 2：
输入：numbers = [2,3,4], target = 6
输出：[0,2]

示例 3：
输入：numbers = [-1,0], target = -1
输出：[0,1]


提示：
2 <= numbers.length <= 3 * 10^4
-1000 <= numbers[i] <= 1000
numbers 按 递增顺序 排列
-1000 <= target <= 1000
仅存在一个有效答案
"""
from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """双指针"""
        left, right = 0, len(numbers) - 1
        while left < right:
            total = numbers[left] + numbers[right]
            if total == target:
                return [left, right]
            elif total < target:
                left += 1
            else:
                right -= 1


if __name__ == '__main__':
    print(Solution().twoSum(numbers=[1, 2, 4, 6, 10], target=8))
