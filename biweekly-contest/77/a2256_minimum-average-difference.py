# -*- coding: UTF-8 -*-
"""
title: 最小平均差
You are given a 0-indexed integer array nums of length n.
The average difference of the index i is the absolute difference between the average of the first i + 1 elements of nums and the average of the last n - i - 1 elements. Both averages should be rounded down to the nearest integer.
Return the index with the minimum average difference. If there are multiple such indices, return the smallest one.
Note:
    The absolute difference of two numbers is the absolute value of their difference.
    The average of n elements is the sum of the n elements divided (integer division) by n.
    The average of 0 elements is considered to be 0.


Example 1:
Input: nums = [2,5,3,9,5,3]
Output: 3
Explanation:
- The average difference of index 0 is: |2 / 1 - (5 + 3 + 9 + 5 + 3) / 5| = |2 / 1 - 25 / 5| = |2 - 5| = 3.
- The average difference of index 1 is: |(2 + 5) / 2 - (3 + 9 + 5 + 3) / 4| = |7 / 2 - 20 / 4| = |3 - 5| = 2.
- The average difference of index 2 is: |(2 + 5 + 3) / 3 - (9 + 5 + 3) / 3| = |10 / 3 - 17 / 3| = |3 - 5| = 2.
- The average difference of index 3 is: |(2 + 5 + 3 + 9) / 4 - (5 + 3) / 2| = |19 / 4 - 8 / 2| = |4 - 4| = 0.
- The average difference of index 4 is: |(2 + 5 + 3 + 9 + 5) / 5 - 3 / 1| = |24 / 5 - 3 / 1| = |4 - 3| = 1.
- The average difference of index 5 is: |(2 + 5 + 3 + 9 + 5 + 3) / 6 - 0| = |27 / 6 - 0| = |4 - 0| = 4.
The average difference of index 3 is the minimum average difference so return 3.

Example 2:
Input: nums = [0]
Output: 0
Explanation:
The only index is 0 so return 0.
The average difference of index 0 is: |0 / 1 - 0| = |0 - 0| = 0.


Constraints:
1 <= nums.length <= 10^5
0 <= nums[i] <= 10^5
"""
from typing import List


class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        n = len(nums)
        pre_sum = [nums[0]]
        for i in range(1, n):
            pre_sum.append(pre_sum[i - 1] + nums[i])
        diff = float('inf')
        res = 0
        for i in range(n):
            num1 = 0 if i == n - 1 else (pre_sum[n - 1] - pre_sum[i]) // (n - 1 - i)
            num2 = pre_sum[i] // (i + 1)
            tmp = abs(num1 - num2)
            if tmp < diff:
                diff = tmp
                res = i
            if tmp == 0:
                break
        return res


if __name__ == '__main__':
    print(Solution().minimumAverageDifference(nums=[0]))
