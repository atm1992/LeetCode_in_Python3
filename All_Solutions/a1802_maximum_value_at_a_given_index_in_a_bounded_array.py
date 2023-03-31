# -*- coding: utf-8 -*-
# @date: 2023/3/30
# @author: liuquan
"""
title: 有界数组中指定下标处的最大值
You are given three positive integers: n, index, and maxSum. You want to construct an array nums (0-indexed) that satisfies the following conditions:
    nums.length == n
    nums[i] is a positive integer where 0 <= i < n.
    abs(nums[i] - nums[i+1]) <= 1 where 0 <= i < n-1.
    The sum of all the elements of nums does not exceed maxSum.
    nums[index] is maximized.
Return nums[index] of the constructed array.
Note that abs(x) equals x if x >= 0, and -x otherwise.


Example 1:
Input: n = 4, index = 2,  maxSum = 6
Output: 2
Explanation: nums = [1,2,2,1] is one array that satisfies all the conditions.
There are no arrays that satisfy all the conditions and have nums[2] == 3, so 2 is the maximum nums[2].

Example 2:
Input: n = 6, index = 1,  maxSum = 10
Output: 3


Constraints:
1 <= n <= maxSum <= 10^9
0 <= index < n
"""


class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        """
        二分查找 + 贪心check
        要想使nums[index]最大，并满足abs(nums[i] - nums[i+1]) <= 1，则index左右两侧应尽量都是公差为1的等差数列。
        一直向两侧延伸为1，直到左右边界
        """

        def check(num: int) -> bool:
            total = num
            # 左右两侧等差数列的最大长度
            left_size, right_size = min(index, num - 1), min(n - index - 1, num - 1)
            # 左右两侧等差数列的首项
            left_first, right_first = num - left_size, num - right_size
            total += left_size * (left_first + num - 1) // 2 + right_size * (right_first + num - 1) // 2
            total += max(0, index - left_size) + max(0, n - index - 1 - right_size)
            return total <= maxSum

        # 先将n个元素都置为1，然后将剩下的 maxSum - n 都分配给index
        left, right = 1, 1 + maxSum - n
        while left < right:
            mid = (left + right + 1) // 2
            if check(mid):
                left = mid
            else:
                right = mid - 1
        return left


if __name__ == '__main__':
    print(Solution().maxValue(n=6, index=1, maxSum=10))
