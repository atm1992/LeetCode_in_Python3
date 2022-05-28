# -*- coding: UTF-8 -*-
"""
title: 直方图最大矩形面积
给定非负整数数组 heights ，数组中的数字用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。
求在该柱状图中，能够勾勒出来的矩形的最大面积。


示例 1:
输入：heights = [2,1,5,6,2,3]
输出：10
解释：最大的矩形为图中红色区域，面积为 10

示例 2：
输入： heights = [2,4]
输出： 4


提示：
1 <= heights.length <=10^5
0 <= heights[i] <= 10^4
"""
from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """单调栈。寻找每个高度的最大长度"""
        n = len(heights)
        # 左右边界下标。
        # left_boundary[i] 表示heights[i]左侧最后一个小于其值的元素下标j，即 heights[j] < heights[i]，且 j+1 ~ i 之间的所有高度均大于等于heights[i]；
        # right_boundary[i] 表示heights[i]右侧第一个小于其值的元素下标j，即 heights[j] < heights[i]，且 i ~ j-1 之间的所有高度均大于等于heights[i]。
        # 若左侧不存在小于heights[i]的元素，则left_boundary[i]为-1；若右侧不存在小于heights[i]的元素，则right_boundary[i]为n。
        left_boundary, right_boundary = [0] * n, [0] * n
        # 更新left_boundary
        stack = []
        for i in range(n):
            tmp = heights[i]
            while stack and stack[-1][0] >= tmp:
                stack.pop()
            left_boundary[i] = stack[-1][1] if stack else -1
            stack.append((tmp, i))
        # 更新right_boundary
        stack = []
        for i in range(n - 1, -1, -1):
            tmp = heights[i]
            while stack and stack[-1][0] >= tmp:
                stack.pop()
            right_boundary[i] = stack[-1][1] if stack else n
            stack.append((tmp, i))
        return max(heights[i] * (right_boundary[i] - left_boundary[i] - 1) for i in range(n))

    def largestRectangleArea_2(self, heights: List[int]) -> int:
        """单调栈。优化方法一，在一次遍历中同时更新left_boundary、right_boundary"""
        n = len(heights)
        # 注意：right_boundary 的默认值为n
        left_boundary, right_boundary = [0] * n, [n] * n
        stack = []
        for i in range(n):
            tmp = heights[i]
            # 栈顶元素(下标j)出栈，意味着元素j大于等于元素i。
            # 并且j+1 ~ i-1之间的元素都大于元素j，因为如果j+1 ~ i-1之间存在小于等于元素j的元素，那么元素j在当时就已经出栈了，而不会等到现在。
            # 所以元素i为元素j右侧第一个小于等于它的元素。上一个方法是要求右侧第一个小于它的元素，因此元素j最终求得的最大面积不一定是正确值，
            # 但这并不影响最终答案，因为最终要求的是整个柱状图中的最大面积，而非单个元素所对应的最大面积。因为对于高度相等的多个元素，
            # 总有一个元素能够取到正确的右边界，即 最后一个等于该高度的元素，它的右边界一定小于该高度。
            while stack and stack[-1][0] >= tmp:
                _, idx = stack.pop()
                right_boundary[idx] = i
            left_boundary[i] = stack[-1][1] if stack else -1
            stack.append((tmp, i))
        return max(heights[i] * (right_boundary[i] - left_boundary[i] - 1) for i in range(n))


if __name__ == '__main__':
    print(Solution().largestRectangleArea_2([2, 1, 5, 6, 2, 3]))
