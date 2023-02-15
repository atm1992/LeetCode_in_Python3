# -*- coding: UTF-8 -*-
"""
title: 检查「好数组」
Given an array nums of positive integers. Your task is to select some subset of nums, multiply each element by an integer and add all these numbers. The array is said to be good if you can obtain a sum of 1 from the array by any possible subset and multiplicand.
Return True if the array is good otherwise return False.


Example 1:
Input: nums = [12,5,7,23]
Output: true
Explanation: Pick numbers 5 and 7.
5*3 + 7*(-2) = 1

Example 2:
Input: nums = [29,6,10]
Output: true
Explanation: Pick numbers 29, 6 and 10.
29*1 + 6*(-3) + 10*(-1) = 1

Example 3:
Input: nums = [3,6]
Output: false


Constraints:
1 <= nums.length <= 10^5
1 <= nums[i] <= 10^9
"""
from functools import reduce
from math import gcd
from typing import List


class Solution:
    def isGoodArray(self, nums: List[int]) -> bool:
        """
        数论。
        根据裴蜀定理：对于不全为零的两个整数a和b，若a和b的最大公约数gcd(a, b) = g，则对于任意整数x和y，都满足 a*x + b*y 是 g 的倍数，
        特别地，存在整数x和y使得 a*x + b*y = g
        裴蜀定理还可推广到多个整数的情况，对于不全为零的n个整数a1、a2、……、an，若这n个整数的最大公约数为g，则对于任意n个整数x1、x2、……、xn，
        都满足 a1 * x1 + a2 * x2 + …… + an * xn 是 g 的倍数。一个重要的推论是：正整数a1、a2、……、an的最大公约数为1 的充要条件是
        存在n个整数x1、x2、……、xn使得 a1 * x1 + a2 * x2 + …… + an * xn = 1
        回到本题，只要原数组nums中存在若干个元素的最大公约数为1，则说明存在好数组。若数组中若干个元素的最大公约数为1，
        则整个数组中所有元素的最大公约数也一定为1，因此只需直接判断整个数组中所有元素的最大公约数是否为1
        """
        return reduce(gcd, nums) == 1


if __name__ == '__main__':
    print(Solution().isGoodArray(nums=[12, 5, 7, 23]))
