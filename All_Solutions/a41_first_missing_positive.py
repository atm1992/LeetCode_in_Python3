# -*- coding: UTF-8 -*-
"""
title: 缺失的第一个正数。找出其中没有出现的最小的正整数
Given an unsorted integer array nums, return the smallest missing positive integer.
You must implement an algorithm that runs in O(n) time and uses constant extra space.


Example 1:
Input: nums = [1,2,0]
Output: 3

Example 2:
Input: nums = [3,4,-1,1]
Output: 2

Example 3:
Input: nums = [7,8,9,11,12]
Output: 1


Constraints:
1 <= nums.length <= 5 * 10^5
-2^31 <= nums[i] <= 2^31 - 1


解题思路：
如果没有额外的时空复杂度要求，通常会有两种做法：
1、将数组中的所有数放入哈希表，然后从 1 开始依次枚举正整数，判断其是否在哈希表中。时间复杂度为 O(N)，空间复杂度为 O(N)。
2、从 1 开始依次枚举正整数，判断其是否在数组中。时间复杂度为 O(N^2)，空间复杂度为 O(1)。
其实，「真正」满足时间复杂度为 O(N) 且空间复杂度为 O(1) 的算法是不存在的，不过可以退而求其次：利用给定数组中的空间来存储一些状态。
也就是说，如果题目给定的数组是不可修改的，那么就不存在满足时空复杂度要求的算法；但如果我们可以修改给定的数组，那么是存在满足要求的算法的。
对于一个长度为 N 的数组，其中没有出现的最小正整数只可能在 [1, N+1] 中。因为如果 [1, N] 都出现了，那么答案就是 N+1，
否则答案就是 [1, N] 中没有出现的最小正整数。
"""
from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        """原地哈希。将原数组设计成哈希表。
        遍历3次，第一次：将所有<= 0的数变为大于N的正数（例如：N+1）；第二次：遇到元素绝对值在[1, N]范围内的，
        将对应下标(元素绝对值-1, 即 0~N-1)位置的元素值转换为负数；第三次：若发现某个元素值为正数，则说明该下标+1的数字不存在。"""
        n = len(nums)
        for i in range(n):
            if nums[i] <= 0:
                nums[i] = n + 1

        for i in range(n):
            num = abs(nums[i])
            if num <= n:
                nums[num - 1] = -abs(nums[num - 1])

        for i in range(n):
            if nums[i] > 0:
                return i + 1
        return n + 1

    def firstMissingPositive_2(self, nums: List[int]) -> int:
        """置换。
        遍历2次，第一次：遇到元素值在[1, N]范围内的，将对应下标(元素值-1, 即 0~N-1)位置的元素值与当前元素值进行交换，交换后，
        若当前下标的元素值依旧在[1, N]范围内，则继续交换，从而将[1, N]范围内的元素值都放到正确的位置；
        第二次：若发现某个元素值不等于下标+1，则说明该下标+1的数字不存在。"""
        n = len(nums)
        for i in range(n):
            # 加上判断nums[nums[i]-1] != nums[i]，是为了避免进入死循环
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                # nums[i], nums[nums[i] - 1] = nums[nums[i] - 1], nums[i]
                # 上面那样写不会交换元素值。必须下面这样写 或者 先执行idx = nums[i]-1
                # nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
                # 为了避免出错，还是先用一个变量保存好下标
                idx = nums[i] - 1
                nums[i], nums[idx] = nums[idx], nums[i]
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        return n + 1


if __name__ == '__main__':
    print(Solution().firstMissingPositive_2([3, 4, -1, 1]))
