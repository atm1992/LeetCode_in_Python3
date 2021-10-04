# -*- coding: UTF-8 -*-
"""
title：接雨水。
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.


Example 1:
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

Example 2:
Input: height = [4,2,0,3,2,5]
Output: 9


Constraints:
n == height.length
1 <= n <= 2 * 10^4
0 <= height[i] <= 10^5
"""
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        """暴力法。对于数组中的每个元素，只考虑该柱子上方能盛多少水。柱子上能盛多少水，取决于该柱子左右两侧最近的最大值。
        时间复杂度O(N^2)，空间复杂度为O(1)"""
        if len(height) < 3:
            return 0
        res = 0
        for i in range(len(height)):
            extra_height = min(max(height[:i]) if height[:i] else 0, max(height[i + 1:]) if height[i + 1:] else 0) - height[i]
            if extra_height > 0:
                res += extra_height
        return res

    def trap_2(self, height: List[int]) -> int:
        """动态规划。上个方法中存在大量的重复计算，对于每个柱子都需要遍历一次左右两侧的最高柱子。
        可使用两个数组left_max、right_max来分别存储左右两侧的最高柱子，left_max[i]表示下标为i柱子左侧的最高柱子。这样就只需遍历一次便可得到结果，避免重复计算。
        时间复杂度O(N)，空间复杂度为O(N)"""
        if len(height) < 3:
            return 0
        n = len(height)
        # 千万不能写成left_max = right_max = [0] * n，否则修改right_max的同时也会修改left_max
        # 引用传递，left_max、right_max指向的是同一个数组
        left_max, right_max = [0] * n, [0] * n
        res = 0
        # 初始化
        for i in range(1, n):
            left_max[i] = max(height[i - 1], left_max[i - 1])
        for i in range(n - 2, -1, -1):
            right_max[i] = max(height[i + 1], right_max[i + 1])
        # 第一个柱子以及最后一个柱子上面肯定是没有水的
        for i in range(1, n - 1):
            extra_height = min(left_max[i], right_max[i]) - height[i]
            if extra_height > 0:
                res += extra_height
        return res

    def trap_3(self, height: List[int]) -> int:
        """双指针法。时间复杂度O(N)，空间复杂度为O(1)"""
        if len(height) < 3:
            return 0
        left, right = 0, len(height) - 1
        left_max = right_max = 0
        res = 0
        while left < right:
            # 更新left_max, right_max。确保此时的left_max一定大于等于height[left]，从而确保left_max - height[left]大于等于0
            left_max = max(height[left], left_max)
            right_max = max(height[right], right_max)
            # 能盛多少水，取决于短板（矮的那个）
            if height[left] < height[right]:
                # res每次累加的都是当前柱子上能接多少雨水
                res += left_max - height[left]
                left += 1
            else:
                res += right_max - height[right]
                right -= 1
        return res


if __name__ == '__main__':
    print(Solution().trap_2([4, 2, 0, 3, 2, 5]))
