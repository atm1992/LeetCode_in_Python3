# -*- coding: UTF-8 -*-
"""
title: 柱状图中最大的矩形
Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.


Example 1:
Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.

Example 2:
Input: heights = [2,4]
Output: 4


Constraints:
1 <= heights.length <= 10^5
0 <= heights[i] <= 10^4
"""
from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """依次以每根柱子的高度heights[i]为基准，分别向左右两侧延伸，找到能以该高度覆盖的所有柱子(即 宽度)，两者之积 为当前柱子的最大面积。"""
        n = len(heights)
        # 使用左右边界数组分别存储当前柱子(i)的左右边界(heights数组下标)：左侧最后一个小于当前heights[i]的元素下标；右侧第一个小于当前heights[i]的元素下标。
        # 使用哨兵 -1、n 分别表示最左侧、最右侧范围以外的下标。
        left_boundary, right_boundary = [0] * n, [0] * n
        # 单调栈，栈中的柱子高度单调递增。每个元素均为一个二元组(heights[i], i)
        mono_stack = []
        for i in range(n):
            cur_height = heights[i]
            while mono_stack and mono_stack[-1][0] >= cur_height:
                mono_stack.pop()
            left_boundary[i] = mono_stack[-1][1] if mono_stack else -1
            mono_stack.append((cur_height, i))

        # 单调栈，栈中的柱子高度单调递增。每个元素均为一个二元组(heights[i], i)
        mono_stack = []
        for i in range(n - 1, -1, -1):
            cur_height = heights[i]
            while mono_stack and mono_stack[-1][0] >= cur_height:
                mono_stack.pop()
            right_boundary[i] = mono_stack[-1][1] if mono_stack else n
            mono_stack.append((cur_height, i))

        return max((right_boundary[i] - left_boundary[i] - 1) * height for i, height in enumerate(heights))

    def largestRectangleArea_2(self, heights: List[int]) -> int:
        """优化方法一。在一次遍历中，同时更新左右边界数组。"""
        n = len(heights)
        # 将右边界的默认值设为n的原因：有些元素可能始终不出栈mono_stack，因为在右侧始终没遇到小于等于它的元素，也就意味着它的右边界为n
        left_boundary, right_boundary = [0] * n, [n] * n
        mono_stack = []
        for i in range(n):
            cur_height = heights[i]
            # 栈顶元素(下标j)出栈，意味着元素j大于等于元素i。
            # 并且j+1 ~ i之间的元素都大于元素j，因为如果j+1 ~ i之间存在小于等于元素j的元素，那么元素j在当时就已经出栈了，而不会等到现在。
            # 所以元素i为元素j右侧第一个小于等于它的元素。上一个方法是要求右侧第一个小于它的元素，因此元素j最终求得的最大面积不一定是正确值，
            # 但这并不影响最终答案，因为最终要求的是整个柱状图中的最大面积，而非单个元素所对应的最大面积。因为对于高度相等的多个元素，
            # 总有一个元素能够取到正确的右边界，即 最后一个等于该高度的元素，它的右边界一定小于该高度。
            while mono_stack and mono_stack[-1][0] >= cur_height:
                right_boundary[mono_stack[-1][1]] = i
                mono_stack.pop()
            left_boundary[i] = mono_stack[-1][1] if mono_stack else -1
            mono_stack.append((cur_height, i))
        return max((right_boundary[i] - left_boundary[i] - 1) * height for i, height in enumerate(heights))


if __name__ == '__main__':
    print(Solution().largestRectangleArea_2([2, 1, 5, 6, 2, 3]))
