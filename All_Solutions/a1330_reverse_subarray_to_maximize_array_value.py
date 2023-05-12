# -*- coding: utf-8 -*-
# @date: 2023/5/12
# @author: liuquan
"""
title: 翻转子数组得到最大的数组值
You are given an integer array nums. The value of this array is defined as the sum of |nums[i] - nums[i + 1]| for all 0 <= i < nums.length - 1.
You are allowed to select any subarray of the given array and reverse it. You can perform this operation only once.
Find maximum possible value of the final array.


Example 1:
Input: nums = [2,3,1,5,4]
Output: 10
Explanation: By reversing the subarray [3,1,5] the array becomes [2,5,1,3,4] whose value is 10.

Example 2:
Input: nums = [2,4,9,24,2,1,10]
Output: 68


Constraints:
1 <= nums.length <= 3 * 10^4
-10^5 <= nums[i] <= 10^5
"""
from typing import List


class Solution:
    def maxValueAfterReverse(self, nums: List[int]) -> int:
        """
        分类讨论 + 枚举
        1、不进行翻转时，数组值记为 base
        2、进行翻转时，假设待翻转子数组的首尾下标分别为 i、j，则 nums[i-1] = a, nums[i] = b, nums[j] = c, nums[j+1] = d
            2.1、若 i = 0, 0 < j < n-1，则 incr = abs(d - nums[0]) - abs(d - c)，即 j从1遍历到n-2
            2.2、若 j = n-1, 0 < i < n-1，则 incr = abs(nums[n-1] - a) - abs(b - a)，即 i从1遍历到n-2
            上面这两种情况，可综合为将i从1遍历到n-2，incr = max(abs(d - nums[0]) - abs(d - c), abs(nums[n-1] - a) - abs(b - a))
            = max(abs(nums[i+1] - nums[0]) - abs(nums[i+1] - nums[i]), abs(nums[n-1] - nums[i-1]) - abs(nums[i] - nums[i-1]))

            2.3、若 0 < i < j < n-1，此时假设 ，
            则 incr = abs(c - a) + abs(d - b) - abs(b - a) - abs(d - c)
            由于 abs(a - b) = max(a, b) - min(a, b)，a + b = max(a, b) + min(a, b)
            所以 a + b + abs(a - b) = 2 * max(a, b)，a + b - abs(a - b) = 2 * min(a, b)
            其中，a、b、c、d 之间的大小关系有24种情况，不过可以分为以下3大类：

                第1大类：
                max(a, b) <= min(c, d) 对应4种情况：a <= b <= c <= d、b <= a <= c <= d、a <= b <= d <= c、b <= a <= d <= c
                此时，incr = c - a + d - b - abs(b - a) - abs(d - c) = (c + d - abs(d - c)) - (a + b + abs(b - a))
                          = 2 * min(c, d) - 2 * max(a, b) = 2 * (min(c, d) - max(a, b)) >= 0
                根据对称性，max(c, d) <= min(a, b) 也对应4种情况：
                此时，incr = 2 * min(a, b) - 2 * max(c, d) = 2 * (min(a, b) - max(c, d)) >= 0

                第2大类：
                max(a, c) <= min(b, d) 对应4种情况：a <= c <= b <= d、c <= a <= b <= d、a <= c <= d <= b、c <= a <= d <= b
                此时，incr = abs(c - a) + abs(d - b) - (b - a) - (d - c) = (a + c + abs(c - a)) - (b + d - abs(d - b))
                          = 2 * max(a, c) - 2 * min(b, d) = 2 * (max(a, c) - min(b, d)) <= 0
                根据对称性，max(b, d) <= min(a, c) 也对应4种情况：
                此时，incr = 2 * min(a, c) - 2 * max(b, d) = 2 * (min(a, c) - max(b, d)) <= 0

                第3大类：
                max(a, d) <= min(b, c) 对应4种情况：a <= d <= c <= b、d <= a <= c <= b、a <= d <= b <= c、d <= a <= b <= c
                此时，incr = (c - a) + (b - d) - (b - a) - (c - d) = 0
                根据对称性，max(b, c) <= min(a, d) 也对应4种情况：
                此时，incr = (a - c) + (d - b) - (a - b) - (d - c) = 0

            综上以上3大类可知，当0 < i < j < n-1时，只有 max(a, b) <= min(c, d) 或 max(c, d) <= min(a, b) 时，incr 才可能为正数，
            要使incr尽量大，则意味着要使 max(a, b)、max(c, d) 要尽量小，min(c, d)、min(a, b) 要尽量大
            可综合为将i从1遍历到n-2，记录此过程中的 min_max = min(min_max, max(a, b), max(b, c))，max_min = max(max_min, min(b, c), min(a, b))
            最终最大的incr = 2 * (max_min - min_max)
        """
        n = len(nums)
        if n == 1:
            return nums[0]
        # -10^5 <= nums[i] <= 10^5
        max_min, min_max = -10 ** 5, 10 ** 5
        first, last = nums[0], nums[n - 1]
        base, incr = abs(nums[n - 1] - nums[n - 2]), 0
        for i in range(1, n - 1):
            a, b, c = nums[i - 1], nums[i], nums[i + 1]
            base += abs(b - a)
            # 当 i = 0, 0 < j < n-1 时 以及 当 j = n-1, 0 < i < n-1 时
            incr = max(incr, max(abs(c - first) - abs(c - b), abs(last - a) - abs(b - a)))
            # 当 0 < i < j < n-1 时
            max_min = max(max_min, min(b, c), min(a, b))
            min_max = min(min_max, max(a, b), max(b, c))
        return base + max(incr, 2 * (max_min - min_max))


if __name__ == '__main__':
    print(Solution().maxValueAfterReverse(nums=[2, 3, 1, 5, 4]))
