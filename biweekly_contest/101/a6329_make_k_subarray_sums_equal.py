# -*- coding: utf-8 -*-
# @date: 2023/4/1
# @author: liuquan
"""
title: 使子数组元素和相等
You are given a 0-indexed integer array arr and an integer k. The array arr is circular. In other words, the first element of the array is the next element of the last element, and the last element of the array is the previous element of the first element.
You can do the following operation any number of times:
    Pick any element from arr and increase or decrease it by 1.
Return the minimum number of operations such that the sum of each subarray of length k is equal.
A subarray is a contiguous part of the array.


Example 1:
Input: arr = [1,4,1,3], k = 2
Output: 1
Explanation: we can do one operation on index 1 to make its value equal to 3.
The array after the operation is [1,3,1,3]
- Subarray starts at index 0 is [1, 3], and its sum is 4
- Subarray starts at index 1 is [3, 1], and its sum is 4
- Subarray starts at index 2 is [1, 3], and its sum is 4
- Subarray starts at index 3 is [3, 1], and its sum is 4

Example 2:
Input: arr = [2,5,5,7], k = 3
Output: 5
Explanation: we can do three operations on index 0 to make its value equal to 5 and two operations on index 3 to make its value equal to 5.
The array after the operations is [5,5,5,5]
- Subarray starts at index 0 is [5, 5, 5], and its sum is 15
- Subarray starts at index 1 is [5, 5, 5], and its sum is 15
- Subarray starts at index 2 is [5, 5, 5], and its sum is 15
- Subarray starts at index 3 is [5, 5, 5], and its sum is 15


Constraints:
1 <= k <= arr.length <= 10^5
1 <= arr[i] <= 10^9
"""
import math
from collections import defaultdict
from typing import List


class Solution:
    def makeSubKSumEqual(self, arr: List[int], k: int) -> int:
        """原问题可转化为：每个长度为gcd(len(arr), k)的子数组的元素和应相等。即 要使 arr[i] == arr[i + gcd]"""
        n = len(arr)
        if k == n:
            return 0

        def get_diff(nums: List[int]) -> int:
            """
            贪心，当都变成中位数时，所需的运算次数最少。
            将nums中的所有元素都变成同一个值，该值肯定在 [min, max] 之间，无论该值是多少，
            min到该值的距离 + 该值到max的距离 始终等于 max - min，这样就将问题规模缩小了
            最终会缩到只剩中间的一个元素(数组长度为奇数)或不剩任何元素(数组长度为偶数)
            """
            nums = sorted(nums)
            if nums[0] == nums[-1]:
                return 0
            res = 0
            left, right = 0, len(nums) - 1
            while left < right:
                res += nums[right] - nums[left]
                right -= 1
                left += 1
            return res

        k = math.gcd(k, n)
        idx2nums = defaultdict(list)
        for i, num in enumerate(arr):
            idx2nums[i % k].append(num)
        return sum(get_diff(nums) for nums in idx2nums.values())


if __name__ == '__main__':
    print(Solution().makeSubKSumEqual(arr=[2, 5, 5, 7], k=3))
