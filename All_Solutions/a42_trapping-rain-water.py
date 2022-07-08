# -*- coding: UTF-8 -*-
"""
title：接雨水
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
        """
        动态规划。时间复杂度为O(n)，空间复杂度为O(n)
        使用两个数组left_max、right_max来分别存储左右两侧的最高柱子，left_max[i]表示下标为i柱子左侧的最高柱子，right_max[i]表示下标为i柱子右侧的最高柱子。
        """
        n = len(height)
        if n < 3:
            return 0
        # 千万不能写成left_max = right_max = [0] * n，否则修改right_max的同时也会修改left_max
        left_max, right_max = [0] * n, [0] * n
        for i in range(1, n):
            left_max[i] = max(height[i - 1], left_max[i - 1])
            right_max[n - i - 1] = max(height[n - i], right_max[n - i])
        res = 0
        # 第一个柱子和最后一个柱子上肯定没有水
        for i in range(1, n - 1):
            extra_height = min(left_max[i], right_max[i]) - height[i]
            if extra_height > 0:
                res += extra_height
        return res

    def trap_2(self, height: List[int]) -> int:
        """递减单调栈。时间复杂度为O(n)，空间复杂度为O(n)"""
        if len(height) < 3:
            return 0
        stack = []
        res = 0
        for i, h in enumerate(height):
            while stack and h > stack[-1][1]:
                # 将stack中的最后一个元素的高度作为水平面，倒数第二个元素的高度作为左边界，当前高度h作为右边界，计算这个围绕区域的盛水量
                _, level = stack.pop()
                if not stack:
                    break
                j, left_h = stack[-1]
                res += (min(left_h, h) - level) * (i - j - 1)
            stack.append((i, h))
        return res

    def trap_3(self, height: List[int]) -> int:
        """
        双指针。时间复杂度为O(n)，空间复杂度为O(1)
        假设有两个指针i(从左向右移动)、j(从右向左移动)，移动i时会更新i_left_max，移动j时会更新j_right_max，
        虽然没有计算i_right_max、j_left_max，但可以肯定的是 j_left_max >= i_left_max（因为j在i的右侧）、i_right_max >= j_right_max（因为i在j的左侧），
        如果i_left_max < j_right_max，那么i_left_max一定会小于i_right_max，所以此时应该计算柱子i上的盛水量，然后i向右移动
        柱子i上的盛水量为：min(i_left_max, i_right_max) - height[i] = i_left_max - height[i]
        """
        n = len(height)
        if n < 3:
            return 0
        left, right = 0, n - 1
        left_max = right_max = 0
        res = 0
        # 当left==right时，无需计算盛水量，因为这个柱子是所有柱子中的最高柱子，上面不会有雨水
        while left < right:
            # 更新left_max, right_max。注意：left_max始终大于等于当前柱子的高度height[left]
            left_max = max(height[left], left_max)
            right_max = max(height[right], right_max)
            if left_max < right_max:
                # res每次累加的都是当前柱子上能接多少雨水
                res += left_max - height[left]
                left += 1
            else:
                res += right_max - height[right]
                right -= 1
        return res


if __name__ == '__main__':
    print(Solution().trap_3([4, 2, 0, 3, 2, 5]))
